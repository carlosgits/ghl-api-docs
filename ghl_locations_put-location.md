# Put Sub-Account (Formerly Location)

Source: https://marketplace.gohighlevel.com/docs/ghl/locations/put-location

Screenshot: C:\Users\carlo\OneDrive\Desktop\Proyectos\ghl-api-docs\images\ghl_locations_put-location_screenshot.png

---

Sub-Account (Formerly location)Sub-Account (Formerly Location)Put Sub-Account (Formerly Location)
Put Sub-Account (Formerly Location)
PUT
 https://services.leadconnectorhq.com/locations/:locationId
Update a Sub-Account (Formerly Location) based on the data provided
Requirements
Scope(s)
locations.write
Auth Method(s)
OAuth Access Token
Private Integration Token
Token Type(s)
Agency Token
Request
HEADER PARAMETERS
Version
string
REQUIRED
Possible values: [2021-07-28]
API Version
PATH PARAMETERS
locationId
string
REQUIRED
Location Id
Example: ve9EPM428h8vShlRW1KT
APPLICATION/JSON
BODY
REQUIRED
name
string
The name for the sub-account/location
Example:Mark Shoes
phone
string
The phone number of the business for which sub-account is created
Example:+1410039940
companyId
string
REQUIRED
Company/Agency Id
Example:UAXssdawIWAWD
address
string
The address of the business for which sub-account is created
Example:4th fleet street
city
string
The city where the business is located for which sub-account is created
Example:New York
state
string
The state in which the business operates for which sub-account is created
Example:Illinois
country
string
The country in which the business is present for which sub-account is created
Possible values: [AF, AX, AL, DZ, AS, AD, AO, AI, AQ, AG, AR, AM, AW, AU, AT, AZ, BS, BH, BD, BB, BY, BE, BZ, BJ, BM, BT, BO, BA, BW, BV, BR, IO, BN, BG, BF, BI, KH, CM, CA, CV, KY, CF, TD, CL, CN, CX, CC, CO, KM, CG, CD, CK, CR, CI, HR, CU, CY, CZ, DK, DJ, DM, DO, EC, EG, SV, GQ, ER, EE, ET, FK, FO, FJ, FI, FR, GF, PF, TF, GA, GM, GE, DE, GH, GI, GR, GL, GD, GP, GU, GT, GG, GN, GW, GY, HT, HM, VA, HN, HK, HU, IS, IN, ID, IR, IQ, IE, IM, IL, IT, JM, JP, JE, JO, KZ, KE, KI, KP, KR, XK, KW, KG, LA, LV, LB, LS, LR, LY, LI, LT, LU, MO, MK, MG, MW, MY, MV, ML, MT, MH, MQ, MR, MU, YT, MX, FM, MD, MC, MN, ME, MS, MA, MZ, MM, NA, NR, NP, NL, AN, NC, NZ, NI, NE, NG, NU, NF, MP, NO, OM, PK, PW, PS, PA, PG, PY, PE, PH, PN, PL, PT, PR, QA, RE, RO, RU, RW, SH, KN, LC, MF, PM, VC, WS, SM, ST, SA, SN, RS, SC, SL, SG, SX, SK, SI, SB, SO, ZA, GS, ES, LK, SD, SR, SJ, SZ, SE, CH, SY, TW, TJ, TZ, TH, TL, TG, TK, TO, TT, TN, TR, TM, TC, TV, UG, GB, UA, AE, US, UM, UY, UZ, VU, VE, VN, VG, VI, WF, EH, YE, ZM, ZW]
Example:US
postalCode
string
The postal code of the business for which sub-account is created
Example:567654
website
string
The website of the business for which sub-account is created
Example:https://yourwebsite.com
timezone
string
The timezone of the business for which sub-account is created
Example:US/Central
prospectInfo
object
settings
object
social
object
twilio
object
DEPRECATED
mailgun
object
snapshot
object
Responses
200
400
401
Successful update response
APPLICATION/JSON
Schema
Example (auto)
SCHEMA
id
string
Location Id
Example:ve9EPM428h8vShlRW1KT
companyId
string
Company/Agency Id
Example:UAXssdawIWAWD
name
string
The name for the sub-account/location
Example:Mark Shoes
phone
string
The phone number of the business for which sub-account is created
Example:+1410039940
email
string
The email for the sub-account/location
Example:john.doe@mail.com
address
string
The address of the business for which sub-account is created
Example:4th fleet street
city
string
The city where the business is located for which sub-account is created
Example:New York
state
string
The state in which the business operates for which sub-account is created
Example:Illinois
domain
string
Example:test.msgsndr.com
country
string
The country in which the business is present for which sub-account is created
Possible values: [AF, AX, AL, DZ, AS, AD, AO, AI, AQ, AG, AR, AM, AW, AU, AT, AZ, BS, BH, BD, BB, BY, BE, BZ, BJ, BM, BT, BO, BA, BW, BV, BR, IO, BN, BG, BF, BI, KH, CM, CA, CV, KY, CF, TD, CL, CN, CX, CC, CO, KM, CG, CD, CK, CR, CI, HR, CU, CY, CZ, DK, DJ, DM, DO, EC, EG, SV, GQ, ER, EE, ET, FK, FO, FJ, FI, FR, GF, PF, TF, GA, GM, GE, DE, GH, GI, GR, GL, GD, GP, GU, GT, GG, GN, GW, GY, HT, HM, VA, HN, HK, HU, IS, IN, ID, IR, IQ, IE, IM, IL, IT, JM, JP, JE, JO, KZ, KE, KI, KP, KR, XK, KW, KG, LA, LV, LB, LS, LR, LY, LI, LT, LU, MO, MK, MG, MW, MY, MV, ML, MT, MH, MQ, MR, MU, YT, MX, FM, MD, MC, MN, ME, MS, MA, MZ, MM, NA, NR, NP, NL, AN, NC, NZ, NI, NE, NG, NU, NF, MP, NO, OM, PK, PW, PS, PA, PG, PY, PE, PH, PN, PL, PT, PR, QA, RE, RO, RU, RW, SH, KN, LC, MF, PM, VC, WS, SM, ST, SA, SN, RS, SC, SL, SG, SX, SK, SI, SB, SO, ZA, GS, ES, LK, SD, SR, SJ, SZ, SE, CH, SY, TW, TJ, TZ, TH, TL, TG, TK, TO, TT, TN, TR, TM, TC, TV, UG, GB, UA, AE, US, UM, UY, UZ, VU, VE, VN, VG, VI, WF, EH, YE, ZM, ZW]
Example:US
postalCode
string
The postal code of the business for which sub-account is created
Example:567654
website
string
The website of the business for which sub-account is created
Example:https://yourwebsite.com
timezone
string
The timezone of the business for which sub-account is created
Example:US/Central
settings
object
social
object











































