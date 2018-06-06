# Account
* base url: [host]/user/v1/

## Registration
* URL: register/
* Authentication: Allow Any
* Type: POST

**Request:**

```
Content-Type: application/json
{
    "email": "rohit.rawat@luuna.mx",
    "password": "undesirably complicated password",  # optional
    "first_name": "rohit",
    "last_name": "rawat",  # optional
    "phone_number": "5512345678",
    "additional_number": "+521 5512345678",  # optional
}
```

**Response:**

### Success Response (all but logout)
```
The request has been successfully processed

status code: 201 CREATED
content:
{
    "user": {
        "first_name": "jose",
        "last_name": "sanchez",
        "email": "jose@luuna.mx",
        "phone_number": "5512345678",
        "additional_number": "+521 5512345678",
        "date_joined": "2017-07-06"
    },
    "token": "eyJ0eXAiOiJK.OTk0ODk0MDAsImVtYWlsIjoi.2T8Pfy28yoF_nXvw",
    "included": {
        "cart_id": <int> or null
    }
}
```

### Account Disabled Response
```
status code: 403 PERMISSION DENIED
{
    "error": {
        "code": "ul_002",
        "message": "Your account has been disabled. Please contact customer service to activate it"
    }
}
```

### Invalid new or existing Password
```
status code: 422 UNPROCESSABLE ENTITY
content:
{
    "error": {
        "code": "ur_003",
        "message": "Message describing why the password is invalid"
    }
}
```

**case 1:** Incomplete request
```
Some required parameter is missing

status code: 400 Bad Request
content:
{
    "error": {
        "code": "ur_001",
        "message": "Required parameter <parameter> is missing"
    }
}
```

**case 2:** Incorrect data
```
Email/Password etc are incorrectly formatted or does not meet the standard (char field)

status code: 422 UNPROCESSABLE ENTITY
content:
{
    "error": {
        "code": "ur_002",
        "message": "Email or password is incorrect"
    }
}
```

**case 3:** Email already exists
```
Email address is already registered

status code: 409 CONFLICT
content:
{
    "error": {
        "code": "ur_002",
        "message": "The email has already been registered. Please login"
    }
}
```

**case 4:** Missing/Blank required parameter
```
status code: 400 BAD REQUEST
content:
{
    "error": {
        "code": "ur_001",
        "message": "Validation Error",
        "fields": [
            "email"
        ],
        "details": {
            "email": [
                "This field is required."
            ]
        }
    }
}
```


## Login
* URL: login/
* Authentication: Allow Any
* Type: POST

**Request:**

```
Content-Type: application/json
{
    "email": "rohit.rawat@luuna.mx",
    "password": "undesirably complicated password",
}
```

**Response:**

**case 1:** Missing/Blank/Invalid Parameter (email/password) -> same as register

**case 2:** Incorrect Email/Password
```
status code: 401 UNAUTHORIZED
content:
{
    "error": {
        "code": "ul_001",
        "message": "Email or password not found"
    }
}
```


## Logout
* URL: logout/
* Authentication: Allow any
* Type: GET

**Request:**

```
Content-Type: application/json
token: "eyJ0eXAiOiJK.OTk0ODk0MDAsImVtYWlsIjoi.2T8Pfy28yoF_nXvw"
```

**Response:** Irrespective of the request, the response is always going to be 204 NO CONTENT


## Profile View
* URL: profile/
* Authentication: Token Based
* Type:
    * GET - Get user's profile
    * PUT - Update user's profile

### GET

**Request:**

```
Content-Type: application/json
token: "eyJ0eXAiOiJK.OTk0ODk0MDAsImVtYWlsIjoi.2T8Pfy28yoF_nXvw"
```

### PUT

**Request:**

```
Content-Type: application/json
token: "eyJ0eXAiOiJK.OTk0ODk0MDAsImVtYWlsIjoi.2T8Pfy28yoF_nXvw"
{
    "new_first_name": "juan",
    "new_last_name": "mondragon"
}
```

**Response:**

**case 1: (get and put)** Token Not included / Invalid token (not found)
```
status code: 401 UNAUTHORIZED
content:
{
    "detail": "Authentication credentials were not provided."
}
```

**case 2: (put only)** No parameter provided
```
status code: 400 Bad Request
content:
{
    "error": {
        "code": "ur_001",
        "message": "All of the required parameters are missing."
    }
}
```

**case 3: (put only)** Empty parameter -> same as register (400)


## Change Password
* URL: change-password/
* Authentication: Token Based
* Type: PUT

**Request:**

```
Content-Type: application/json
token: "eyJ0eXAiOiJK.OTk0ODk0MDAsImVtYWlsIjoi.2T8Pfy28yoF_nXvw"
{
    "password": "original password",
    "new_password": "new password",
}
```

**Response:**

**case 1:** Token Not included / Invalid token / Inexistent token / Expired token
```
status code: 422 UNPROCESSABLE ENTITY
content:
{
    "error": "Token is incorrect or has expired! Please try again!"
}
```

**case 2:** Missing password or new password
```
status code: 400 BAD REQUEST
content:
{
    "error": {
        "code": "ur_001",
        "message": "Required parameter `new_password/password` is missing"
    }
}
```


## Forgot Password
* URL: forgot-password/
* Authentication: None
* Type:
    * POST: Confirm email is registered and generate a temporary token. Send token to user via email
    * PUT: confirm token & new password. Change password, send email, auto-login.

