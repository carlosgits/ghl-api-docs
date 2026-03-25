# Get Subscription by ID

Source: https://marketplace.gohighlevel.com/docs/ghl/payments/get-subscription-by-id

Screenshot: C:\Users\carlo\OneDrive\Desktop\Proyectos\ghl-api-docs\images\ghl_payments_get-subscription-by-id_screenshot.png

---

PaymentsSubscriptionsGet Subscription by ID
Get Subscription by ID
GET
 https://services.leadconnectorhq.com/payments/subscriptions/:subscriptionId
The "Get Subscription by ID" API allows to retrieve information for a specific subscription using its unique identifier. Use this endpoint to fetch details for a single subscription based on the provided subscription ID.
Requirements
Scope(s)
payments/subscriptions.readonly
Auth Method(s)
OAuth Access Token
Private Integration Token
Token Type(s)
Sub-Account Token
Request
HEADER PARAMETERS
Version
string
REQUIRED
Possible values: [2021-07-28]
API Version
PATH PARAMETERS
subscriptionId
string
REQUIRED
ID of the subscription that needs to be returned
Example: 6322e9c9e39fc14ab3ed7042
QUERY PARAMETERS
altId
string
REQUIRED
AltId is the unique identifier e.g: location id.
Example: 3SwdhCu3svxI8AKsPJt6
altType
string
REQUIRED
Possible values: [location]
AltType is the type of identifier.
Example: location
Responses
200
400
401
422
Successful response
APPLICATION/JSON
Schema
Example (auto)
SCHEMA
_id
string
REQUIRED
The unique identifier for the subscription.
Example:64bf78af39118e4011926cba
altType
object
REQUIRED
AltType is the type of identifier.
Example:location
altId
string
REQUIRED
AltId is the unique identifier eg: location id.
Example:3SwdhCu3svxI8AKsPJt6
contactId
string
Contact id corresponding to the subscription.
Example:XPLSw2SVagl12LMDeTmQ
contactSnapshot
object
Contact details of the subscriber.
Example:{ last_name: "Mcclain", type: "lead", first_name_lower_case: "rogan", email: "anish+11@gohighlevel.com", last_name_lower_case: "mcclain", location_id: "o6241QsiRwUIJHyjuhos", company_name: "Jordan and Cox Trading"}
coupon
object
Coupon details of the subscription.
Example:{ _id: "6374c6926d119a393fe1e556", usageCount: 5260, altId: "jVFIxsMY19D94nOSIOEO", altType: "location", name: "FREE-100%", code: "FREE100", discountType: "percentage", discountValue: 100 }
currency
string
Currency in which subscription was made.
Example:USD
amount
number
Subscription value.
Example:100
status
object
Subscription status.
Example:active
liveMode
boolean
Subscription is in live / test mode.
Example:false
entityType
string
Entity type of subscription (eg: order).
Example:order
entityId
string
Entity id for the subscription. e.g: order id
Example:62f4db0f3059ecee61379012
entitySource
object
subscriptionId
string
Subscription id for subscription.
Example:I-0UE609H8E43P
subscriptionSnapshot
object
Snapshot of subscription.
Example:{ status: "ACTIVE", status_update_time: "2022-08-16T11:06:53Z", id: "I-0UE609H8E43P", plan_id: "P-82K11750F0313430KMLRGE6Y", start_time: "2022-08-16T11:05:31Z", quantity: 1 }
paymentProvider
object
Payment provider details for the subscription.
Example:{ type: "paypal", connectedAccount: { _id: "64410debdc8f3b0503523abb", merchantClientId: "AeXtjrxdgsJiCPwQt5jML5pH-0mwmLs-tH7ub4Uo3IrDKvRl34FvJy8niI6E1wmS_pryIRdNllyVl58b" } }
ipAddress
string
Ip address from where subscription was initiated.
Example:103.100.16.82
createdAt
date-time
REQUIRED
The creation timestamp of the subscription.
Example:2023-11-20T10:23:36.515Z
updatedAt
date-time
REQUIRED
The last update timestamp of the subscription.
Example:2024-01-23T09:57:04.846Z
meta
object
Meta details of the subscription.
Example:{ collection: "transactionsv2", id: "6320652f0f664b6632006920" }
markAsTest
boolean
Is test subscription.
Example:false
schedule
object
autoPayment
object
Auto payment details of the subscription.
Example:{ customerId: "908879612", paymentMethodId: "908646635" }
recurringProduct
object
Recurring product details of the subscription.
Example:{ locationId: "Z4Bxl8J4SaPEPLq9IQ8g", funnel: "bQHJWKcyjiKjk4BHv91g", step: "2281a993-8a75-4b48-9912-571f29c99a74", name: "Sofa Set" }
canceledAt
date-time
Cancellation timestamp of the subscription.
Example:2023-11-20T10:23:36.515Z
canceledBy
string
User id who cancelled the subscription.
Example:qUuXUiB2AiA2DIthEicP
traceId
string
Trace id of the subscription.
Example:302d2cf4-1ba0-4bf5-bc3b-f8fa76fda58a
createdBy
string
User ID who created the subscription.
Example:user123














































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
curl -L 'https://services.leadconnectorhq.com/payments/subscriptions/:subscriptionId' \
-H 'Accept: application/json' \
-H 'Authorization: Bearer <TOKEN>'
REQUEST
COLLAPSE ALL
Base URL
https://services.leadconnectorhq.com
Auth
Bearer Token
Parameters
subscriptionId — path
REQUIRED
altId — query
REQUIRED
altType — query
REQUIRED
---
location
Version — header
REQUIRED
---
2021-07-28
SEND API REQUEST
RESPONSE
CLEAR
Click the Send API Request button above and see the response here!