import logging

from rest_framework import exceptions, status as http_status
from rest_framework.response import Response

from . import custom_exceptions


logger = logging.getLogger('django.error.log')


def user_already_exists() -> exceptions.APIException:  # 409
    logger.error('The email has already been registered. Please login')

    return custom_exceptions.ConflictError(
        detail={
            'error': {
                'code': 'ur_002',
                'message': 'The email has already been registered. Please login'
            }
        },
        code='email_exists'
    )


def user_unacceptable_password(message: str) -> exceptions.APIException:  # 422
    return custom_exceptions.UnprocessableEntityError(
        detail={
            'error': {
                'code': 'ur_003',
                'message': message
            }
        },
        code='password_invalid'
    )


def user_email_or_password_not_found() -> exceptions.AuthenticationFailed:  # 401
    return exceptions.AuthenticationFailed(
        detail={
            'error': {
                'code': 'ul_001',
                'message': 'Email or password not found'
            }
        },
        code='email_or_password_not_found'
    )


def user_id_not_exist():  # 404
    return exceptions.NotFound(
        detail={
            'error': {
                'code': 'user_001',
                'message': 'user id not exist.'
            }
        },
        code='user_id_not_found'
    )


def user_account_disabled() -> exceptions.PermissionDenied:  # 403
    return exceptions.PermissionDenied(
        detail={
            'error': {
                'code': 'ul_002',
                'message': 'Your account has been disabled. '
                           'Please contact customer service to activate it'
            }
        },
        code='account_disabled'
    )


def user_is_not_seller() -> exceptions.PermissionDenied:  # 403
    return exceptions.PermissionDenied(
        detail={
            'error': {
                'code': 'pos_seller_001',
                'message': 'You have not authorization for use this platform. '
                           'Please contact sales manager to get your credentials'
            }
        },
        code='personal_without_authorization'
    )


def customer_not_found():  # 404
    return exceptions.NotFound(
        detail={
            'error': {
                'code': 'pos_customer_001',
                'message': 'user is not active or not exist.'
            }
        },
        code='customer_not_found'
    )


def invalid_medium():  # 404
    return exceptions.NotFound(
        detail={
            'error': {
                'code': 'checkout_005',
                'message': 'medium awareness not found and is required for close this order.'
            }
        },
        code='medium_awareness_not_found'
    )


def pos_not_found():  # 404
    return exceptions.NotFound(
        detail={
            'error': {
                'code': 'pos_010',
                'message': 'point of sale not registered.'
            }
        },
        code='customer_not_found'
    )


def pos_not_found():  # 404
    return exceptions.NotFound(
        detail={
            'error': {
                'code': 'pos_007',
                'message': 'Point of sale not found.'
            }
        },
        code='pos_not_found'
    )


def incorrect_parameter(parameter: str):  # 400
    return exceptions.ValidationError(
        detail={
            'error': {
                'code': 'ufp_004',
                'message': f'Parameter `{parameter}` is incorrect. Please enter correct value'
            }
        },
        code='incorrect_parameter'
    )


def incorrect_amount(amount, total):  # 400
    return exceptions.ValidationError(
        detail={
            'error': {
                'code': 'checkout_001',
                'message': f'Amount ${ str(total) } in payment is incorrect. '
                           f'Please enter correct value because amount must be complete '
                           f'the total of this order ${ str(amount) }'
            }
        },
        code='incorrect_amount'
    )


def acknowledgement() -> Response:
    return Response(
        data={},
        status=http_status.HTTP_204_NO_CONTENT
    )


def token_expired():
    """token has expired or it never existed"""
    return exceptions.NotFound(
        detail={
            'error': {
                'code': 'ufp_005',
                'message': 'The entered token has expired. Please generate a new one'
            }
        },
        code='token_expired'
    )


def catalog_disabled(slug: str):  # 403
    return exceptions.PermissionDenied(
        detail={
            'error': {
                'code': 'cd_001',
                'message': f'The catalog for `{slug}` has been disabled'
            }
        },
        code='catalog_disabled'
    )


def incorrect_slug(slug: str):  # 400
    return exceptions.ValidationError(
        detail={
            'error': {
                'code': 's_001',
                'message': f'The slug `{slug}` does not exists. '
            }
        },
        code='incorrect_parameter'
    )


def item_not_found():  # 404
    return exceptions.NotFound(
        detail={
            'error': {
                'code': 'pos_product_001',
                'message': 'item is not available or not exist.'
            }
        },
        code='product_not_found'
    )


def incorrect_carrier(carrier: str):  # 400
    return exceptions.ValidationError(
        detail={
            'error': {
                'code': 'c_001',
                'message': f'The carrier `{carrier}` does not exists'
            }
        },
        code='incorrect_parameter'
    )


def duplicated_address():  # 400
    return exceptions.ValidationError(
        detail={
            'error': {
                'code': 'checkout_002',
                'message': 'You have duplicated address for a group of products.'
            }
        },
        code='duplicated_parameter'
    )


def address_must_not_be():
    return exceptions.ValidationError(
        detail={
            'error': {
                'code': 'checkout_005',
                'message': 'Address must not be when you use a method pickup.'
            }
        },
        code='invalid_parameter'
    )


