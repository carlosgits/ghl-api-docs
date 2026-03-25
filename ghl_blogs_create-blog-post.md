# Create Blog Post

Source: https://marketplace.gohighlevel.com/docs/ghl/blogs/create-blog-post

Screenshot: images/ghl_blogs_create-blog-post_screenshot.png

---

BlogsBlogsCreate Blog Post
Create Blog Post
POST
 https://services.leadconnectorhq.com/blogs/posts
The "Create Blog Post" API allows you create blog post for any given blog site. Please use blogs/post.write
Requirements
Scope(s)
blogs/post.write
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
title
string
REQUIRED
Example:Your blog title
locationId
string
REQUIRED
Example:Location ID
blogId
string
REQUIRED
You can find the blog id from blog site dashboard link
Example:Blog ID
imageUrl
string
REQUIRED
Example:Image URl
description
string
REQUIRED
Example:A short description
rawHTML
string
REQUIRED
Example:<h1>Your blog content</h1>
status
string
REQUIRED
Possible values: [DRAFT, PUBLISHED, SCHEDULED, ARCHIVED]
Example:This can be PUBLISHED OR SCHEDULED OR ARCHIVED OR DRAFT
imageAltText
string
REQUIRED
Example:Alt text for your blog image
categories
string[]
REQUIRED
This needs to be array of category ids, which you can get from the category get api call.
Example:["9c48df2694a849b6089f9d0d3513efe","6683abde331c041f32c07aee"]
tags
string[]
Example:["blog","seo"]
author
string
REQUIRED
This needs to be author id, which you can get from the author get api call.
Example:6683abde331c041f32c07aea
urlSlug
string
REQUIRED
Example:any-blog-post-url
canonicalLink
string
Example:https://tryghl.blog/post/testing-unsplash
publishedAt
string
REQUIRED
Provide ISO timestamp
Example:2025-02-05T18:30:47.000Z
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
data
object
REQUIRED








































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
curl -L 'https://services.leadconnectorhq.com/blogs/posts' \
-H 'Content-Type: application/json' \
-H 'Accept: application/json' \
-H 'Authorization: Bearer <TOKEN>' \
-d '{
  "title": "Your blog title",
  "locationId": "Location ID",
  "blogId": "Blog ID",
  "imageUrl": "Image URl",
  "description": "A short description",
  "rawHTML": "<h1>Your blog content</h1>",
  "status": "This can be PUBLISHED OR SCHEDULED OR ARCHIVED OR DRAFT",
  "imageAltText": "Alt text for your blog image",
  "categories": [
    "9c48df2694a849b6089f9d0d3513efe",
    "6683abde331c041f32c07aee"
  ],
  "tags": [
    "blog",
    "seo"
  ],
  "author": "6683abde331c041f32c07aea",
  "urlSlug": "any-blog-post-url",
  "canonicalLink": "https://tryghl.blog/post/testing-unsplash",
  "publishedAt": "2025-02-05T18:30:47.000Z"
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
  "title": "Your blog title",
  "locationId": "Location ID",
  "blogId": "Blog ID",
  "imageUrl": "Image URl",
  "description": "A short description",
  "rawHTML": "<h1>Your blog content</h1>",
  "status": "This can be PUBLISHED OR SCHEDULED OR ARCHIVED OR DRAFT",
  "imageAltText": "Alt text for your blog image",
  "categories": [
    "9c48df2694a849b6089f9d0d3513efe",
    "6683abde331c041f32c07aee"
  ],
  "tags": [
    "blog",
    "seo"
  ],
  "author": "6683abde331c041f32c07aea",
  "urlSlug": "any-blog-post-url",
  "canonicalLink": "https://tryghl.blog/post/testing-unsplash",
  "publishedAt": "2025-02-05T18:30:47.000Z"
}
SEND API REQUEST
RESPONSE
CLEAR
Click the Send API Request button above and see the response here!