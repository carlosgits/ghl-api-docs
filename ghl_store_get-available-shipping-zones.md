# Get available shipping rates

Source: https://marketplace.gohighlevel.com/docs/ghl/store/get-available-shipping-zones

Screenshot: images/ghl_store_get-available-shipping-zones_screenshot.png

---

StoreShipping ZoneGet available shipping rates
Get available shipping rates
POST
 https://services.leadconnectorhq.com/store/shipping-zone/shipping-rates
This return available shipping rates for country based on order amount
Request
APPLICATION/JSON
BODY
REQUIRED
altId
string
REQUIRED
Location Id or Agency Id
Example:6578278e879ad2646715ba9c
altType
string
REQUIRED
Possible values: [location]
country
string
REQUIRED
Country code of the customer
Possible values: [US, CA, AF, AX, AL, DZ, AS, AD, AO, AI, AQ, AG, AR, AM, AW, AU, AT, AZ, BS, BH, BD, BB, BY, BE, BZ, BJ, BM, BT, BO, BA, BW, BV, BR, IO, BN, BG, BF, BI, KH, CM, CV, KY, CF, TD, CL, CN, CX, CC, CO, KM, CG, CD, CK, CR, CI, HR, CU, CY, CZ, DK, DJ, DM, DO, EC, EG, SV, GQ, ER, EE, ET, FK, FO, FJ, FI, FR, GF, PF, TF, GA, GM, GE, DE, GH, GI, GR, GL, GD, GP, GU, GT, GG, GN, GW, GY, HT, HM, VA, HN, HK, HU, IS, IN, ID, IR, IQ, IE, IM, IL, IT, JM, JP, JE, JO, KZ, KE, KI, KP, XK, KW, KG, LA, LV, LB, LS, LR, LY, LI, LT, LU, MO, MK, MG, MW, MY, MV, ML, MT, MH, MQ, MR, MU, YT, MX, FM, MD, MC, MN, ME, MS, MA, MZ, MM, NA, NR, NP, NL, AN, NC, NZ, NI, NE, NG, NU, NF, MP, NO, OM, PK, PW, PS, PA, PG, PY, PE, PH, PN, PL, PT, PR, QA, RE, RO, RU, RW, SH, KN, LC, MF, PM, VC, WS, SM, ST, SA, SN, RS, SC, SL, SG, SX, SK, SI, SB, SO, ZA, GS, KR, ES, LK, SD, SR, SJ, SZ, SE, CH, SY, TW, TJ, TZ, TH, TL, TG, TK, TO, TT, TN, TR, TM, TC, TV, UG, UA, AE, GB, UM, UY, UZ, VU, VE, VN, VG, VI, WF, EH, YE, ZM, ZW]
Example:US
address
object
amountAvailable
string
it will not calculate the order amount form backend if it is true
Possible values: [AF, AX, AL, DZ, AS, AD, AO, AI, AQ, AG, AR, AM, AW, AU, AT, AZ, BS, BH, BD, BB, BY, BE, BZ, BJ, BM, BT, BO, BA, BW, BV, BR, IO, BN, BG, BF, BI, KH, CM, CA, CV, KY, CF, TD, CL, CN, CX, CC, CO, KM, CG, CD, CK, CR, CI, HR, CU, CY, CZ, DK, DJ, DM, DO, EC, EG, SV, GQ, ER, EE, ET, FK, FO, FJ, FI, FR, GF, PF, TF, GA, GM, GE, DE, GH, GI, GR, GL, GD, GP, GU, GT, GG, GN, GW, GY, HT, HM, VA, HN, HK, HU, IS, IN, ID, IR, IQ, IE, IM, IL, IT, JM, JP, JE, JO, KZ, KE, KI, KP, KR, XK, KW, KG, LA, LV, LB, LS, LR, LY, LI, LT, LU, MO, MK, MG, MW, MY, MV, ML, MT, MH, MQ, MR, MU, YT, MX, FM, MD, MC, MN, ME, MS, MA, MZ, MM, NA, NR, NP, NL, AN, NC, NZ, NI, NE, NG, NU, NF, MP, NO, OM, PK, PW, PS, PA, PG, PY, PE, PH, PN, PL, PT, PR, QA, RE, RO, RU, RW, SH, KN, LC, MF, PM, VC, WS, SM, ST, SA, SN, RS, SC, SL, SG, SX, SK, SI, SB, SO, ZA, GS, ES, LK, SD, SR, SJ, SZ, SE, CH, SY, TW, TJ, TZ, TH, TL, TG, TK, TO, TT, TN, TR, TM, TC, TV, UG, GB, UA, AE, US, UM, UY, UZ, VU, VE, VN, VG, VI, WF, EH, YE, ZM, ZW]
Example:US
totalOrderAmount
number
REQUIRED
The amount of the price. ( min: 0.01 )
Example:99.99
weightAvailable
boolean
Flag to pass when the weight is already calculated and should not calculate again
Example:true
totalOrderWeight
number
REQUIRED
Estimated weight of the order calculated from the order creation side in kg(s)
Example:10
source
object
products
object[]
REQUIRED
couponCode
string
Coupon code
Example:TEST
Responses
201
400
401
422
Successful response
APPLICATION/JSON
Schema
Example (auto)
SCHEMA
status
boolean
REQUIRED
Status of api action
Example:true
message
string
Success message
Example:Successfully created
data
object[]
REQUIRED







































Share your feedback
★
★
★
★
★
CURL
NODEJS
PYTHON
PHP
JAVA
GO
RUBY
POWERSHELL
CURL
curl -L 'https://services.leadconnectorhq.com/store/shipping-zone/shipping-rates' \
-H 'Content-Type: application/json' \
-H 'Accept: application/json' \
--data-raw '{
  "altId": "6578278e879ad2646715ba9c",
  "altType": "location",
  "country": "US",
  "address": {
    "name": "John Doe",
    "companyName": "ABC Company",
    "addressLine1": "123 Main St.",
    "country": "US",
    "state": "US",
    "city": "New York",
    "zip": "12345",
    "phone": "1234567890",
    "email": "abu@example.com"
  },
  "amountAvailable": "US",
  "totalOrderAmount": 99.99,
  "weightAvailable": true,
  "totalOrderWeight": 10,
  "source": {
    "type": "order",
    "subType": "store"
  },
  "products": [
    {
      "id": "string",
      "qty": 0
    }
  ],
  "couponCode": "TEST"
}'
REQUEST
COLLAPSE ALL
Base URL
https://services.leadconnectorhq.com
Body
 REQUIRED
{
  "altId": "6578278e879ad2646715ba9c",
  "altType": "location",
  "country": "US",
  "address": {
    "name": "John Doe",
    "companyName": "ABC Company",
    "addressLine1": "123 Main St.",
    "country": "US",
    "state": "US",
    "city": "New York",
    "zip": "12345",
    "phone": "1234567890",
    "email": "abu@example.com"
  },
  "amountAvailable": "US",
  "totalOrderAmount": 99.99,
  "weightAvailable": true,
  "totalOrderWeight": 10,
  "source": {
    "type": "order",
    "subType": "store"
  },
  "products": [
    {
      "id": "string",
      "qty": 0
    }
  ],
  "couponCode": "TEST"
}
SEND API REQUEST
RESPONSE
CLEAR
Click the Send API Request button above and see the response here!