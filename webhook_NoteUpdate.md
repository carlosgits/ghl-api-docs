# Note

Source: https://marketplace.gohighlevel.com/docs/webhook/NoteUpdate

Screenshot: images/webhook_NoteUpdate_screenshot.png

---

WebhookNoteUpdate
Note
Called whenever a note is updated
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
  "type": "NoteUpdate",
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