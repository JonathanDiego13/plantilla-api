## [User](USER.md)
* Register: user/v1/register/
  * POST
* Login: user/v1/login/
  * POST
* Logout: user/v1/logout/
  * GET
* Profile: user/v1/profile/
  * GET: view
  * PUT: edit
* Change Password: user/v1/change-password/
  * PUT
* Forgot Password: user/v1/forgot-password/
  * POST: Create token
  * PUT: Change password
* Address: user/v1/address/
  * GET: get all addresses
  * POST: add new address
  * PUT: edit an address
  * DELETE: delete an address
* Postal code: user/v1/postal_code/<5 digit postal code>/
  * GET: Get a state, a municipality and a list of colonies


## [Catalog](CATALOG.md)
* Categories: catalog/v1/categories/
    * GET
* Product: catalog/v1/category/<slug for category>/
    * GET

## [Cart](CART.md)
* For logged in users:
    * cart/v1/user/
    * POST: create
    * PUT: update
    * GET: get
    * DELETE: delete
* For anonymous users
    * cart/v1/anonymous/
    * POST: get cart's data


## [Promotion](PROMOTION.md)
Just notes, no request


## [Carrier](CARRIER.md)
* carrier/v1/
* GET: get


## [Order](ORDER.md)
* order/v1/
* Create:
    POST: create/
* List:
    GET: list/
* Details:
    GET: details/<user_order_id>/

# [Payment](PAYMENT.md)
* Base URL: payment/v1/
* Available payment methods:
    method: POST
    URL: get-available-payment-methods/