### POST

**Request:**

```
Content-Type: application/json
content:
{
    "email": "jose.sanchez@luuna.mx"
}
```

**Response:**

**case 1:** Email is wrong (impossible value for email)
```
status code: 400 BAD REQUEST
content:
{
    "error": {
        "code": "ufp_004",
        "message": "Parameter `email` is incorrect. Please enter correct value"
    },
}
```

**case 2:** Email missing -> same as register (400)

**case 3:** User inactive
```
status code: 403 PERMISSION DENIED
content:
{
    "error": {
        "code": "ul_002",
        "message": "Your account has been disabled. Please contact customer service to activate it"
    }
}
```

**case 4:** User not found / Success
```
status code: 204 NO CONTENT
content: {}
```

### PUT

**Request:**

```
Content-Type: application/json
{
    "token": "eyJ0eXAiOiJK"
    "new_password": "new password"
}
```

**Response:**

**case 1:** Missing new password/token -> same as register (400)


## Verify Token Exists
* URL: verify-token/
* Authentication: Token based
* Type: GET

**Request:**

```
Content-Type: application/json
token: "eyJ0eXAiOiJK.OTk0ODk0MDAsImVtYWlsIjoi.2T8Pfy28yoF_nXvw"
```

**Response:**

**case 1:** Missing/Invalid/Inexistent token
```
status code: 401 UNAUTHORIZED
{
    "detail": "Authentication credentials were not provided."
}
```

**case 2:** Success
```
status code: 200 OK
{
    "success": true
}
```

## Address
* Url: address/
* Authentication: Token based
* Type:
    * POST: Create
    * GET: Fetch
    * PUT: Edit
    * Delete: Remove

### Add a new address: POST

**Request:**

```
Content-Type: application/json
token: "eyJ0eXAiOiJK.OTk0ODk0MDAsImVtYWlsIjoi.2T8Pfy28yoF_nXvw"
{
    "n_int": 10,  # optional
    "n_ext": 77,
    "street": "Niza",
    "colony": "juarez",
    "city": "cuauhtemoc",
    "state": "mexico city",
    "postal_code": "06600",
    "latitude": "19.434675",
    "longitude": "-99.168418",
    "phone_number": "5555555555",  # optional
    "additional_number": "+91 9818949188", # optional
    "additional_information": "we do not fraud!"  # optional
}
```

**Response:**

**case 1:** Missing required parameter(s) -> same as register

**case 2:** Success
```
status: 201 CREATED  # POST
{
    "id": 1,
    "n_int": 10,
    "n_ext": 77,
    "street": "Niza",
    "colony": "juarez",
    "city": "cuauhtemoc",
    "state": "mexico city",
    "postal_code": "06600",
    "latitude": "19.434675",
    "longitude": "-99.168418",
    "phone_number": "5555555555",
    "additional_information": "we do not fraud!"
}
```

### Edit an address: PUT

**Request:**

```
Content-Type: application/json
token: "eyJ0eXAiOiJK.OTk0ODk0MDAsImVtYWlsIjoi.2T8Pfy28yoF_nXvw"
{
    "id": "1",
    ... # same as post
}
```

**Response:**

**case 1:** Missing Required Field(s) -> same as register (400)

**case 2:** token/address id doesn't belong to the same user (mismatch)
```
status: 404 NOT FOUND
{
    "error": {
        "code": "uae_001",
        "message": "Address not found"
    }
}
```

**case 3:** Success
```
status: 200 OK
{
    ... # same as post
}
```

### Get all associated addresses: GET

**Request:**

```
Content-Type: application/json
token: "eyJ0eXAiOiJK.OTk0ODk0MDAsImVtYWlsIjoi.2T8Pfy28yoF_nXvw"
```

**Response:** Success
```
{
    "addresses": [{
        ...  # similar to post
    }, {
        ...  # similar to post
    }]
}
```

### Delete an address: DELETE

**Request:**

```
Content-Type: application/json
token: "eyJ0eXAiOiJK.OTk0ODk0MDAsImVtYWlsIjoi.2T8Pfy28yoF_nXvw"
{
    "id": 1
}
```

**Response:**

**case 1:** Missing id or mismatched token/id

```
status: 404 Not Found
{
    "error": {
        "code": "uae_001",
        "message": "Address not found"
    }
}
```

**case 2:** Success -> No content


## Postal code
* Url: postal_code/[0-9]{5}/
* Authentication: Allow Any
* Type:
    * GET: Get a state, a city and a list of colonies

**Response:**

**case 1:** Missing required parameter
```
status code: 404 NOT FOUND
```

**case 2:** Postal code does not exist (e.g. 00000)
```
status code:  422 UNPROCESSABLE ENTITY
{
    "error": {
        "code": "ur_003",
        "message": "postcode not found"
    }
}
```

**case 3:** Success - 1 colony
```
status code: 200 OK
{
    "state": "México",
    "city": "Nezahualcóyotl",
    "colonies": [
        "General José Vicente Villada"
    ]
}
```

**case 4:** Success - Multiple colonies
```
status code: 200 OK
{
    "state": "México",
    "city": "Valle de Chalco Solidaridad",
    "colonies": [
        "Concepción",
        "María Isabel",
        "Santiago",
        "El Agostadero"
    ]
}
```
