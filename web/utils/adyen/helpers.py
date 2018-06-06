import os
from . import adyen


def adapt_adyen_response(adyen_data, payment_method, msi):

    additionalData = adyen_data.get('additionalData')

    expiry_month, expiry_year = additionalData.get('expiryDate').split('/')
    expiry_year = int(expiry_year)
    expiry_month = int(expiry_month)

    def _get_card_type(card_type):
        if card_type == 'credit_card':
            return 'credit'
        elif card_type == 'debit_card':
            return 'debit'
        return None

    success = adyen_data.get('resultCode') in ('Authorized', 'Authorised', 'Received')
    payment = {
        'payment_gateway': 'adyen',
        'payment_method': payment_method,
        'payment_provider': additionalData.get('acquirerAccountCode'),
        'payment_receipt_number': adyen_data.get('pspReference'),
        'payment_acceptance_status': adyen_data.get('resultCode') in ('Authorized', 'Authorised', 'Received'),
        'payment_status_code': adyen_data.get('authCode'),
        'fraud_score': adyen_data.get('fraudResult').get('accountScore'),
        'card_type': _get_card_type(payment_method),
        'card_brand': additionalData.get('paymentMethod'),
        'card_brand_type': additionalData.get('cardPaymentMethod'),
        'bank': additionalData.get('cardIssuingBank'),
        'number_of_installments': msi or 1,
        'cc_expiry_month': expiry_month,
        'cc_expiry_year': expiry_year,
        'cc_last_four_digits': int(additionalData.get('cardSummary')),
        'cc_owner_name': additionalData.get('cardHolderName'),
        'cc_bin': additionalData.get('cardBin'),
    }

    if not success:
        payment['refusal_reason'] = additionalData.get('refusalReasonRaw')
        payment['result_code'] = adyen_data.get('resultCode')

    return {'payment': payment, 'success': success}


def get_adyen_request(amount, card, order_id, extra, dfp, installments):
    request = {
        'merchantAccount': os.environ.get('ADYEN_MERCHANT_ACCOUNT'),
        'amount': {
            'value': int(amount * 100),  # in cents
            'currency': 'MXN'
        },
        'reference': order_id,
        'card': {
            'cvc': card.get('cvc'),
            'expiryMonth': card.get('month'),
            'expiryYear': card.get('year'),
            'holderName': card.get('name'),
            'number': card.get('card')
        },
        'additionalData': {
            'riskdata.deliveryMethod': 'express',  # on_fleet / fedex
            'riskdata.basket.item.productTitle': extra.get('sku'),  # first product
        },
        'shopperReference': extra.get('user_id'),  # user id
        'shopperName': {
          'firstName': extra.get('first_name'),
          'lastName': extra.get('last_name'),
        },
        'shopperEmail': extra.get('email'),
        'shopperIP': extra.get('ip'),
        'deliveryAddress': extra.get('shipping_address'),
        'billingAddress': extra.get('billing_address'),
        'telephoneNumber': extra.get('phone_number'),
        'browserInfo': {
            'userAgent': extra.get('user_agent'),
            'acceptHeader': 'application/json'
        },
        'deviceFingerprint': dfp
    }

    if installments is not None:
        request['installments'] = {'value': installments}

    if 'coupon_code' in extra and extra.get('coupon_code'):
        request['additionalData']['riskdata.promotions.promotion.promotionName'] = \
            extra.get('coupon_code')

    return request


def adyen_payment(amount, order_id, extra, payment):
    card = payment.get('card')
    payment_method = payment.get('payment_method')
    msi = payment.get('msi') if payment_method == 'credit_card' else None
    dfp = payment.get('dfp')

    adyen_request = get_adyen_request(amount, card, order_id, extra, dfp, msi)
    adyen_response = adyen.authorize_and_capture(adyen_request)
    adyen_result = adapt_adyen_response(adyen_response, payment_method, msi)

    return adyen_result


ADYEN_ERRORS = [
        ('01 : Refer to card issuer', 'ord_002'),
        ('03 : Invalid merchant', 'ord_003'),
        ('04 : Capture card', 'ord_004'),
        ('05 : Do not honor', 'ord_005'),
        ('06 : Error', 'ord_006'),
        ('07 : Pickup card, special condition', 'ord_007'),
        ('12 : Invalid transaction', 'ord_012'),
        ('13 : Invalid amount', 'ord_013'),
        ('14 : Invalid card number (no such number)', 'ord_014'),
        ('15 : Invalid issuer', 'ord_015'),
        ('30 : Format error	', 'ord_030'),
        ('41 : Lost card', 'ord_041'),
        ('43 : Stolen card', 'ord_043'),
        ('45 : Reserved', 'ord_045'),
        ('51 : Insufficient funds/over credit limit', 'ord_051'),
        ('54 : Expired card', 'ord_054'),
        ('55 : Invalid PIN', 'ord_055'),
        ('57 : Transaction not permitted to cardholder', 'ord_057'),
        ('59 : Suspected fraud', 'ord_059'),
        ('61 : Exceeds withdrawal amount limit', 'ord_061'),
        ('62 : Restricted card', 'ord_062'),
        ('63 : Security violation', 'ord_063'),
        ('65 : Exceeds withdrawal count limit', 'ord_065'),
        ('70 : Contact Card Issuer', 'ord_070'),
        ('75 : Allowable number of PIN tries exceeded', 'ord_075'),
        ('78 : Blocked, first used', 'ord_078'),
        ('80 : Credit issuer unavailable', 'ord_080'),
        ('85 : No reason to decline a request for account number verification, '
         'address verification, CVV2 verification, '
         'or a credit voucher or merchandise return', 'ord_085'),
        ('85 : Not declined (Valid for all zero amount transactions)', 'ord_085'),
        ('91 : Issuer unavailable or switch inoperative', 'ord_091'),
        ('91 : Authorization platform or issuer system inoperative', 'ord_091'),
        ('92 : Destination cannot be found for routing', 'ord_092'),
        ('92 : Unable to route transaction', 'ord_092'),
        ('93 : Transaction cannot be completed; violation of law', 'ord_093'),
        ('100 : Deny', 'ord_100'),
        ('103 : CVC is not the right length', 'ord_103'),
        ('122 : Invalid card security code (a.k.a., CID, 4DBC, 4CSC)', 'ord_122')
    ]
