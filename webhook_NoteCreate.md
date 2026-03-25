# Note

Source: https://marketplace.gohighlevel.com/docs/webhook/NoteCreate

Screenshot: C:\Users\carlo\OneDrive\Desktop\Proyectos\ghl-api-docs\images\webhook_NoteCreate_screenshot.png

---

WebhookNoteCreate
Note
Called whenever a note is created
Schema
{
  "type": "object",
  "properties": {
    "type": {
      "type": "string"
    },
    "locationId": {
      "type": "string"
    },
    "id": {
      "type": "string"
    },
    "body": {
      "type": "string"
    },
    "contactId": {
      "type": "string"
    },
    "dateAdded": {
      "type": "string"
    }
  }
}
Example
{
  "type": "NoteCreate",
  "locationId": "ve9EPM428h8vShlRW1KT",
  "id": "otg8dTQqGLh3Q6iQI55w",
  "body": "Loram ipsum",
  "contactId": "CWBf1PR9LvvBkcYqiXlc",
  "dateAdded": "2021-11-26T12:41:02.193Z"
}
Share your feedback
★
★
★
★
★
Tags:Webhook Events