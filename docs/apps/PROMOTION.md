# Promotions

## Cart
## All things cart
* handle bundling
* handle volume based discount
* apply coupon to the final price


### Bundling rules
* 2 products are bundled together
id p1
id p2
min_qty p1
max_qty p1
min_qty p2
max_qty p2
priority

### Coupon/Voucher redemption

**Checkpoints**
* The coupon exists in database
* The coupon is valid for the given skus
* The user is eligible to avail this discount

**Calculate value**
* Percent/Fixed: % < 100
* lesser of max_discount/discount value
* lesser of remaining budget/discount value
* greater than or equal to 0


### bundle discounts