Share your feedback
★
★
★
★
★
AUTHORIZATION: AUTHORIZATION
CURL
NODEJS
PYTHON
PHP
JAVA
GO
RUBY
POWERSHELL
CURL
curl -L -X PUT 'https://services.leadconnectorhq.com/locations/:locationId' \
-H 'Content-Type: application/json' \
-H 'Accept: application/json' \
-H 'Authorization: Bearer <TOKEN>' \
--data-raw '{
  "name": "Mark Shoes",
  "phone": "+1410039940",
  "companyId": "UAXssdawIWAWD",
  "address": "4th fleet street",
  "city": "New York",
  "state": "Illinois",
  "country": "US",
  "postalCode": "567654",
  "website": "https://yourwebsite.com",
  "timezone": "US/Central",
  "prospectInfo": {
    "firstName": "John",
    "lastName": "Doe",
    "email": "john.doe@mail.com"
  },
  "settings": {
    "allowDuplicateContact": false,
    "allowDuplicateOpportunity": false,
    "allowFacebookNameMerge": false,
    "disableContactTimezone": false
  },
  "social": {
    "facebookUrl": "https://www.facebook.com/",
    "googlePlus": "https://www.googleplus.com/",
    "linkedIn": "https://www.linkedIn.com/",
    "foursquare": "https://www.foursquare.com/",
    "twitter": "https://www.foutwitterrsquare.com/",
    "yelp": "https://www.yelp.com/",
    "instagram": "https://www.instagram.com/",
    "youtube": "https://www.youtube.com/",
    "pinterest": "https://www.pinterest.com/",
    "blogRss": "https://www.blogRss.com/",
    "googlePlacesId": "ChIJJGPdVbQTrjsRGUkefteUeFk"
  },
  "mailgun": {
    "apiKey": "key-XXXXXXXXXXX",
    "domain": "replies.yourdomain.com"
  },
  "snapshot": {
    "id": "XXXXXXXXXXX",
    "override": false
  }
}'
REQUEST
COLLAPSE ALL
Base URL
https://services.leadconnectorhq.com
Auth
Bearer Token
Parameters
locationId — path
REQUIRED
Version — header
REQUIRED
---
2021-07-28
Body
 REQUIRED
{
  "name": "Mark Shoes",
  "phone": "+1410039940",
  "companyId": "UAXssdawIWAWD",
  "address": "4th fleet street",
  "city": "New York",
  "state": "Illinois",
  "country": "US",
  "postalCode": "567654",
  "website": "https://yourwebsite.com",
  "timezone": "US/Central",
  "prospectInfo": {
    "firstName": "John",
    "lastName": "Doe",
    "email": "john.doe@mail.com"
  },
  "settings": {
    "allowDuplicateContact": false,
    "allowDuplicateOpportunity": false,
    "allowFacebookNameMerge": false,
    "disableContactTimezone": false
  },
  "social": {
    "facebookUrl": "https://www.facebook.com/",
    "googlePlus": "https://www.googleplus.com/",
    "linkedIn": "https://www.linkedIn.com/",
    "foursquare": "https://www.foursquare.com/",
    "twitter": "https://www.foutwitterrsquare.com/",
    "yelp": "https://www.yelp.com/",
    "instagram": "https://www.instagram.com/",
    "youtube": "https://www.youtube.com/",
    "pinterest": "https://www.pinterest.com/",
    "blogRss": "https://www.blogRss.com/",
    "googlePlacesId": "ChIJJGPdVbQTrjsRGUkefteUeFk"
  },
  "mailgun": {
    "apiKey": "key-XXXXXXXXXXX",
    "domain": "replies.yourdomain.com"
  },
  "snapshot": {
    "id": "XXXXXXXXXXX",
    "override": false
  }
}
SEND API REQUEST
RESPONSE
CLEAR
Click the Send API Request button above and see the response here!