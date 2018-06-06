# Catalog
* base url: catalog/v1/

### Categories
* URL: categories/
* Authentication: None
* Type: GET

**Request:**

```
Content-Type: application/json
```

**Response**

```
status code: 200 OK
{
    "categories": [
        {
            "category_id": 1,
            "category_sku": "AL1001",
            "category_name": "Almohada",
            "category_description": "almohada luuna",
            "category_slug": "almohada"
        },
        {
            "category_id": 2,
            "category_sku": "CO1001",
            "category_name": "Colchon",
            "category_description": "colchon luuna",
            "category_slug": "colchon"
        },
        {
            "category_id": 3,
            "category_sku": "SA1001",
            "category_name": "Sabana",
            "category_description": "sabana luuna",
            "category_slug": "sabana"
        }
    ]
}
```

### Products
* URL: category/slug for category/
* Authentication: None
* Type: GET
* example: category/almohada/
**Request:**

```
Content-Type: application/json
```

**Response:**

**Case 1:** Slug doesn't exists

```
status code: 400 BAD REQUEST
{
    "error": {
        "code": "ufp_004",
        "message": "The slug `slug-value` does not exists. "
    }
}
```

**Case 2:** Slug found, category is disabled

```
{
    "error": {
        "code": "cd_001",
        "message": "The catalog for `<category>` has been disabled"
    }
}
```

**Case 3:** Success

```
status code: 200 OK
{
    "sub_category": [
        {
            "sub_category": "almohada",
            "products": [
                {
                    "size": "regular",
                    "height": 10,
                    "width": 20,
                    "length": 50,
                    "weight": 2.8,
                    "name": "Almohada Regular",
                    "product_parent": {
                        "slug": "almohada-regular",
                        "name": "Almohada Regular",
                        "description": "regular sized pillow",
                        "product_parent_id": 1
                    },
                    "cross_sell": [
                        {
                            "product_child_id": 20,
                            "product_parent_id": 1,
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
                            "cross_sell_price": "1000",
                            "sequence": 1,
                            "images": []
                        } ...
                    ],
                    "product_children": [
                        {
                            "product_child_id": 1,
                            "product_parent_id": 1,
                            "color": "default",
                            "price": 100,
                            "special_price": null,
                            "slug": "almohada-regular-default",
                            "sku": "AL3001",
                            "description": "regular sized pillow",
                            "size": "regular",
                            "height": 10,
                            "width": 20,
                            "length": 50,
                            "weight": 2.8,
                            "name": "Almohada Regular",
                            "images": []
                        }
                    ],
                    "bundles": [
                        {
                            "bundle_id": 1,
                            "bundle_name": "best pack",
                            "bundle_price": 10500,
                            "bundle_description": "this is the best pack you can get"
                        }
                    ]
                },
                {
                    "size": "king",
                    "height": 10,
                    "width": 20,
                    "length": 80,
                    "weight": 3.5,
                    "name": "Almohada King",
                    "product_parent": {
                        "slug": "almohada-king",
                        "name": "Almohada King",
                        "description": "king sized pillow",
                        "product_parent_id": 2
                    },
                    "cross_sell": [
                        {
                            "product_child_id": 25,
                            "product_parent_id": 1,
                            "color": "blue",
                            "price": 500,
                            "special_price": null,
                            "slug": "funda-almohada",
                            "sku": "FA3001",
                            "description": "funda almohada blue",
                            "size": "regular",
                            "height": 1,
                            "width": 1,
                            "length": 1,
                            "weight": 1,
                            "name": "Funda Almohada Estandar",
                            "cross_sell_price": "300",
                            "sequence": 1,
                            "images": []
                        }
                    ],
                    "product_children": [
                        {
                            "product_child_id": 2,
                            "product_parent_id": 1,
                            "color": "default",
                            "price": 1100,
                            "special_price": 1000,
                            "slug": "almohada-king-default",
                            "sku": "AL3002",
                            "description": "king sized pillow",
                            "size": "king",
                            "height": 10,
                            "width": 20,
                            "length": 80,
                            "weight": 3.5,
                            "name": "Almohada King",
                            "images": []
                        }
                    ],
                    "bundles": []
                }
            ]
        }
    ],
    "category": {
        "category_id": 1,
        "category_slug": "almohada",
        "category_name": "Almohada",
        "category_description": "almohada luuna"
    }
}
```
