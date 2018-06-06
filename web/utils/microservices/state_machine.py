import json
from .publisher import publish


def order_create(order_number, order_id):
    # activate when magneto die
    # emails.order_create(order_id=order_id)  # send email to the user

    publish(
        task_name='sm_order_machine_start',
        message=json.dumps({
            'order_id': order_id,
            'order_number': order_number,
            'user_email': 'client_api@luuna.mx'
        }),
        queue='sm_order'
    )
