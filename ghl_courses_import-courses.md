# Import Courses

Source: https://marketplace.gohighlevel.com/docs/ghl/courses/import-courses

Screenshot: C:\Users\carlo\OneDrive\Desktop\Proyectos\ghl-api-docs\images\ghl_courses_import-courses_screenshot.png

---

CoursesUNTAGGEDImport Courses
Import Courses
POST
 https://services.leadconnectorhq.com/courses/courses-exporter/public/import
Import Courses through public channels
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
APPLICATION/JSON
BODY
REQUIRED
locationId
string
REQUIRED
userId
string
products
object[]
REQUIRED
Responses
201
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
curl -L 'https://services.leadconnectorhq.com/courses/courses-exporter/public/import' \
-H 'Content-Type: application/json' \
-H 'Authorization: Bearer <TOKEN>' \
-d '{
  "locationId": "string",
  "userId": "string",
  "products": [
    {
      "title": "string",
      "description": "string",
      "imageUrl": "string",
      "categories": [
        {
          "title": "string",
          "visibility": "published",
          "thumbnailUrl": "string",
          "posts": [
            {
              "title": "string",
              "visibility": "published",
              "thumbnailUrl": "string",
              "contentType": "video",
              "description": "string",
              "bucketVideoUrl": "string",
              "postMaterials": [
                {
                  "title": "string",
                  "type": "pdf",
                  "url": "string"
                }
              ]
            }
          ],
          "subCategories": [
            {
              "title": "string",
              "visibility": "published",
              "thumbnailUrl": "string",
              "posts": [
                {
                  "title": "string",
                  "visibility": "published",
                  "thumbnailUrl": "string",
                  "contentType": "video",
                  "description": "string",
                  "bucketVideoUrl": "string",
                  "postMaterials": [
                    {
                      "title": "string",
                      "type": "pdf",
                      "url": "string"
                    }
                  ]
                }
              ]
            }
          ]
        }
      ],
      "instructorDetails": {
        "name": "string",
        "description": "string"
      }
    }
  ]
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
  "locationId": "string",
  "userId": "string",
  "products": [
    {
      "title": "string",
      "description": "string",
      "imageUrl": "string",
      "categories": [
        {
          "title": "string",
          "visibility": "published",
          "thumbnailUrl": "string",
          "posts": [
            {
              "title": "string",
              "visibility": "published",
              "thumbnailUrl": "string",
              "contentType": "video",
              "description": "string",
              "bucketVideoUrl": "string",
              "postMaterials": [
                {
                  "title": "string",
                  "type": "pdf",
                  "url": "string"
                }
              ]
            }
          ],
          "subCategories": [
            {
              "title": "string",
              "visibility": "published",
              "thumbnailUrl": "string",
              "posts": [
                {
                  "title": "string",
                  "visibility": "published",
                  "thumbnailUrl": "string",
                  "contentType": "video",
                  "description": "string",
                  "bucketVideoUrl": "string",
                  "postMaterials": [
                    {
                      "title": "string",
                      "type": "pdf",
                      "url": "string"
                    }
                  ]
                }
              ]
            }
          ]
        }
      ],
      "instructorDetails": {
        "name": "string",
        "description": "string"
      }
    }
  ]
}
SEND API REQUEST
RESPONSE
CLEAR
Click the Send API Request button above and see the response here!