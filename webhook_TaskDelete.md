# Task

Source: https://marketplace.gohighlevel.com/docs/webhook/TaskDelete

Screenshot: C:\Users\carlo\OneDrive\Desktop\Proyectos\ghl-api-docs\images\webhook_TaskDelete_screenshot.png

---

WebhookTaskDelete
Task
Called whenever a task is deleted
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
    "assignedTo": {
      "type": "string"
    },
    "body": {
      "type": "string"
    },
    "contactId": {
      "type": "string"
    },
    "title": {
      "type": "string"
    },
    "dateAdded": {
      "type": "string"
    },
    "dueDate": {
      "type": "string"
    }
  }
}
Example
{
  "type": "TaskDelete",
  "locationId": "ve9EPM428h8vShlRW1KT",
  "id": "UlRWGLSXh0ji5qbiGu4i",
  "assignedTo": "63e4qiWDsFJjOYAC8phG",
  "body": "Loram ipsum",
  "contactId": "CWBf1PR9LvvBkcYqiXlc",
  "title": "Loram ipsum",
  "dateAdded": "2021-11-26T12:41:02.193Z",
  "dueDate": "2021-11-26T12:41:02.193Z"
}
Share your feedback
★
★
★
★
★
Tags:Webhook Events