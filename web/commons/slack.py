import json
import requests
import os

def slack_checkout_error(message, data):

    if os.environ.get('ENV_MODE') == 'production':
        webhook_url = 'https://hooks.slack.com/services/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'

        slack_data = {
            'text': message,
            'icon_emoji': ':rotating_light:',
            'username': 'checkout-bot',
            'attachments': [{
                'text': data,
            }]
        }

        response = requests.post(
            webhook_url, data=json.dumps(slack_data),
            headers={'Content-Type': 'application/json'}
        )

        if response.status_code != 200:
            raise ValueError(
                'Request to slack returned an error %s, the response is:\n%s'
                 % (response.status_code, response.text)
            )


def slack_registration_error(data):

    if os.environ.get('ENV_MODE') == 'production':
        webhook_url = 'https://hooks.slack.com/services/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'

        slack_data = {
            'text': 'Registration Error',
            'icon_emoji': ':rotating_light:',
            'username': 'registration-bot',
            ''
            'attachments': [{
                'text': data,
            }]
        }

        response = requests.post(
            webhook_url, data=json.dumps(slack_data),
            headers={'Content-Type': 'application/json'}
        )

        if response.status_code != 200:
            raise ValueError(
                'Request to slack returned an error %s, the response is:\n%s'
                 % (response.status_code, response.text)
            )
