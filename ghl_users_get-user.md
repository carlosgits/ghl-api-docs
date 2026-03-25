# Get User

Source: https://marketplace.gohighlevel.com/docs/ghl/users/get-user

Screenshot: images/ghl_users_get-user_screenshot.png

---

UsersUsersGet User
Get User
GET
 https://services.leadconnectorhq.com/users/:userId
Get User
Requirements
Scope(s)
users.readonly
Auth Method(s)
OAuth Access Token
Private Integration Token
Token Type(s)
Agency Token
Sub-Account Token
Request
HEADER PARAMETERS
Version
string
REQUIRED
Possible values: [2021-07-28]
API Version
PATH PARAMETERS
userId
string
REQUIRED
User Id
Example: ve9EPM428h8vShlRW1KT
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
id
string
Example:0IHuJvc2ofPAAA8GzTRi
name
string
Example:John Deo
firstName
string
Example:John
lastName
string
Example:Deo
email
string
Example:john@deo.com
phone
string
Example:+1 808-868-8888
extension
string
Example:
permissions
object
scopes
string
Possible values: [campaigns.readonly, campaigns.write, calendars.readonly, calendars/events.write, calendars/groups.write, calendars.write, contacts.write, contacts/bulkActions.write, workflows.readonly, workflows.write, triggers.write, funnels.write, forms.write, surveys.write, quizzes.write, websites.write, medias.write, medias.readonly, opportunities.write, opportunities/leadValue.readonly, opportunities/bulkActions.write, reporting/phone.readonly, reporting/adwords.readonly, reporting/facebookAds.readonly, reporting/attributions.readonly, prospecting/auditReport.write, reporting/reports.readonly, reporting/agent.readonly, reporting/reports.write, reporting/stats.export, payments.write, payments/records.write, payments/orders.readonly, payments/orders.export, payments/orders.import, payments/orders.collectPayment, payments/subscriptions.readonly, payments/subscriptions.write, payments/subscriptions.update, payments/subscriptions.export, payments/subscriptions.pauseResumeCancel, payments/subscriptions.sharePaymentMethod, payments/transactions.readonly, payments/transactions.export, payments/transactions.import, payments/transactions.refund, payments/transactions.viewReceipts, payments/taxesSettings.readonly, payments/settings.readonly, payments/taxesSettings.updateInclusiveExclusive, payments/taxesSettings.manageRates, payments/taxesSettings.configureAutomatic, products.readonly, products.write, products.delete, products.duplicate, products.bulkActions, payments/settings.configureReceipt, payments/settings.configureSubscription, invoices.write, invoices.readonly, invoices/schedule.readonly, invoices/schedule.write, invoices/template.readonly, invoices/template.write, reputation/review.write, reputation/listing.write, reputation/reviewsAIAgents.write, reputation/gbp.write, conversations.write, conversations.readonly, conversations/message.readonly, conversations/message.write, contentAI.write, dashboard/stats.readonly, locations/tags.write, locations/tags.readonly, marketing.write, eliza.write, settings.write, socialplanner/post.write, socialplanner/account.readonly, socialplanner/account.write, socialplanner/category.readonly, socialplanner/category.write, socialplanner/csv.readonly, socialplanner/csv.write, socialplanner/group.write, socialplanner/hashtag.readonly, socialplanner/hashtag.write, socialplanner/oauth.readonly, socialplanner/oauth.write, socialplanner/post.readonly, socialplanner/recurring.readonly, socialplanner/recurring.write, socialplanner/review.readonly, socialplanner/review.write, socialplanner/rss.readonly, socialplanner/rss.write, socialplanner/search.readonly, socialplanner/setting.readonly, socialplanner/setting.write, socialplanner/stat.readonly, socialplanner/tag.readonly, socialplanner/tag.write, socialplanner/filters.readonly, socialplanner/medias.readonly, socialplanner/medias.write, socialplanner/watermarks.readonly, socialplanner/watermarks.write, socialplanner/metatag.readonly, socialplanner/facebook.readonly, socialplanner/linkedin.readonly, socialplanner/twitter.readonly, socialplanner/notification.readonly, socialplanner/notification.write, socialplanner/snapshot.readonly, socialplanner/snapshot.write, marketing/affiliate.write, blogs.write, membership.write, communities.write, gokollab.write, certificates.write, certificates.readonly, adPublishing.write, adPublishing.readonly, prospecting.write, prospecting.readonly, prospecting/reports.readonly, private-integration-location.readonly, private-integration-location.write, private-integration-company.readonly, private-integration-company.write, native-integrations.readonly, native-integrations.write, wordpress.write, wordpress.read, custom-menu-link.write, qrcodes.write, users/team-management.write, users/team-management.readonly, loginas.write, users-sso-login-management.write, users-sso-login-management.readonly, sso-config.write, snapshots/api.readonly, snapshots/api.create, snapshots/api.edit, snapshots/api.push, snapshots/api.refresh, snapshots/api.share, snapshots/api.delete, internaltools.location-transfer.write, internaltools.location-transfer.readonly, affiliateportal.write, affiliateportal.readonly, companies.write, internaltools.billing.write, internaltools.billing.readonly, internaltools.billing-common.readonly, internaltools.billing-common.write, voice-ai-agents.write, voice-ai-agents.readonly, voice-ai-common.readonly, voice-ai-common.write, voice-ai-agent-goals.readonly, voice-ai-agent-goals.write, voice-ai-dashboard.readonly, agency/launchpad.write, agency/launchpad.readonly, launchpad/location.write, launchpad/location.readonly, text-ai-agents.write, text-ai-agent-goals.readonly, text-ai-agent-goals.write, text-ai-agent-training.write, text-ai-agents-dashboard.readonly]
roles
object
lcPhone
object
LC Phone Inbound Phone Numbers
Example:{"locationId":"+1234556677"}
platformLanguage
string
Platform language preference for the user
Possible values: [en_US, es, fr_CA, fr_FR, nl, de, pt_PT, pt_BR, it, sv, da, fi, no]
Example:en_US














































































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
curl -L 'https://services.leadconnectorhq.com/users/:userId' \
-H 'Accept: application/json' \
-H 'Authorization: Bearer <TOKEN>'
REQUEST
COLLAPSE ALL
Base URL
https://services.leadconnectorhq.com
Auth
Security Scheme
Agency-Access
Location-Access
Bearer Token
Parameters
userId — path
REQUIRED
Version — header
REQUIRED
---
2021-07-28
SEND API REQUEST
RESPONSE
CLEAR
Click the Send API Request button above and see the response here!