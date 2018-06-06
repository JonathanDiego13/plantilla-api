# Cart
* base url: [host]/cart/v1/

### Success Response
```
status code: 200 OK (update or get) or 201 CREATED (create new)
content:
{
    "cart": {
        "user_id": 1,
        "total_products": 9,
        "value": {
            "total": 33000,
            "discount": 10800,
            "sub_total": 22200,
            "grand_total": 22200,
            "coupon_code": null,
            "coupon_value": 0,
            "total_discount": 0
        },
        "products": [
            {
                "product_child_id": 1,
                "product_parent_id": 1,
                "product_child_slug": "almohada-regular-default",
                "category_id": 1,
                "category_slug": "almohada",
                "name": "Almohada Regular",
                "price": 100,
                "size": "regular",
                "special_price": 100,
                "color": "default",
                "total_price": 200,
                "discount": 0,
                "quantity": 2,
                "bundle_id": 0,
                "bundle_sequence": 0,
                "address_id": 1,
                "is_free": false,
                "images": []
            },
            {
                "product_child_id": 11,
                "product_parent_id": 8,
                "product_child_slug": "sabana-regular-black",
                "category_id": 3,
                "category_slug": "sabana",
                "name": "Sabana Regular Black",
                "price": 1000,
                "size": "regular",
                "special_price": 1000,
                "color": "black",
                "total_price": 1000,
                "discount": 0,
                "quantity": 1,
                "bundle_id": 0,
                "bundle_sequence": 0,
                "address_id": 1,
                "is_free": false,
                "images": []
            }
        ],
        "bundles": [
            {
                "bundle_id": 1,
                "bundle_sequence": 0,
                "address_id": 1,
                "products": [
                    {
                        "discount": -400,
                        "quantity": 1,
                        "product_child_id": 1,
                        "product_parent_id": 1,
                        "product_child_slug": "almohada-regular-default",
                        "category_id": 1,
                        "category_slug": "almohada",
                        "name": "Almohada Regular",
                        "price": 100,
                        "size": "regular",
                        "special_price": 500,
                        "color": "default",
                        "total_price": 500
                    },
                    {
                        "discount": 2900,
                        "quantity": 2,
                        "product_child_id": 3,
                        "product_parent_id": 3,
                        "product_child_slug": "colchon-regular",
                        "category_id": 2,
                        "category_slug": "colchon",
                        "name": "Colchon Regular",
                        "price": 7900,
                        "size": "regular",
                        "special_price": 5000,
                        "color": "default",
                        "total_price": 10000
                    }
                ]
            },
            {
                "bundle_id": 1,
                "bundle_sequence": 1,
                "address_id": 1,
                "products": [
                    {
                        "discount": -400,
                        "quantity": 1,
                        "product_child_id": 1,
                        "product_parent_id": 1,
                        "product_child_slug": "almohada-regular-default",
                        "category_id": 1,
                        "category_slug": "almohada",
                        "name": "Almohada Regular",
                        "price": 100,
                        "size": "regular",
                        "special_price": 500,
                        "color": "default",
                        "total_price": 500
                    },
                    {
                        "discount": 2900,
                        "quantity": 2,
                        "product_child_id": 3,
                        "product_parent_id": 3,
                        "product_child_slug": "colchon-regular",
                        "category_id": 2,
                        "category_slug": "colchon",
                        "name": "Colchon Regular",
                        "price": 7900,
                        "size": "regular",
                        "special_price": 5000,
                        "color": "default",
                        "total_price": 10000
                    }
                ]
            }
        ],
        "product_cross_sell_children": [
            {
                "product_child_id": 20,
                "product_parent_id": 11,
                "color": "white",
                "price": 1200,
                "special_price": null,
                "slug": "sabana-matrimonial-white",
                "sku": "SA3013",
                "description": "queen sized white sheets",
                "size": "matrimonial",
                "height": 1,
                "width": 150,
                "length": 180,
                "weight": 1,
                "name": "Sabana Matrimonial",
                "images": []
            },
            {
                "product_child_id": 21,
                "product_parent_id": 11,
                "color": "red",
                "price": 1200,
                "special_price": null,
                "slug": "sabana-matrimonial-red",
                "sku": "SA3014",
                "description": "queen sized red sheets",
                "size": "matrimonial",
                "height": 1,
                "width": 150,
                "length": 180,
                "weight": 1,
                "name": "Sabana Matrimonial",
                "images": []
            }
        ]
    }
}
```


## Logged in Users

### Create a new cart
* URL: user/
* Authentication: Token based
* Type: POST

**Request:**

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
    }],
    "ip_address": "0.0.0.0",
    "coupon_code": "LUUNA10",   # optional
}
```

**Response**

**Case 1:** Coupon Code Invalid/Inexistent/Expired (only alphanumeric coupon is valid)

```
status: 400 BAD REQUEST
{
    "error": {
        "code": "inv_001",
        "message": "This coupon cannot be applied to your cart"
    }
}
```

**Case 2:** Token has expired or is invalid or the user is inactive
* Check [Users](USERS.md)

**Case 3:** Slug disabled or inexistent

```
{
    "error": {
        "code": "cd_001",
        "message": "The catalog for `{slug}` has been disabled"
    }
}
```

**Case 4:** Bundle disabled

```
{
    "error": {
        "code": "cbd_001",
        "message": "The bundle with id {bundle_id} has been disabled or does not exists"
    }
}
```

### Get(existing cart)
* URL: /
* Authentication: Token based
* Type: GET

**Request:**

```
Content-Type: application/json
token: "eyJ0eXAiOiJK.OTk0ODk0MDAsImVtYWlsIjoi.2T8Pfy28yoF_nXvw"
```

**Response:**

**case 1:** User doesn't have a cart

```
status: 404 NOT FOUND
{
    "error": {
        "code": "ce_002",
        "message": "You don't seem to have anything in the cart. Please add an item to proceed"
    }
}
```


###  Update(existing cart)
* URL: user/
* Authentication: Token based
* Type: PUT

**Request:**

```
Content-Type: application/json
token: "eyJ0eXAiOiJK.OTk0ODk0MDAsImVtYWlsIjoi.2T8Pfy28yoF_nXvw"
{
    "products": [{
        "slug": "almohada-regular",
        "quantity": 4
    }, {
        "slug": "colchon-individual",
        "quantity": 1
    }],
    "ip_address": "<user's ip address>",
    "coupon_code": "LUUNA10",   # optional
}
```

### Delete
* URL: user/
* Authentication: Token based
* Type: DELETE

**Request:**

```
Content-Type: application/json
token: "eyJ0eXAiOiJK.OTk0ODk0MDAsImVtYWlsIjoi.2T8Pfy28yoF_nXvw"
```

**Response:** Empty


## Anonymous User

### Get cart's data
* URL: anonymous/
* Authentication: Allow Any
* Type: POST

**Request** -> same as for logged-in user
**Response** -> Same as for logged-in user


# Notes
* in case the sku or id doesn't exist in the db, send error message immediately
* in case the sku or id is disabled, remove the item from the cart silently
