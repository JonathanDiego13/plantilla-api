# Order
* base_url: [host]/order/v1/


## Create a new order
* URL: create/
* Authentication: Token Based
* Type: POST

**Request**

```
Content-Type: application/json
token: "eyJ0eXAiOiJK.OTk0ODk0MDAsImVtYWlsIjoi.2T8Pfy28yoF_nXvw"
{
    "products": [{
        "product_child_id": 1,
        "address_id": <int>,  # optional
        "quantity": 6
    }, {
        "product_child_id": 5,
        "quantity": 2
    }, {
        "product_child_id": 11,
        "quantity": 1
    }],
    "bundles": [{
        "bundle_id": 1,
        "product_child_ids": [1, 8]
    },{
        "bundle_id": 1,
        "product_child_ids": [1, 8],
        "address_id": 2
    }, {
        "bundle_id": 2,
        "product_child_ids": [5, 6, 7],
    }],
    "shipping": {
        "address_id": <int>,
        "method": "on_fleet",
        "date": "2017-11-02",  # optional
        "from": "10:00"  # optional
        "until": "12:00",  # optional
    },
    "payment": {
        "payment_method": "credit_card",  # oxxo, bank_transfer, pod, credit_card, debit_card, paypal
        "payment_provider": "adyen",  # optional in case of bank_transfer and pod
        "msi": 1,  # only in case of credit_card
        "paypal": {  # optional
            "transaction_id": '8XS04180LL905831S',
            "payer_id": '8XD7T8PXXNWNQ',
            "payer_email": 'carlos-buyer@ksmvcapital.com',
            "payer_status": 'VERIFIED',
            "merchant_protection_eligibility": 'ELIGIBLE',
            "last_correlation_id": null,
            "last_transaction_id": '8XS04180LL905831S'
        },
        "card": { # Required for credit and debit card
        	"name": "Joey Steve",
        	"card": "4111526233333223",
        	"cvc": "123",
        	"month": "11",
        	"year": "2019",
            "device_session_id": "141221go4ghgftu412i4t12413"
		}
        
    }
}
```

**Response**

**case 1:** cart/coupons/user related issues => check [cart](CART.md)

**case 2:** scheduled shipping not available

```
status code: 409 CONFLICT
{
    "error": {
        "code": "ssu_001",
        "message": "The selected date and time are unavailable for shipping."
                   "Please select a different one",
    }
}
```

**case 3:** Invalid payment method

```
status code: 401 FORBIDDEN
{
    "error": {
        "code": "pme_001",
        "message": "The provided payment method cannot be applied to the cart. "
                   "Please choose a different method of payment"
    }
}
```

**case 4:** Payment rejected

```
status code: 400 BAD REQUEST
{
    "error": {
        "code": "pme_002",
        "message": "The payment was rejected with following message. "
                   "<custom message>"
    }
}
```

**case 5:** Success

```
status code: 201 CREATED
{
    "order": {
        "id": "10234",
    }
}
```


## List existing orders

* URL: list/
* Authentication: Token Based
* Type: GET

**Request**

```
Content-Type: application/json
token: "eyJ0eXAiOiJK.OTk0ODk0MDAsImVtYWlsIjoi.2T8Pfy28yoF_nXvw"
```

**Response**

**case 1:** No order found

```
status code: 200 OK
{
    "error": "You have no order. Please create one to view"
}
```

**case 2:** Success

```
status code: 200 OK
{
    "orders": [
        {
            "order_number": 171023120503,
            "sub_total_price": 27700,
            "sub_total_special_price": 27700,
            "coupon_code": null,
            "coupon_discount": 0,
            "discount": 0,
            "grand_total": 27700,
            "created_at": "2017-10-23"
        }, ...
    ]
}
```


# View one of the listed orders

* URL: details/<order_number>/
* Authentication: Token Based
* Type: GET

**Request**

```
Content-Type: application/json
token: "eyJ0eXAiOiJK.OTk0ODk0MDAsImVtYWlsIjoi.2T8Pfy28yoF_nXvw"
```

**Response**

**case 1:** No matching order found

```
status code: 400 BAD REQUEST
{
    "error": {
        "code": "ufp_004",
        "message": "Parameter `user_order_id` is incorrect. Please enter correct value'
    }
}
```

**case 2:** Success

```
status code: 200 OK
{
    "order": {
        "order_number": 171023311816,
        "sub_total_price": 27700,
        "sub_total_special_price": 27700,
        "coupon_code": null,
        "coupon_discount": 0,
        "discount": 0,
        "grand_total": 27700,
        "created_at": "2017-10-23"
    },
    "order_items": {
        "shipping_address": {
            "n_int": "2",
            "n_ext": "22",
            "street": "Rio Amur",
            "colony": "Cuauhtemoc",
            "city": "CDMX",
            "state": "CDMX",
            "postal_code": 6500,
            "phone_number": 5564239883,
            "additional_number": "+52155555555"
        },
        "items": [
            {
                "catalog_product_child_sku": "CO3001",
                "bundle_id": 0,
                "bundle_sequence": 0,
                "name": "Colchon Regular",
                "price": 7900,
                "special_price": 7900,
                "discount": 0,
                "is_free": false,
                "grand_total": 7900
            },
            {
                "catalog_product_child_sku": "CO3002",
                "bundle_id": 0,
                "bundle_sequence": 0,
                "name": "Colchon Matrimonial",
                "price": 9900,
                "special_price": 9900,
                "discount": 0,
                "is_free": false,
                "grand_total": 9900
            },
            {
                "catalog_product_child_sku": "CO3002",
                "bundle_id": 0,
                "bundle_sequence": 0,
                "name": "Colchon Matrimonial",
                "price": 9900,
                "special_price": 9900,
                "discount": 0,
                "is_free": false,
                "grand_total": 9900
            }
        ]
    }
}
```
