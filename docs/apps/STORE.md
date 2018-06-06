# Stores

**Return available stores for sell products Luuna**

```
Return available/general store(s).
To edit/add a store use admin
```

* URL: store/v1/


## Get all stores for state
* URL: [host]/user/v1/
* Authentication: Allow any
* Type: GET

**Request**

```
Allow: GET, OPTIONS
Content-Type: application/json
```

**Response**

**case 1:** Success

```
{
    "stores": [
        {
            "name": "Liverpool",
            "phone_number": "5262-9999",
            "address": "AV. Central, Colonia centro",
            "state": "Aguascalientes",
            "latitude": 19.4339455,
            "longitude": -99.1689133,
            "opening_hours": "Lunes a Domingo de 11:00 am a 09:00pm",
            "url_image": "https://www.liverpool.com.mx/tienda/home.jsp"
        },
        {
            "name": "Liverpool Polanco",
            "phone_number": "5262-9999",
            "address": "Polanco, Calle #13",
            "state": "Ciudad de México",
            "latitude": 19.4339455,
            "longitude": -99.1689133,
            "opening_hours": "Lunes a Domingo de 11:00 am a 09:00pm",
            "url_image": "https://www.liverpool.com.mx/tienda/home.jsp"
        },
        {
            "name": "Liverpool Reforma",
            "phone_number": "5262-9999",
            "address": "Av.Reforma #32, Delegación Cuahutemoc",
            "state": "Ciudad de México",
            "latitude": 19.4339455,
            "longitude": -19.4339455,
            "opening_hours": "Lunes a Domingo de 11:00 am a 09:00pm",
            "url_image": "https://www.liverpool.com.mx/tienda/home.jsp"
        },
        {
            "name": "Liverpool Cuernavaca",
            "phone_number": "01 777 100 7400",
            "address": "Mexico-Acapulco Km 87.5, Tulipanes, 62370 Cuernavaca.",
            "state": "Morelos",
            "latitude": 18.9365588,
            "longitude": -99.1922083,
            "opening_hours": "Lunes a Domingo de 11:00 am a 09:00pm",
            "url_image": "https://www.liverpool.com.mx/tienda/home.jsp"
        },
        {
            "name": "Liverpool Galerias",
            "phone_number": "5262-9999",
            "address": "Cuernavaca, Morelos. Av. Morelos",
            "state": "Morelos",
            "latitude": 19.4327776,
            "longitude": -99.17409,
            "opening_hours": "Lunes a Domingo de 11:00 am a 09:00pm",
            "url_image": "https://www.liverpool.com.mx/tienda/browse/store.jsp"
        },
        {
            "name": "Liverpool Sports",
            "phone_number": "5262-9999",
            "address": "Cuernavaca centro",
            "state": "Morelos",
            "latitude": 19.4327776,
            "longitude": -99.17409,
            "opening_hours": "Lunes a Domingo de 11:00 am a 09:00pm",
            "url_image": "https://www.liverpool.com.mx/tienda/browse/store.jsp"
        },
        {
            "name": "Liverpool",
            "phone_number": "5262-9999",
            "address": "Monterrey Centro",
            "state": "Nuevo León",
            "latitude": 19.4327776,
            "longitude": -99.17409,
            "opening_hours": "Lunes a Domingo de 11:00 am a 09:00pm",
            "url_image": "https://www.liverpool.com.mx/tienda/browse/store.jsp"
        }
    ]
}
```