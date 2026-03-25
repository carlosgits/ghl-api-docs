# Migrate external authentication connection

Source: https://marketplace.gohighlevel.com/docs/ghl/marketplace/migrate-connection

Screenshot: images/ghl_marketplace_migrate-connection_screenshot.png

---

Developer marketplaceExternal Auth MigrationMigrate external authentication connection
Migrate external authentication connection
POST
 https://services.leadconnectorhq.com/marketplace/external-auth/migration
Migrates an external authentication connection credentials (basic or oauth2) for a specific app and location. This endpoint validates the app configuration, stores credentials safely in Highlevel's native encrypted storage. With this the lifecycle of the token is managed by Highlevel.
Requirements
Scope(s)
marketplace-external-auth-migration.write
Auth Method(s)
OAuth Access Token
Token Type(s)
Sub-Account Token
Sub-Account Token
Request
HEADER PARAMETERS
Version
string
REQUIRED
Possible values: [2021-07-28]
API Version
APPLICATION/JSON
BODY
REQUIRED
type
string
REQUIRED
Type of authentication - basic or oauth2
Possible values: [oauth2, basic]
Example:oauth2
locationId
string
REQUIRED
Location ID
Example:location_12345
appId
string
REQUIRED
App ID
Example:507f1f77bcf86cd799439011
appVersionId
string
REQUIRED
App Version ID
Example:507f1f77bcf86cd799439012
accountId
string
REQUIRED
Connection identifier
Example:my-connection-identifier
apiKey
string
API Key (supported when type is basic)
Example:sk_test_1234567890
basicCredentials
object
Basic auth credentials as key/value pairs (supported when type is basic). Keys are validated against the app version externalAuthConfig.fields.
Example:{"email":"user@example.com","password":"p@ssw0rd"}
accessToken
string
Access token (required when type is oauth2)
Example:ya29.a0AfH6SMBx...
refreshToken
string
Refresh token (required when type is oauth2)
Example:1//0gHq5F...
expiryIn
number
Access token expiry time in milliseconds (optional for oauth2)
Example:3600000
expiryAt
number
Timestamp for access token expiry (optional for oauth2)
Example:1735689600000
scopes
string[]
OAuth2 scopes (optional for oauth2)
Example:["contacts.readonly","contacts.write"]
displayName
string
Display name for the connection (optional, defaults to accountId)
Example:My Connection Display Name
isDefault
boolean
Whether this is the default connection for the location (optional, defaults to false)
Example:false
Responses
201
400
401
404
500
Connection migrated successfully
APPLICATION/JSON
Schema
Example (auto)
SCHEMA
success
boolean
REQUIRED
Indicates if the migration was successful
Example:true
identifier
string
REQUIRED
Unique identifier for the migrated connection
Example:migration_12345
message
string
Message describing the result
Example:Connection migrated successfully


















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
curl -L 'https://services.leadconnectorhq.com/marketplace/external-auth/migration' \
-H 'Content-Type: application/json' \
-H 'Accept: application/json' \
-H 'Authorization: Bearer <TOKEN>' \
--data-raw '{
  "type": "oauth2",
  "locationId": "location_12345",
  "appId": "507f1f77bcf86cd799439011",
  "appVersionId": "507f1f77bcf86cd799439012",
  "accountId": "my-connection-identifier",
  "apiKey": "sk_test_1234567890",
  "basicCredentials": {
    "email": "user@example.com",
    "password": "p@ssw0rd"
  },
  "accessToken": "ya29.a0AfH6SMBx...",
  "refreshToken": "1//0gHq5F...",
  "expiryIn": 3600000,
  "expiryAt": 1735689600000,
  "scopes": [
    "contacts.readonly",
    "contacts.write"
  ],
  "displayName": "My Connection Display Name",
  "isDefault": false
}'
REQUEST
COLLAPSE ALL
Base URL
https://services.leadconnectorhq.com
Auth
Security Scheme
Location-Access
Location-Access-Only
Bearer Token
Parameters
Version — header
REQUIRED
---
2021-07-28
Body
 REQUIRED
{
  "type": "oauth2",
  "locationId": "location_12345",
  "appId": "507f1f77bcf86cd799439011",
  "appVersionId": "507f1f77bcf86cd799439012",
  "accountId": "my-connection-identifier",
  "apiKey": "sk_test_1234567890",
  "basicCredentials": {
    "email": "user@example.com",
    "password": "p@ssw0rd"
  },
  "accessToken": "ya29.a0AfH6SMBx...",
  "refreshToken": "1//0gHq5F...",
  "expiryIn": 3600000,
  "expiryAt": 1735689600000,
  "scopes": [
    "contacts.readonly",
    "contacts.write"
  ],
  "displayName": "My Connection Display Name",
  "isDefault": false
}
SEND API REQUEST
RESPONSE
CLEAR
Click the Send API Request button above and see the response here!