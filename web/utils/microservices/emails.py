import json

from .publisher import publish

queue = 'email'


def user_register(user_id: int, password: str) -> None:
    """send user registration email"""
    publish(
        task_name='email_user_register',
        message=json.dumps({
            'user_id': user_id,
            'password': password
        }),
        queue=queue,
    )


def user_forget_password(email: str, token: str) -> None:
    """send password recovery email for forget password"""
    publish(
        task_name='email_user_forget_password',
        message=json.dumps({
            'email': email,
            'token': token
        }),
        queue=queue
    )


def user_change_password(user_id: int) -> None:
    """success message after password change"""
    publish(
        task_name='email_user_change_password',
        message=json.dumps({'user_id': user_id}),
        queue=queue
    )
