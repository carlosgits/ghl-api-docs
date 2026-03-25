# Location

Source: https://marketplace.gohighlevel.com/docs/webhook/LocationCreate

Screenshot: images/webhook_LocationCreate_screenshot.png

---

WebhookLocationCreate
Location
Called whenever a location is created.
Available only to Agency Level Apps.
Schema
{
  "type": "object",
  "properties": {
    "type": {
      "type": "string"
    },
    "id": {
      "type": "string"
    },
    "name": {
      "type": "string"
    },
    "email": {
      "type": "string"
    },
    "stripeProductId": {
      "type": "string"
    },
    "companyId": {
      "type": "string"
    }
  }
}
Example
{
  "type": "LocationCreate",
  "id": "ve9EPM428h8vShlRW1KT",
  "companyId": "otg8dTQqGLh3Q6iQI55w",
  "name": "Loram ipsum",
  "email": "mailer@example.com",
  "stripeProductId": "prod_xyz123abc"
}
Share your feedback
★
★
★
★
★
Tags:Webhook Events