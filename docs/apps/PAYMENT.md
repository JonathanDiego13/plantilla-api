# Payment
* BASE URL: /payment/v1/
* The responses for missing parameters or incorrect parameters are same as other apps

## Get available methods
* URL: get-available-payment-methods/
* Authentication: Token Based
* Type: GET

**Request**

```
Content-Type: application/json
token: "stdfghgsdif8adfjkasnb"
```


**Response**

**case 1:** If cart is eligible for on_fleet

```
{
    "payment_methods": [
        "credit_card",
        "debit_card",
        "bank_transfer",
        "pod",
        "paypal",
        "oxxo",
    ]
}
```

**case 2:** If cart is not eligible for on_fleet

```
{
    "payment_methods": [
        "credit_card",
        "debit_card",
        "bank_transfer",
        "paypal",
        "oxxo",
    ]
}
```
