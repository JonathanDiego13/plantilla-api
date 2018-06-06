from .config import conekta


def create_order_oxxo(order):
    conekta_oxxo = conekta()
    try:
        order_info = conekta_oxxo.Order.create(
            {
                "line_items": [{
                    "name": "Tacos",
                    "unit_price": 1000,
                    "quantity": 12
                }],
                "shipping_lines": [{
                    "amount": 1500,
                    "carrier": "FEDEX"
                }],  # shipping_lines - physical goods only
                "currency": "MXN",
                "customer_info": {
                    "name": "Fulanito Pérez",
                    "email": "<a href='mailto: fulanito @ conekta.com'>fulanito@conekta.com</a>",
                    "phone": "+5218181818181"
                },
                "shipping_contact": {
                    "address": {
                        "street1": "Calle 123, int 2",
                        "postal_code": "06100",
                        "country": "MX"
                        }
                    },  # shipping_contact - required only for physical goods
                "charges": [{
                    "payment_method": {
                        "type": "oxxo_cash",
                        "payment_method": 'timestamp'
                    }
                }]
            })
    except conekta_oxxo.ConektaError as e:
        print(e.message)

    return oxxo_adapter(order_info)


def oxxo_adapter(order_data):
    return {
        "id": order_data.id,
        "payment_method": order_data.charges.data[0].payment_method.service_name,
        "reference": order_data.charges.data[0].payment_method.reference,
        "amount": (order_data.amount / 100) + order_data.currency,
        "order": {
            "quantity": order_data.line_items.data[0].quantity,
            "name": order_data.line_items.data[0].name,
            "price": (order_data.line_items.data.unit_price / 100)
        }
    }
