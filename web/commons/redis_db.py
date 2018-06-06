import os

import redis


def redis_connection(db: int=0):
    """
    :param db: Database to be used
    :return: redis connection
    """
    return redis.StrictRedis.from_url(url=os.environ.get('REDIS_URL'), db=db)
