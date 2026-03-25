# Edit post

Source: https://marketplace.gohighlevel.com/docs/ghl/social-planner/edit-post

Screenshot: images/ghl_social-planner_edit-post_screenshot.png

---

Social PlannerPostEdit post
Edit post
PUT
 https://services.leadconnectorhq.com/social-media-posting/:locationId/posts/:id
Create posts for all supported platforms. It is possible to create customized posts per channel by using the same platform account IDs in a request and hitting the create post API multiple times with different summaries and account IDs per platform.
The content and media limitations, as well as platform rate limiters corresponding to the respective platforms, are provided in the following reference link:
Link: Platform Limitations
Requirements
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
locationId
string
REQUIRED
Location Id
Example: ve9EPM428h8vShlRW1KT
id
string
REQUIRED
Post Id
Example: 65fac446d599990d1313c1dd
APPLICATION/JSON
BODY
REQUIRED
accountIds
string[]
REQUIRED
Account IDs for the post. Each account ID identifies a connected social media account.
Get IDs from: Get Accounts API — use the id field from each account.
Validations:
Required for non-draft posts
Must be a non-empty array
All account IDs must be valid connected accounts for the location
Example:["aF3KhyL8JIuBwzK3m7Ly_iVrVJ2uoXNF0wzcBzgl5_12554616564525983496"]
summary
string
Post content/caption text. Character limits vary by platform.
Custom Values & Hashtags:
You can include custom values/variables in the content (e.g., {{contact.name}})
Hashtags: Use #hashtag format. Instagram allows max 30 hashtags.
Mentions: Use platform-specific mention format (see mentions field for structured mentions)
Validations:
Instagram/Facebook Story: Caption NOT supported for direct publishing
Facebook, LinkedIn, GMB: Content OR media is required (at least one)
Content is automatically trimmed to platform limits
Reference: Platform Limitations Guide
Example:Hello World! Check out our latest updates. #social #marketing
media
object[]
status
string
Post status indicating the current state of the post.
Available Status Values:
draft - Post saved as draft, not yet ready for publishing
scheduled - Post scheduled for future publishing (requires scheduleDate)
in_review - Post pending approval (requires scheduleDate and postApprovalDetails)
published - Post has been published
in_progress - Post is currently being processed
pending - Post is awaiting platform processing for Instagram media container creation
failed - Post publishing failed
notification_sent - Story notification sent (for manual story posting)
deleted - Post has been deleted
Validations:
scheduled or in_review status requires scheduleDate to be set
Draft posts skip most validations (accountIds, media requirements)
Possible values: [draft, scheduled, in_review, published, in_progress, pending, failed, notification_sent, deleted]
Example:scheduled
scheduleDate
string
Schedule Date
Example:2024-01-15T10:00:00Z
selectedBestTime
string
Selected Best Time slot for scheduling
Example:2024-01-15T10:00:00Z
createdBy
string
User ID of the creator who is creating/managing the post. Must be a valid MongoDB ObjectId.
Get User IDs from: Get User API — use the id field from the user object.
Validation: Must be a valid MongoDB ObjectId.
Example:65f151c99bc2bf3aaf970d72
followUpComment
string
Follow-up comment to be posted immediately after the main post is published.
Supported Platforms: Facebook, Instagram, LinkedIn, Pinterest, YouTube
NOT Supported: TikTok, Google My Business (GMB)
Use Case: Great for adding hashtags, additional context, or engagement prompts without cluttering the main post.
Example:What do you think? Let us know in the comments!
ogTagsDetails
object
type
string
REQUIRED
Type of post to create. Determines the format and platform requirements.
Available Types:
post - Standard feed post (all platforms)
story - Temporary 24-hour story (Instagram, Facebook)
reel - Short-form video content (Instagram, Facebook, TikTok, YouTube)
Customize Per Platform: You can specify different content/types per platform using facebookPostDetails.type, instagramPostDetails.type, etc.
Validations:
Reels require exactly 1 video
Stories: Caption not supported for Instagram/Facebook
Facebook Groups do not support Reels
Possible values: [post, story, reel]
Example:post
postApprovalDetails
object
scheduleTimeUpdated
boolean
Flag indicating if the schedule datetime was manually updated. Used for tracking rescheduled posts.
Example:true
tags
string[]
Array of Tag IDs to associate with the post for organization and filtering.
Get Tag IDs from: Get Tags API — use the _id field from each tag.
Validation: All IDs must be valid MongoDB ObjectIds.
Example:["65f151c99bc2bf3aaf970d72","65f151c99bc2bf3aaf970d73"]
categoryId
string
Category ID to organize the post. Categories help group related posts.
Get Category IDs from: Get Categories API — use the _id field.
Validation: Must be a valid MongoDB ObjectId.
Example:65f151c99bc2bf3aaf970d72
applyWatermark
boolean
Apply watermark to media in this post.
Note: Watermarks are applied to images only. Videos are not watermarked.
Example:true
tiktokPostDetails
object
gmbPostDetails
object
userId
string
REQUIRED
User ID of the user creating/managing the post. Required for OAuth channel posts (non-draft).
Example:sdfdsfdsfEWEsdfsdsW32dd
linkedinPostDetails
object
pinterestPostDetails
object
facebookPostDetails
object
instagramPostDetails
object
youtubePostDetails
object
communityPostDetails
object
Responses
200
400
401
422
Successful response
APPLICATION/JSON
Schema
Example (auto)
SCHEMA
success
boolean
REQUIRED
Success or Failure
Example:true
statusCode
number
REQUIRED
Status Code
Example:200
message
string
REQUIRED
Message
Example:Updated Post





















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
curl -L -X PUT 'https://services.leadconnectorhq.com/social-media-posting/:locationId/posts/:id' \
-H 'Content-Type: application/json' \
-H 'Accept: application/json' \
-H 'Authorization: Bearer <TOKEN>' \
-d '{
  "accountIds": [
    "aF3KhyL8JIuBwzK3m7Ly_iVrVJ2uoXNF0wzcBzgl5_12554616564525983496"
  ],
  "summary": "Hello World! Check out our latest updates. #social #marketing",
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
  "createdBy": "65f151c99bc2bf3aaf970d72",
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
  }
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
  "accountIds": [
    "aF3KhyL8JIuBwzK3m7Ly_iVrVJ2uoXNF0wzcBzgl5_12554616564525983496"
  ],
  "summary": "Hello World! Check out our latest updates. #social #marketing",
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
  "createdBy": "65f151c99bc2bf3aaf970d72",
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
  }
}
SEND API REQUEST
RESPONSE
CLEAR
Click the Send API Request button above and see the response here!