# Getting Started with HighLevel SDKs

Source: https://marketplace.gohighlevel.com/docs/sdk/GettingStartedSDK

Screenshot: C:\Users\carlo\OneDrive\Desktop\Proyectos\ghl-api-docs\images\sdk_GettingStartedSDK_screenshot.png

---

SDK Overview
Getting Started with HighLevel SDKs
HighLevel now ships official SDKs for Node.js, Python, and PHP so you can stop hand-rolling API calls. All three clients deliver the same core features—automatic OAuth flows, PIT support, per-location token storage, webhook helpers, auto refresh tokens and typed service methods—so pick the runtime that matches your stack.
Pick your language
SDK Package Minimum runtime Deep dive
Node.js @gohighlevel/api-client Node.js 18+ Node guide
Python gohighlevel-api-client Python 3.8+ Python guide
PHP gohighlevel/api-client PHP 7.4+ PHP guide
Installation quick reference
Node.js
Python
PHP
npm install @gohighlevel/api-client
# or
yarn add @gohighlevel/api-client
# or
pnpm add @gohighlevel/api-client
Read the Node guide when you are ready.




What you get out of the box
Auto token rotation – refresh happens transparently once storage is configured.
Webhook utilities – signature validation plus automatic handling of webhook events (INSTALL and UNINSTALL).
Token for bulk installation – if webhook is used, it will generate token for each location in which app is installed and store it in the db
Share your feedback
★
★
★
★
★