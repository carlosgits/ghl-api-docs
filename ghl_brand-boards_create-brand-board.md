# Create a new brand board

Source: https://marketplace.gohighlevel.com/docs/ghl/brand-boards/create-brand-board

Screenshot: images/ghl_brand-boards_create-brand-board_screenshot.png

---

Brand BoardsBrand BoardsCreate a new brand board
Create a new brand board
POST
 https://services.leadconnectorhq.com/brand-boards/
Creates a new brand board with logos, colors, and fonts
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
APPLICATION/JSON
BODY
REQUIRED
locationId
string
REQUIRED
Location ID where the brand board will be created
Example:ve9EPM428h8vShlRW1KT
name
string
REQUIRED
Name of the brand board
Example:My Brand Board
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
brandBoardId
string
Source brand board ID to copy from (creates a new brand board based on this template)
Example:507f1f77bcf86cd799439011
parentId
string
Parent folder ID in media library for organizing brand boards
Example:507f1f77bcf86cd799439011
type
string
Source type indicating how the brand board was created
Possible values: [template, blank, snapshot]
Example:blank
Responses
201
400
401
403
422
Created
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
curl -L 'https://services.leadconnectorhq.com/brand-boards/' \
-H 'Content-Type: application/json' \
-H 'Accept: application/json' \
-H 'Authorization: Bearer <TOKEN>' \
-d '{
  "locationId": "ve9EPM428h8vShlRW1KT",
  "name": "My Brand Board",
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
  "brandBoardId": "507f1f77bcf86cd799439011",
  "parentId": "507f1f77bcf86cd799439011",
  "type": "blank"
}'
REQUEST
COLLAPSE ALL
Base URL
https://services.leadconnectorhq.com
Auth
Bearer Token
Parameters
Version — header
REQUIRED
---
2021-07-28
Body
 REQUIRED
{
  "locationId": "ve9EPM428h8vShlRW1KT",
  "name": "My Brand Board",
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
  "brandBoardId": "507f1f77bcf86cd799439011",
  "parentId": "507f1f77bcf86cd799439011",
  "type": "blank"
}
SEND API REQUEST
RESPONSE
CLEAR
Click the Send API Request button above and see the response here!