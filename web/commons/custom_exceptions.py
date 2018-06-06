from rest_framework import exceptions
from rest_framework import status


class ConflictError(exceptions.APIException):
    status_code = status.HTTP_409_CONFLICT
    default_detail = ('A conflict has occurred',)
    default_code = 'conflict'


class UnprocessableEntityError(exceptions.APIException):
    status_code = status.HTTP_422_UNPROCESSABLE_ENTITY
    default_detail = ('Unable to process the request content',)
    default_code = 'cannot_process'


class FakeSuccess(exceptions.APIException):
    """fake the success. e.g while logging out"""
    status_code = status.HTTP_204_NO_CONTENT
    default_detail = ('The request was successfully processed',)
    default_code = 'no_content'
