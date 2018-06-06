import requests
import json
import os
from .helpers import get_gateway_data, payment_method_adapter

HEADERS = {'Content-Type': 'application/json'}

gateways = {
    'test': 'Ye0Kb9FOmmFul0ZbPC10TW8qjVN',
    'adyen': 'EIIiwxSzo4me8sA4Gn62KjuiVQR',
    'payu': 'OXhebq6rWMerOj7m1si5FpsFRLM',
    'openpay': 'FaymjtplojunHMKeEeoXhNekxpg',
    'netpay': None
}


def spreedly(data, url):
    return requests.post(
        url="https://core.spreedly.com" + url,
        auth=(os.environ.get('SPREEDLY_KEY'), os.environ.get('SPREEDLY_SECRET')),
        headers=HEADERS, data=json.dumps(data)
    )


class PaymentSpreedly:

    def __init__(self, payment=None, amount=None, order_number=None, extra=None, gateway=None):
        self.payment = payment
        self.card = payment.get('card')
        self.amount = amount
        self.order_number = order_number
        self.extra = extra
        self.gateway = gateway

    def create_spreedly_payment_method(self):

        data = payment_method_adapter(self.extra, self.card, self.order_number)

        response = spreedly(data, '/v1/payment_methods.json')
        transaction = json.loads(response.text)

        return transaction['transaction']['payment_method']['token']

    def create_payment(self):
        """
            amount: la cantidad a cobrar
            gateway: la pasarela elegida (adyen, conekta, ... )
        """
        gateway_token = gateways.get(self.gateway)

        url = '/v1/gateways/' + gateway_token + '/purchase.json'

        data = {
            'transaction': {
                'payment_method_token': self.create_spreedly_payment_method(),
                'amount': int(self.amount * 100),
                'currency_code': 'MXN',
                'order_id': self.order_number,
                'description': self.extra.get('sku') or None,
                'retain_on_success': True,
                'ip': self.extra.get('ip') or None,
                'email': self.extra.get('email'),
                'country': 'Mexico',
                'phone': self.extra.get('phone_number') or None,
                'shipping_address': {
                    'address1': self.extra.get('address').street,
                    'address2': self.extra.get('address').n_ext + self.extra.get('address').n_int,
                    'city': self.extra.get('address').city,
                    'state': self.extra.get('address').state,
                    'zip': self.extra.get('address').postal_code,
                    'country': 'México',
                    'phone': self.extra.get('address').phone_number or None
                }
            }
        }

        data['transaction']['gateway_specific_fields'] = get_gateway_data(
            self.amount, self.gateway, self.order_number, self.payment, self.extra
        )

        response = spreedly(data, url)
        return json.loads(response.text)

    def check(self):
        payment = self.create_payment()
        return payment
