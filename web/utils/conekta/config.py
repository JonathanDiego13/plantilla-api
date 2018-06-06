import conekta
import os


def conekta():

    conekta.api_key = os.environ.get('CONEKTA_KEY')
    conekta.api_version = os.environ.get('CONEKTA_VERSION')

    return conekta
