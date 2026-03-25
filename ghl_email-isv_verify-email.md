# Email Verification

Source: https://marketplace.gohighlevel.com/docs/ghl/email-isv/verify-email

Screenshot: C:\Users\carlo\OneDrive\Desktop\Proyectos\ghl-api-docs\images\ghl_email-isv_verify-email_screenshot.png

---

LC EmailEmail VerificationEmail Verification
Email Verification
POST
 https://services.leadconnectorhq.com/email/verify
Verify Email
Requirements
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
QUERY PARAMETERS
locationId
string
REQUIRED
Location Id, The email verification charges will be deducted from this location (if rebilling is enabled) / company wallet
Example: 5DP4iH6HLkQsiKESj6rh
APPLICATION/JSON
BODY
REQUIRED
type
string
REQUIRED
Email Verification type
Possible values: [email, contact]
Example:email
verify
string
REQUIRED
Email Verification recepient (email address / contactId)
Example:abc@xyz.com
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
oneOf
EmailVerifiedResponseDto
EmailNotVerifiedResponseDto
reason
string[]
Reason for email verification failure
Example:["mailbox_does_not_exist"]
result
string
REQUIRED
Email verification result
Possible values: [deliverable, undeliverable, do_not_send, unknown, catch_all]
Example:undeliverable
risk
string
REQUIRED
Risk level of email sending to bounce
Possible values: [high, low, medium, unknown]
Example:low
address
string
REQUIRED
Email address
Example:abc@xyz.com
leadconnectorRecomendation
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
curl -L 'https://services.leadconnectorhq.com/email/verify' \
-H 'Content-Type: application/json' \
-H 'Accept: application/json' \
-H 'Authorization: Bearer <TOKEN>' \
--data-raw '{
  "type": "email",
  "verify": "abc@xyz.com"
}'
REQUEST
COLLAPSE ALL
Base URL
https://services.leadconnectorhq.com
Auth
Bearer Token
Parameters
locationId — query
REQUIRED
Version — header
REQUIRED
---
2021-07-28
Body
 REQUIRED
{
  "type": "email",
  "verify": "abc@xyz.com"
}
SEND API REQUEST
RESPONSE
CLEAR
Click the Send API Request button above and see the response here!