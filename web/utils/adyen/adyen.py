import os
import pytz
from datetime import datetime, timedelta
from functools import lru_cache
import Adyen
from commons import custom_responses

@lru_cache(maxsize=2)
def get_adyen_instance(get_method=False):
    adyen = Adyen.Adyen()
    client = adyen.client
    client.hmac = os.environ.get('ADYEN_HMAC')
    client.platform = os.environ.get('ADYEN_PLATFORM')
    client.app_name = os.environ.get('ADYEN_APP_NAME')
    if not get_method:
        client.username = os.environ.get('ADYEN_USERNAME')
        client.password = os.environ.get('ADYEN_PASSWORD')
    return adyen


def authorize_and_capture(request) -> dict:
    '''
    To query adyen for validity of the payment
    :return: adapter for adyen_request
    '''

    adyen = get_adyen_instance()

    try:
        response = adyen.payment.authorise(request)
        return response.message
    except Exception:
        raise custom_responses.invalid_field('card')
