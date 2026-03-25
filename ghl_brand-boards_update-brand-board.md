# Update a Brand Board

Source: https://marketplace.gohighlevel.com/docs/ghl/brand-boards/update-brand-board

Screenshot: images/ghl_brand-boards_update-brand-board_screenshot.png

---

Brand BoardsBrand BoardsUpdate a Brand Board
Update a Brand Board
PATCH
 https://services.leadconnectorhq.com/brand-boards/:locationId/:id
Updates an existing Brand Board
Requirements
Scope(s)
brand-boards/design-kit.write
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
locationId
string
REQUIRED
Location ID where the brand board exists
Example: ve9EPM428h8vShlRW1KT
id
string
REQUIRED
Brand board ID to update, retrieve, or delete
Example: 507f1f77bcf86cd799439011
APPLICATION/JSON
BODY
REQUIRED
name
string
Name of the brand board
Example:My Brandboard 2
logos
object[]
colors
object[]
fonts
object[]
default
boolean
Set as the default brand board for this location
Example:true
parentId
string
Parent folder ID in media library (reserved for future use)
Example:507f1f77bcf86cd799439011
Responses
200
400
401
403
404
422
Success
APPLICATION/JSON
Schema
Example (auto)
SCHEMA
_id
string
REQUIRED
Brand board ID
Example:507f1f77bcf86cd799439011
locationId
string
REQUIRED
Location ID
Example:ve9EPM428h8vShlRW1KT
name
string
REQUIRED
Brand board name
Example:My Brand Board
logos
object[]
colors
object[]
fonts
object[]
default
boolean
REQUIRED
Whether this is the default brand board for the location
Example:false
deleted
boolean
REQUIRED
Whether the brand board has been soft deleted
Example:false
parentId
string
Parent folder ID in media library
Example:507f1f77bcf86cd799439011
folderId
string
Media library folder ID for this brand board
Example:507f1f77bcf86cd799439011
originId
string
Original brand board ID if cloned from snapshot
Example:507f1f77bcf86cd799439011
meta
object
createdAt
string
Creation timestamp
Example:2024-01-05T12:00:00.000Z
updatedAt
string
Last update timestamp
Example:2024-01-05T12:00:00.000Z





































































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
curl -L -X PATCH 'https://services.leadconnectorhq.com/brand-boards/:locationId/:id' \
-H 'Content-Type: application/json' \
-H 'Accept: application/json' \
-H 'Authorization: Bearer <TOKEN>' \
-d '{
  "name": "My Brandboard 2",
  "logos": [
    {
      "id": "logo_abc123",
      "url": "https://storage.googleapis.com/bucket/logos/my-logo.png",
      "label": "Primary Logo",
      "path": "/locations/ve9EPM428h8vShlRW1KT/logos/my-logo.png"
    }
  ],
  "colors": [
    {
      "id": "color_xyz789",
      "hexa": "#FF5733FF",
      "rgba": "rgba(255, 87, 51, 1)",
      "hex": "#FF5733",
      "rgb": "rgb(255, 87, 51)",
      "label": "Brand Orange"
    }
  ],
  "fonts": [
    {
      "id": "font_def456",
      "font": "Montserrat",
      "fallback": "sans-serif",
      "label": "Heading Font"
    }
  ],
  "default": true,
  "parentId": "507f1f77bcf86cd799439011"
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
id — path
REQUIRED
Version — header
REQUIRED
---
2021-07-28
Body
 REQUIRED
{
  "name": "My Brandboard 2",
  "logos": [
    {
      "id": "logo_abc123",
      "url": "https://storage.googleapis.com/bucket/logos/my-logo.png",
      "label": "Primary Logo",
      "path": "/locations/ve9EPM428h8vShlRW1KT/logos/my-logo.png"
    }
  ],
  "colors": [
    {
      "id": "color_xyz789",
      "hexa": "#FF5733FF",
      "rgba": "rgba(255, 87, 51, 1)",
      "hex": "#FF5733",
      "rgb": "rgb(255, 87, 51)",
      "label": "Brand Orange"
    }
  ],
  "fonts": [
    {
      "id": "font_def456",
      "font": "Montserrat",
      "fallback": "sans-serif",
      "label": "Heading Font"
    }
  ],
  "default": true,
  "parentId": "507f1f77bcf86cd799439011"
}
SEND API REQUEST
RESPONSE
CLEAR
Click the Send API Request button above and see the response here!