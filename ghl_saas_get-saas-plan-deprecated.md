# Get SaaS Plan

Source: https://marketplace.gohighlevel.com/docs/ghl/saas/get-saas-plan-deprecated

Screenshot: images/ghl_saas_get-saas-plan-deprecated_screenshot.png

---

SaasSaasGet SaaS Plan
Get SaaS Plan
GET
 https://services.leadconnectorhq.com/saas-api/public-api/saas-plan/:planId
DEPRECATED
This endpoint has been deprecated and may be replaced or removed in future versions of the API.
Fetch a specific SaaS plan by plan ID
Requirements
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
Possible values: [2021-04-15]
API Version
PATH PARAMETERS
planId
string
REQUIRED
Plan ID to get SaaS plan details for
Example: 66c4d36534f21f900dc2a265
QUERY PARAMETERS
companyId
string
REQUIRED
Company ID to filter SaaS plan
Example: 5DP4iH6HLkQsiKESj6rh
Responses
200
400
401
404
500
SaaS plan retrieved successfully
APPLICATION/JSON
Schema
Example (auto)
SCHEMA
planId
string
REQUIRED
Unique identifier for the SaaS plan
Example:66c4d36534f21f900dc2a265
companyId
string
REQUIRED
Company ID associated with the SaaS plan
Example:66c4d36534f21f900dc2a265
title
string
REQUIRED
Title of the SaaS plan
Example:AED 1.5 changed
description
string
REQUIRED
Description of the SaaS plan
Example:AED 1.5
saasProducts
string[]
REQUIRED
Array of SaaS products included in the plan
Example:["2-way-text-messaging","gmb-messaging","web-chat"]
addOns
string[]
Array of add-ons included in the plan
Example:["YEXT_V2","WHATSAPP_V1","WORDPRESS_V1","AI_EMPLOYEE","Ad_Publishing_Connect_Your_BM"]
planLevel
number
REQUIRED
Level of the plan (0-4)
Example:0
trialPeriod
number
REQUIRED
Trial period in days
Example:16
setupFee
number
Setup fee for the plan
Example:100
userLimit
number
User limit for the plan
Example:50
contactLimit
number
Contact limit for the plan
Example:50
prices
object[]
REQUIRED
categoryId
string
Category ID for the plan
Example:66911cdc98508ec2731979b9
snapshotId
string
Snapshot ID for the plan
Example:G8KmpIeLnZc7ZMoJoxDx
providerLocationId
string
Provider location ID
Example:r06mdj4OrrERzYDvsOdh
productId
string
Product ID for the plan
Example:66a9edbfcc6c5090bedb7974
isSaaSV2
boolean
REQUIRED
Indicates if this is a SaaS V2 plan
Example:true
createdAt
date-time
REQUIRED
Creation timestamp
Example:2024-07-31T07:54:41.885Z
updatedAt
date-time
REQUIRED
Last update timestamp
Example:2025-04-01T12:27:29.167Z






























































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
curl -L 'https://services.leadconnectorhq.com/saas-api/public-api/saas-plan/:planId' \
-H 'Accept: application/json' \
-H 'Authorization: Bearer <TOKEN>'
REQUEST
COLLAPSE ALL
Base URL
https://services.leadconnectorhq.com
Auth
Bearer Token
Parameters
planId — path
REQUIRED
companyId — query
REQUIRED
Version — header
REQUIRED
---
2021-04-15
SEND API REQUEST
RESPONSE
CLEAR
Click the Send API Request button above and see the response here!