from secrets import token_urlsafe
from contextlib import suppress

from rest_framework_jwt.settings import api_settings

from commons import redis_db

db_con = redis_db.redis_connection()


def generate_token(user, expires: int=2592000) -> str:
    """Generate jwt authentication token for current user"""
    jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
    jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER

    payload = jwt_payload_handler(user)
    token = jwt_encode_handler(payload)

    save_token(user_id=user.id, token=token, expires=expires)

    return token


def save_token(user_id: int, token: str, expires: int=2592000) -> None:
    """
    Save user authentication token to redis
    :expires: default expiry time: 30 days
    """
    db_con.set(name=token, value=user_id, ex=expires)


def token_exists(token: str) -> bool:
    """Check whether or not the token exists"""
    return db_con.exists(token)


def get_value_if_key_exists(key: str):
    """Get value of a key if the key exists else None"""
    return db_con.get(name=key) if db_con.exists(key) else None


def refresh_token_expiry_time(user, token: str, time: int=2592000) -> None:
    db_con.setex(name=token, time=time, value=user.id)


def delete_token(token: str) -> None:
    db_con.delete(token)


def delete_all_tokens(user_id: int) -> None:
    scan_iter = db_con.scan_iter()
    token_list = []

    for token in scan_iter:
        with suppress(ValueError, Exception):  # it can be other content
            if int(get_value_if_key_exists(key=token)) == user_id:
                token_list.append(token)

    if token_list:
        db_con.delete(*token_list)


def generate_random_token(length: int=10):
    """Generate an url_safe string of given length"""
    return token_urlsafe(length)


def generate_and_save_random_token(user_id: int, length: int=10, expires: int=43200) -> str:
    """
    Generate a random token and save it.
    default expiry time: 12 hours
    """
    token = generate_random_token(length)
    save_token(user_id=user_id, token=token, expires=expires)

    return token


def update_token_lifetime(token: str, time: int=2592000) -> None:
    db_con.expire(name=token, time=time)
