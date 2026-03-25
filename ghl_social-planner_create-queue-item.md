# Create a new item in the queue

Source: https://marketplace.gohighlevel.com/docs/ghl/social-planner/create-queue-item

Screenshot: images/ghl_social-planner_create-queue-item_screenshot.png

---

Social PlannerCategory QueueCreate a new item in the queue
Create a new item in the queue
POST
 https://services.leadconnectorhq.com/social-media-posting/category/queues/:queueId/create/item
Adds a new post item to a queue. Use sessionId for edit session or directToQueue for immediate addition.
Requirements
Scope(s)
socialplanner/category.write
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
Example: 2021-07-28
PATH PARAMETERS
queueId
string
REQUIRED
APPLICATION/JSON
BODY
REQUIRED
locationId
string
REQUIRED
Location ID
Example:609e126a1c4ae1001291e1b5
sessionId
string
Edit session ID
Example:60af88475f1b2c001f5d5f4b
modifiedPostPayload
object
order
object
variations
object[]
primaryImage
string
Primary media URL (image) for the post. Falls back to modifiedPostPayload.primaryImage if not set.
Example:http://example.com/media.png
directToQueue
boolean
When true, creates the queue item directly without requiring an edit session, even for active/paused queues. The order field is ignored and the item position is determined by the queue's prioritizeNewContent setting: if true, the item is added to the top of the queue; if false, it is added to the bottom.
Example:false
Responses
201
400
401
422
Queue item created successfully.
APPLICATION/JSON
Schema
Example (auto)
SCHEMA
success
boolean
REQUIRED
Example:true
statusCode
number
REQUIRED
Example:201
results
object
REQUIRED
traceId
string





































































































































































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
curl -L 'https://services.leadconnectorhq.com/social-media-posting/category/queues/:queueId/create/item' \
-H 'Content-Type: application/json' \
-H 'Accept: application/json' \
-H 'Authorization: Bearer <TOKEN>' \
-d '{
  "locationId": "609e126a1c4ae1001291e1b5",
  "sessionId": "60af88475f1b2c001f5d5f4b",
  "modifiedPostPayload": {
    "accountIds": [
      "aF3KhyL8JIuBwzK3m7Ly_iVrVJ2uoXNF0wzcBzgl5_12554616564525983496"
    ],
    "summary": "Hello World",
    "media": [
      {
        "url": "https://example.com/image.jpg",
        "type": "image/jpeg",
        "caption": "Sample caption"
      }
    ],
    "status": "scheduled",
    "scheduleDate": "2024-01-15T10:00:00Z",
    "selectedBestTime": "2024-01-15T10:00:00Z",
    "createdBy": "Lx1EI6YIgQYMQi0ytFXv",
    "followUpComment": "What do you think? Let us know in the comments!",
    "ogTagsDetails": {
      "metaImage": "https://example.com/image.jpg",
      "metaLink": "https://www.yahoo.com/",
      "ogTitle": "Page Title",
      "ogDescription": "Page Description"
    },
    "type": "post",
    "postApprovalDetails": {
      "approver": "iVrVJ2uoXNF0wzcBzgl5",
      "approvalStatus": "pending"
    },
    "scheduleTimeUpdated": true,
    "tags": [
      "65f151c99bc2bf3aaf970d72",
      "65f151c99bc2bf3aaf970d73"
    ],
    "categoryId": "65f151c99bc2bf3aaf970d72",
    "applyWatermark": true,
    "tiktokPostDetails": {
      "privacyLevel": "PUBLIC_TO_EVERYONE",
      "enableComment": true,
      "enableDuet": false
    },
    "gmbPostDetails": {
      "gmbEventType": "STANDARD",
      "actionType": "BOOK",
      "url": "https://example.com"
    },
    "userId": "sdfdsfdsfEWEsdfsdsW32dd",
    "linkedinPostDetails": {
      "pdfTitle": "Q4 Marketing Strategy Presentation",
      "postAsPdf": true
    },
    "pinterestPostDetails": {
      "title": "10 Easy Home Decor Ideas for 2024",
      "link": "https://yoursite.com/blog/home-decor-ideas",
      "boardIds": {
        "6887d6de1d8175813d50dab8": "987654321098765432",
        "682c7d1710a2fe3d805a3513": "123456789012345678"
      },
      "shortenedLinks": [
        "string"
      ]
    },
    "facebookPostDetails": {
      "type": "post"
    },
    "instagramPostDetails": {
      "type": "post",
      "collaborators": {
        "accountId1": [
          "username1",
          "username2"
        ],
        "accountId2": [
          "username3",
          "username4"
        ]
      },
      "showOnFeed": true,
      "publishViaPushNotification": true,
      "publisherNote": "When publishing, add swipe up link to the landing page so that we can direct them to the sales page"
    },
    "youtubePostDetails": {
      "title": "How to Build a Successful Marketing Strategy in 2024",
      "privacyLevel": "public",
      "type": "video"
    },
    "communityPostDetails": {
      "title": "Welcome to Our New Community Feature!",
      "notifyAllGroupMembers": true,
      "postAsUser": {
        "xMQswA02zgqKPpxITe": {
          "avatar": "https://lh3.googleusercontent.com/a/user-avatar.jpg",
          "id": "snCr14eeYkSppD04rkNW",
          "name": "John Smith"
        }
      }
    },
    "locationId": "ve9EPM428h8vShlRW1KT"
  },
  "order": 0,
  "variations": [
    {
      "content": "Check out our latest blog post! #marketing #socialmedia",
      "mentions": [
        {
          "platform": "instagram",
          "username": "example_user",
          "offset": 10,
          "length": 12
        }
      ],
      "ogTags": {
        "metaLink": "https://example.com/blog/post-title",
        "metaImage": "https://example.com/images/preview.png",
        "ogTitle": "Check out our latest blog post!"
      }
    }
  ],
  "primaryImage": "http://example.com/media.png",
  "directToQueue": false
}'
REQUEST
COLLAPSE ALL
Base URL
https://services.leadconnectorhq.com
Auth
Bearer Token
Parameters
queueId — path
REQUIRED
Version — header
REQUIRED
---
2021-07-28
Body
 REQUIRED
{
  "locationId": "609e126a1c4ae1001291e1b5",
  "sessionId": "60af88475f1b2c001f5d5f4b",
  "modifiedPostPayload": {
    "accountIds": [
      "aF3KhyL8JIuBwzK3m7Ly_iVrVJ2uoXNF0wzcBzgl5_12554616564525983496"
    ],
    "summary": "Hello World",
    "media": [
      {
        "url": "https://example.com/image.jpg",
        "type": "image/jpeg",
        "caption": "Sample caption"
      }
    ],
    "status": "scheduled",
    "scheduleDate": "2024-01-15T10:00:00Z",
    "selectedBestTime": "2024-01-15T10:00:00Z",
    "createdBy": "Lx1EI6YIgQYMQi0ytFXv",
    "followUpComment": "What do you think? Let us know in the comments!",
    "ogTagsDetails": {
      "metaImage": "https://example.com/image.jpg",
      "metaLink": "https://www.yahoo.com/",
      "ogTitle": "Page Title",
      "ogDescription": "Page Description"
    },
    "type": "post",
    "postApprovalDetails": {
      "approver": "iVrVJ2uoXNF0wzcBzgl5",
      "approvalStatus": "pending"
    },
    "scheduleTimeUpdated": true,
    "tags": [
      "65f151c99bc2bf3aaf970d72",
      "65f151c99bc2bf3aaf970d73"
    ],
    "categoryId": "65f151c99bc2bf3aaf970d72",
    "applyWatermark": true,
    "tiktokPostDetails": {
      "privacyLevel": "PUBLIC_TO_EVERYONE",
      "enableComment": true,
      "enableDuet": false
    },
    "gmbPostDetails": {
      "gmbEventType": "STANDARD",
      "actionType": "BOOK",
      "url": "https://example.com"
    },
    "userId": "sdfdsfdsfEWEsdfsdsW32dd",
    "linkedinPostDetails": {
      "pdfTitle": "Q4 Marketing Strategy Presentation",
      "postAsPdf": true
    },
    "pinterestPostDetails": {
      "title": "10 Easy Home Decor Ideas for 2024",
      "link": "https://yoursite.com/blog/home-decor-ideas",
      "boardIds": {
        "6887d6de1d8175813d50dab8": "987654321098765432",
        "682c7d1710a2fe3d805a3513": "123456789012345678"
      },
      "shortenedLinks": [
        "string"
      ]
    },
    "facebookPostDetails": {
      "type": "post"
    },
    "instagramPostDetails": {
      "type": "post",
      "collaborators": {
        "accountId1": [
          "username1",
          "username2"
        ],
        "accountId2": [
          "username3",
          "username4"
        ]
      },
      "showOnFeed": true,
      "publishViaPushNotification": true,
      "publisherNote": "When publishing, add swipe up link to the landing page so that we can direct them to the sales page"
    },
    "youtubePostDetails": {
      "title": "How to Build a Successful Marketing Strategy in 2024",
      "privacyLevel": "public",
      "type": "video"
    },
    "communityPostDetails": {
      "title": "Welcome to Our New Community Feature!",
      "notifyAllGroupMembers": true,
      "postAsUser": {
        "xMQswA02zgqKPpxITe": {
          "avatar": "https://lh3.googleusercontent.com/a/user-avatar.jpg",
          "id": "snCr14eeYkSppD04rkNW",
          "name": "John Smith"
        }
      }
    },
    "locationId": "ve9EPM428h8vShlRW1KT"
  },
  "order": 0,
  "variations": [
    {
      "content": "Check out our latest blog post! #marketing #socialmedia",
      "mentions": [
        {
          "platform": "instagram",
          "username": "example_user",
          "offset": 10,
          "length": 12
        }
      ],
      "ogTags": {
        "metaLink": "https://example.com/blog/post-title",
        "metaImage": "https://example.com/images/preview.png",
        "ogTitle": "Check out our latest blog post!"
      }
    }
  ],
  "primaryImage": "http://example.com/media.png",
  "directToQueue": false
}
SEND API REQUEST
RESPONSE
CLEAR
Click the Send API Request button above and see the response here!