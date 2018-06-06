from rest_framework.response import Response
from rest_framework import status as http_status


def response_ok(data):
    return Response(
        data=data,
        status=http_status.HTTP_200_OK
    )


def response_created(data):
    return Response(
        data=data,
        status=http_status.HTTP_201_CREATED
    )


def response_deleted(data):
    return Response(
        data=data,
        status=http_status.HTTP_204_NO_CONTENT
    )
