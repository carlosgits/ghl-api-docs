# App

Source: https://marketplace.gohighlevel.com/docs/webhook/AppUninstall

Screenshot: images/webhook_AppUninstall_screenshot.png

---

WebhookAppUninstall
App
Called whenever an app is uninstalled
Schema
{
  "type": "object",
  "properties": {
    "type": {
      "type": "string"
    },
    "appId": {
      "type": "string"
    },
    "companyId": {
      "type": "string"
    },
    "locationId": {
      "type": "string"
    }
  }
}
Example
For Location Level App Uninstall
{
  "type": "UNINSTALL",
  "appId": "ve9EPM428h8vShlRW1KT",
  "locationId": "otg8dTQqGLh3Q6iQI55w"
}
For Agency Level App Uninstall
{
  "type": "UNINSTALL",
  "appId": "ve9EPM428h8vShlRW1KT",
  "companyId": "otg8dTQqGLh3Q6iQI55w"
}
Share your feedback
★
★
★
★
★
Tags:Webhook Events