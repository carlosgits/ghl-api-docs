# Location

Source: https://marketplace.gohighlevel.com/docs/webhook/LocationUpdate

Screenshot: C:\Users\carlo\OneDrive\Desktop\Proyectos\ghl-api-docs\images\webhook_LocationUpdate_screenshot.png

---

WebhookLocationUpdate
Location
Called whenever a location is updated.
Available to Agency Level Apps for all sub-accounts or to specific sub-accounts.
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
  "type": "LocationUpdate",
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