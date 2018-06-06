import os
from celery import Celery

celery_app = Celery()
celery_app.conf.update(
    accept_content=['json'],
    enable_utc=False,
    timezone=os.environ.get('TIME_ZONE', 'America/Mexico_City'),
    task_store_errors_even_if_ignored=True,
    task_time_limit=600,  # After 10 min the task will be killed
    broker_pool_limit=1,  # number of connections in the connection pool
    worker_send_task_events=True,  # for monitoring
    task_send_sent_event=True,
    broker_url=os.environ.get('BROKER_URL'),
    result_backend=os.environ.get('CELERY_RESULT_BACKEND'),
    broker_heartbeat = 240,
    broker_heartbeat_checkrate = 2
)


def publish(task_name: str, message: str, queue: str, exchange: str = 'direct') -> None:
    """
    send message to broker
    :param exchange: Named custom exchange to send the task to
    :param task_name: Name of the task
        email_user_register: To send registration email to the user
        email_user_forget_password: To send forgot password email
        email_user_change_password: To send change password email
    :param message: body of the message to be sent to the task
    :param queue: Name of the message queue to send this message to
        ['state_machine', 'emails']
    :return: None
    """
    try:
        celery_app.send_task(
            task_name,
            (message,),
            queue=queue,
            exchange=exchange,
            serializer='json'
        )
    except Exception as e:
        print(e)
