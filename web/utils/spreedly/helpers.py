import os
import hashlib
import time
import secrets
import random


def get_gateway_data(amount=None, gateway=None, order_ref=None, payment=None, extra=None):

    card = payment.get('card')

    gateway_data = {
        "test": None,
        "adyen": {
            "shopper_reference": extra.get('user_id'),
            "fraud_offset": 0,
            "selected_brand": 'visa',
            "delivery_date": extra.get('date'),  # '12/11/2018',
            "merchant_order_reference": order_ref,
            "shopper_interaction": "Ecommerce",
            # From our adyen adapter
            'amount': {
                'value': int(amount * 100),
                'currency': 'MXN'
            },
            'reference': order_ref,
            'additionalData': {
                'card.encrypted.json': payment.get('encrypted_card'),
                'riskdata.deliveryMethod': 'express',  # on_fleet / fedex
                'riskdata.basket.item.productTitle': extra.get('sku'),  # first product
            },
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
            'deviceFingerprint': extra.get('device_fingerprint')
        },
        "conekta": None,
        'netpay': {  # TODO agregar campos para checar
            'data': None
        },
        'openpay': {
            "device_session_id": card.get('device_session_id')
        },
        'payu': {
            # "order_id": order_ref,
            "cvv": card.get('cvc'),
            "installments_number": extra.get('installments') or "1",
            "user_agent": extra.get('user_agent'),
            "cookie": extra.get('cookie'),
            "device_session_id": get_device_session_id(extra.get('cookie')),
            "dni_number": str(random.choice(range(4000000000000, 4999999999999))),
            "dni_type": "TI",
            "birth_date": generate_random_date(),
            "description": "Compra en luuna.mx",
            "language": "es",
            "buyer": {
                "name": card.get('name'),
                "email": extra.get('email'),
                "dni_number": "5415668464654",
                "dni_type": "TI"
            },
            "verify_amount": int(amount * 100)  # "5100"
        }
    }
    """

    For OpenPay

    {
        "method" : "card",
        "amount" : 100,
        "description" : "Cargo inicial a mi cuenta",
        "order_id" : "oid-00051",
        "customer" : {
            "name" : "Juan",
            "last_name" : "Vazquez Juarez",
            "phone_number" : "4423456723",
            "email" : "juan.vazquez@empresa.com.mx"
        },
        "confirm" : "false",
        "send_email":"false",
        "redirect_url":"http://www.openpay.mx/index.html"
    }
    """

    # For Adyen
    # if extra.get('msi') is not None:
    #    gateway_data['adyen']['installments'] = {'value': payment.get('msi')}

    # if 'coupon_code' in extra and extra.get('coupon_code'):
    #    gateway_data['adyen']['additionalData']['riskdata.promotions.promotion.promotionName'] = \
    #        extra.get('coupon_code')

    if gateway == 'adyen':
        return {'adyen': gateway_data.get('adyen')}
    elif gateway == 'conekta':
        return gateway_data.get('conekta')
    elif gateway == 'openpay':
        return gateway_data.get('conekta')
    elif gateway == 'payu':
        return {"payu_latam": gateway_data.get('payu')}
    else:
        return gateway_data.get('test')


def payment_method_adapter(extra, card, order_number):

    data = {
        "payment_method": {
            "credit_card": {
                "first_name": extra.get('first_name'),
                "last_name": extra.get('last_name'),
                "number": card.get('card'),
                "verification_value": card.get('cvc'),
                "month": card.get('month'),
                "year": card.get('year')
            },
            "retained": True,
            "email": extra.get('email'),
            "data": {
                "user_id": extra.get('user_id'),
                "extra_stuff": {
                    "description": "Compra hecha desde luuna.mx",
                    "order_number": order_number,
                    "tipo": 'test' if not os.environ.get('ENV_MODE') == 'production' else 'real payment'
                }
            }
        }
    }

    if extra.get('shipping'):
        data['payment_method']['credit_card']['address1'] = extra.get('shipping_address')
        data['payment_method']['credit_card']['address2'] = extra.get('billing_address')
        data['payment_method']['credit_card']['country'] = 'Mexico'
        data['payment_method']['credit_card']['phone_number'] = extra.get('phone_number')
        data['payment_method']['credit_card']['company'] = "N/A"

    return data


def adapt_spreedly_result(spreedly_data, payment_data, gateway):
    """
    Adapt data spreedly to adyen data
    :param spreedly_data:
    :param adyen_data:
    :return:
    """
    payment_data['success'] = spreedly_data['transaction']['succeeded']
    payment_data['payment']['payment_gateway'] = spreedly_data['transaction']['gateway_type']

    if payment_data['success']:
        payment_data['payment']['payment_receipt_number'] = spreedly_data['transaction']['gateway_specific_response_fields']['payu_latam']['order_id'] if gateway == 'payu' else spreedly_data['transaction']['token']
        payment_data['payment']['payment_acceptance_status'] = 1
        payment_data['payment'].pop('refusal_reason')
        payment_data['payment'].pop('result_code')

    return payment_data


def get_device_session_id(cookie):
    microtime = str(time.time())
    string = cookie + microtime
    return hashlib.md5(string.encode('utf-8')).hexdigest()


def generate_random_date():
    """
    Generate a random date
    :return: datetime YYYY-MM-DD
    """
    year = random.choice(range(1940, 2000))
    month = random.choice(range(1, 13))
    day = random.choice(range(1, 29))
    birth_date = str(year) + '-' + str(month) + '-' + str(day)
    return birth_date