def shipping_invalid_for_pod():
    return exceptions.ValidationError(
        detail={
            'error': {
                'code': 'checkout_006',
                'message': 'You can only use onfleet with pod.'
            }
        },
        code='invalid_pod_shipping'
    )


def invalid_multishipping_for_pod():
    return exceptions.ValidationError(
        detail={
            'error': {
                'code': 'checkout_007',
                'message': 'You can not use different addresses with pod.'
            }
        },
        code='invalid_pod_multishipping'
    )


def invalid_month_for_pod():
    return exceptions.ValidationError(
        detail={
            'error': {
                'code': 'checkout_008',
                'message': 'Must not have shipping with different months respect to order in pod.'
            }
        },
        code='invalid_pod_month'
    )


def invalid_year_for_pod():
    return exceptions.ValidationError(
        detail={
            'error': {
                'code': 'checkout_009',
                'message': 'Must not have shipping with different years respect to order in pod.'
            }
        },
        code='invalid_pod_year'
    )


def invalid_quantity_for_update():
    return exceptions.ValidationError(
        detail={
            'error': {
                'code': 'checkout_010',
                'message': 'Check your quantity, you have not this quantity available for update.'
            }
        },
        code='invalid_quantity_for_update'
    )


def pod_in_multipayment():
    return exceptions.ValidationError(
        detail={
            'error': {
                'code': 'checkout_004',
                'message': 'You can not use pod with multipayment.'
            }
        },
        code='invalid_pod_in_multipayment'
    )


def duplicated_address_in_products():  # 400
    return exceptions.ValidationError(
        detail={
            'error': {
                'code': 'checkout_003',
                'message': 'You have duplicated items(product and address) in products products.'
            }
        },
        code='duplicated_parameter'
    )


def incorrect_date(date: str):  # 400
    return exceptions.ValidationError(
        detail={
            'error': {
                'code': 'd_001',
                'message': f'The date `{date}` in invalid or is not provided'
            }
        },
        code='incorrect_parameter'
    )    


def invalid_field(field: str) -> exceptions.APIException:  # 422
    """the field is in wrong format or the type is wrong"""
    return custom_exceptions.UnprocessableEntityError(
        detail={
            'error': {
                'code': 'ur_004',
                'message': f'{field} is invalid'
            }
        },
        code='invalid_field'
    )


def cart_product_unavailable(names: list):  # 404
    return exceptions.NotFound(
        detail={
            'error': {
                'code': 'ci_001',
                'message': 'The following products are unavailable: {}'.format(', '.join(names))
            }
        }
    )


def cart_already_exists():  # 409
    return custom_exceptions.ConflictError(
        detail={
            'error': {
                'code': 'ce_001',
                'message': 'You have an existing cart. Please try to fetch it'
            }
        },
        code='cart_exists'
    )


def cart_empty():  # 404
    return exceptions.NotFound(
        detail={
            'error': {
                'code': 'cem_001',
                'message': 'Your cart is empty. Please add some items to view or modify it'
            }
        },
        code='cart_empty'
    )


def address_not_found():  # 404
    return exceptions.NotFound(
        detail={
            'error': {
                'code': 'uae_001',
                'message': 'Address not found'
            }
        }
    )


def order_not_found():
    return exceptions.NotFound(
        detail={
            'error': {
                'code': 'order_007',
                'message': 'Order not found'
            }
        }
    )


def validation_errors(error_dict) -> exceptions.ValidationError:  # 400
    """missing or invalid fields"""
    if isinstance(error_dict, str):
        keys = error_dict
        error_dict = {error_dict: 'This field is required'}
    elif 'error' in error_dict:
        return exceptions.ValidationError(
            detail=error_dict
        )
    else:
        keys = list(error_dict.keys())

    return exceptions.ValidationError(
        detail={
            'error': {
                'code': 'ur_001',
                'message': 'Validation Error',
                'fields': keys,
                'details': error_dict
            }
        }
    )


def invalid_coupon():  # 400
    """this coupon cannot be applied to the cart"""
    return exceptions.ValidationError(
        detail={
            'error': {
                'code': 'inv_001',
                'message': 'This coupon cannot be applied to your cart'
            }
        },
        code='invalid_coupon'
    )


def invalid_carrier(carrier, postal_code):  # 400
    """Chosen carrier is invalid"""
    return exceptions.ValidationError(
        detail={
            'error': {
                'code': 'inc_001',
                'message': f'{carrier} cannot deliver to {postal_code}'
            }
        },
        code='invalid_carrier'
    )


def missing_field(field):  # 422
    raise custom_exceptions.UnprocessableEntityError(
        detail={
            'error': {
                'code': 'ur_005',
                'message': f'Parameter `{field}` not found. Please retry with correct data'
            }
        },
        code='password_invalid'
    )


def pk_field(field):  # 422
    raise custom_exceptions.UnprocessableEntityError(
        detail={
            'error': {
                'code': 'field_001',
                'message': f'field `{field}` is a incorrect type.'
                           f'Please retry with correct data, must be a integer.'
            }
        },
        code='id_invalid'
    )


def empty_list_field(field):  # 422
    raise custom_exceptions.UnprocessableEntityError(
        detail={
            'error': {
                'code': 'field_002',
                'message': 'the field ' + field + ' is empty.'
            }
        },
        code='list_empty'
    )
