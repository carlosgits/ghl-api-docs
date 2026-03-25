# How to Search This Documentation Efficiently

> This guide is designed for AI agents and developers who need to find any piece of GHL API information fast.

## Repository Structure

```
ghl-api-docs/
├── INDEX.md                  # Master index — START HERE
├── all_urls.json             # All 770 source URLs (JSON array)
├── ghl_api_full.json         # Complete scraped data (JSON, 2.1MB)
├── *.md                      # 770 individual endpoint/topic pages
├── images/
│   ├── *_screenshot.png      # Full-page screenshots (one per page)
│   └── *_00.png, *_01.png    # Inline images extracted from pages
└── browser_scrape.py         # The scraper that generated everything
```

## File Naming Convention

Every filename is a **slug derived from the URL path**, using underscores as separators:

```
URL:  https://marketplace.gohighlevel.com/docs/ghl/contacts/create-contact
File: ghl_contacts_create-contact.md
```

**Pattern:** `{section}_{category}_{endpoint-name}.md`

### Common prefixes and what they map to:

| Prefix | Section | Example |
|--------|---------|---------|
| `ghl_contacts_*` | Contacts API | `ghl_contacts_create-contact.md` |
| `ghl_calendars_*` | Calendars API | `ghl_calendars_create-appointment.md` |
| `ghl_conversations_*` | Conversations API | `ghl_conversations_send-a-new-message.md` |
| `ghl_opportunities_*` | Opportunities/Pipelines | `ghl_opportunities_create-opportunity.md` |
| `ghl_payments_*` | Payments API | `ghl_payments_list-orders.md` |
| `ghl_workflows_*` | Workflows API | `ghl_workflows_get-workflow.md` |
| `ghl_locations_*` | Locations/Sub-Accounts | `ghl_locations_get-location.md` |
| `ghl_oauth_*` | OAuth endpoints | `ghl_oauth_get-access-token.md` |
| `Authorization_*` | Auth concepts & guides | `Authorization_OAuth2_0.md` |
| `marketplace-modules_*` | Marketplace & Custom Actions | `marketplace-modules_CustomActions.md` |

## Search Strategies (Fastest to Slowest)

### 1. Direct File Lookup (instant)

If you know the API category and action, construct the filename directly:

```
# Want "Create Contact"?
→ ghl_contacts_create-contact.md

# Want "Send Message in Conversation"?
→ ghl_conversations_send-a-new-message.md

# Want "List Invoices"?
→ ghl_invoices_list-invoices.md
```

**Rule:** `ghl_{category}_{action-in-kebab-case}.md`

### 2. INDEX.md Scan (fast)

`INDEX.md` lists every page grouped by API category with:
- Page title
- Filename link
- Content length (chars)
- Image count

**Use this when:** you need to browse all endpoints in a category, or you're unsure of the exact endpoint name.

```
# Example: Find all Contacts endpoints
→ Search INDEX.md for "## ghl/contacts"
→ Returns 43 pages with links
```

### 3. Filename Glob (fast)

Search by pattern when you know the category but not the exact endpoint:

```bash
# All calendar endpoints
ghl_calendars_*.md

# All "create" operations across the API
ghl_*_create-*.md

# All "get" operations for contacts
ghl_contacts_get-*.md

# Everything about webhooks
*webhook*.md
```

### 4. Full-Text Content Search (medium)

Search inside markdown files when you need to find:
- Specific field names (e.g., `contactId`, `locationId`)
- HTTP methods and paths (e.g., `POST /contacts/`)
- Response field names or error codes
- Query parameter names

```bash
# Find which endpoints use "pipelineId"
grep -rl "pipelineId" *.md

# Find all POST endpoints
grep -rl "POST" ghl_*.md

# Find rate limit info
grep -rl "rate limit" *.md
```

### 5. JSON Master File (for programmatic access)

`ghl_api_full.json` contains all 770 pages as a JSON array:

```json
[
  {
    "url": "https://marketplace.gohighlevel.com/docs/ghl/contacts/create-contact",
    "title": "Create Contact",
    "content": "full page text...",
    "images": [
      {
        "src": "original_url",
        "local_path": "images/ghl_contacts_create-contact_00.png",
        "filename": "ghl_contacts_create-contact_00.png",
        "alt": "description",
        "width": 800,
        "height": 600,
        "size_kb": 45.2,
        "format": "PNG"
      }
    ],
    "screenshot": "images/ghl_contacts_create-contact_screenshot.png"
  }
]
```

**Use this when:** you need to programmatically process multiple endpoints or build tools on top of the docs.

## Finding Images & Screenshots

### Screenshot naming
Every page has exactly one full-page screenshot:
```
images/{slug}_screenshot.png
```

### Inline image naming
Pages with embedded images (diagrams, flowcharts, UI examples) use sequential numbering:
```
images/{slug}_00.png
images/{slug}_01.png
images/{slug}_02.png
```

### Which pages have images?
Only 65 inline images exist across the 770 pages. The pages with images are flagged in `INDEX.md` with an `- N imgs` suffix:

```
- [OAuth 2.0](Authorization_OAuth2_0.md) (13149 chars - 6 imgs)
```

**Pages with the most images:**
- `Authorization_OAuth2_0.md` — 6 images (OAuth flow diagrams)
- `marketplace-modules_CustomActions.md` — Multiple images (Custom Actions UI)

### To find a specific image
1. Check if the markdown file references it: images are listed under `## Images` in each `.md`
2. Or glob the images folder: `images/{slug}_*.png`

## API Categories Reference (39 total)

| Category | File Prefix | Endpoints |
|----------|-------------|-----------|
| Agent Studio | `ghl_agent-studio_*` | 5 |
| Associations | `ghl_associations_*` | 13 |
| Blogs | `ghl_blogs_*` | 9 |
| Brand Boards | `ghl_brand-boards_*` | 7 |
| Businesses | `ghl_businesses_*` | 7 |
| Calendars | `ghl_calendars_*` | 64 |
| Campaigns | `ghl_campaigns_*` | 3 |
| Companies | `ghl_companies_*` | 3 |
| Contacts | `ghl_contacts_*` | 43 |
| Conversations | `ghl_conversations_*` | 25+ |
| Courses | `ghl_courses_*` | 10+ |
| Custom Fields | `ghl_custom-fields_*` | 10+ |
| Custom Menu Links | `ghl_custom-menu-link_*` | 5+ |
| Custom Values | `ghl_custom-values_*` | 5+ |
| Emails | `ghl_emails_*` | 10+ |
| Forms | `ghl_forms_*` | 10+ |
| Funnels | `ghl_funnels_*` | 10+ |
| Invoices | `ghl_invoices_*` | 15+ |
| Links | `ghl_links_*` | 5+ |
| Locations | `ghl_locations_*` | 20+ |
| Media | `ghl_media_*` | 5+ |
| OAuth | `ghl_oauth_*` | 5+ |
| Opportunities | `ghl_opportunities_*` | 15+ |
| Payments | `ghl_payments_*` | 20+ |
| Products | `ghl_products_*` | 10+ |
| SaaS | `ghl_saas-api_*` | 10+ |
| Snapshots | `ghl_snapshots_*` | 5+ |
| Social Media | `ghl_social-media-posting_*` | 10+ |
| Surveys | `ghl_surveys_*` | 5+ |
| Triggers | `ghl_triggers_*` | 5+ |
| Users | `ghl_users_*` | 10+ |
| Workflows | `ghl_workflows_*` | 5+ |

## Quick Reference: Common Tasks

| I need to... | Search this |
|--------------|-------------|
| Create/update/delete a resource | `ghl_{category}_create-*.md` / `update-*.md` / `delete-*.md` |
| List or get resources | `ghl_{category}_get-*.md` / `list-*.md` |
| Understand authentication | `Authorization_*.md` |
| See webhook payloads | `category_webhook.md` + `*webhook*.md` |
| Find required scopes | `Authorization_Scopes.md` |
| See the full OpenAPI spec | `ghl_api_full.json` |
| Browse all endpoints in a category | `INDEX.md` → search for category heading |
| Find a specific field or parameter | Full-text search across `*.md` files |
| See visual UI reference | `images/{slug}_screenshot.png` |
