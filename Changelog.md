# Changelog

Source: https://marketplace.gohighlevel.com/docs/Changelog

Screenshot: C:\Users\carlo\OneDrive\Desktop\Proyectos\ghl-api-docs\images\Changelog_screenshot.png

---

Changelog
Changelog
2025-08-26
Conversations:
Added:
response body field chatWidgetId added in getMessage method (optional)
response body array item field messages.messages[].chatWidgetId added in getMessages method (optional)
Marketplace:
Added:
request body field price added in charge method (optional)
Modified:
method getInstallerDetails endpoint changed from GET /marketplace/app/{appId}/installer-details to GET /marketplace/app/{appId}/installations
Users:
Added:
path param userId is added in getUser method (required)