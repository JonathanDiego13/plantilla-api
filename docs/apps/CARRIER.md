# Carriers

**Return available carriers for current cart**

```
Return available/general time slot(s) depending on your cart/postcode.
To edit/add a datetime slot, user cart api
```

* URL: carrier/v1/


## Suggest a carrier
* URL: suggest/
* Authentication: Token Based
* Type: GET

**Request**

```
Content-Type: application/json
token: "eyJ0eXAiOiJK.OTk0ODk0MDAsImVtYWlsIjoi.2T8Pfy28yoF_nXvw"
```

**Response**

**case 1:** Success

```
status code: 200 OK
{
    "carrier": {
        "provider": "on_fleet",  # on_fleet, fedex, 99_minutos
        "delivery_type": "date_time_slots",  # undetermined, date_slots, date_time_slots
        "detail": "same day delivery"
    }
}
```


## Get a list of available slots, given a carrier and a date
* URL: date/< carrier >/?date=< javascript datetime >
* Authentication: Token Based
* Type: GET

**Request**

```
Content-Type: application/json
token: "eyJ0eXAiOiJK.OTk0ODk0MDAsImVtYWlsIjoi.2T8Pfy28yoF_nXvw"
```

**Response**

**case 1:** Success

```
status code: 200 OK
{
    "slots": {
        morning: [{
                "slot": 1,
                "from": 8,
                "till": 10
            }, {
                "slot": 2,
                "from": 10,
                "till": 12
        } ...],
        evening: [{
                "slot": 1,
                "from": 8,
                "till": 10
            }, {
                "slot": 2,
                "from": 10,
                "till": 12
        } ...]
    }
}
```
