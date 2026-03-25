# How to Build an API Documentation Scraper

> A complete guide to building scrapers that produce well-organized, AI-searchable documentation with screenshots and properly named files — based on the scraper that generated this repository.

## What This Scraper Achieved

- 770 markdown pages from a JavaScript-rendered documentation site
- 834 images (65 inline + 769 full-page screenshots)
- Consistent naming convention across all files
- A master JSON file for programmatic access
- An auto-generated INDEX.md for browsing
- Zero errors across all 770 pages

## Architecture Overview

```
┌─────────────────┐     ┌──────────────┐     ┌─────────────────┐
│  URL Discovery   │────▶│  Page Render  │────▶│  Content Extract │
│  (all_urls.json) │     │  (Selenium)   │     │  (text + images) │
└─────────────────┘     └──────────────┘     └────────┬────────┘
                                                       │
                                    ┌──────────────────┼──────────────────┐
                                    ▼                  ▼                  ▼
                              ┌──────────┐     ┌─────────────┐    ┌───────────┐
                              │ Markdown  │     │ Screenshots │    │ Master    │
                              │ per page  │     │ per page    │    │ JSON +    │
                              │ (.md)     │     │ (.png)      │    │ INDEX.md  │
                              └──────────┘     └─────────────┘    └───────────┘
```

## Step-by-Step: Building Your Own

### Step 1: URL Discovery

Before scraping, you need a complete list of every page to visit. There are several approaches:

#### Option A: Sitemap (easiest)
```python
import requests
import xml.etree.ElementTree as ET

resp = requests.get("https://example.com/sitemap.xml")
root = ET.fromstring(resp.content)
urls = [loc.text for loc in root.iter("{http://www.sitemaps.org/schemas/sitemap/0.9}loc")]
```

#### Option B: Crawl navigation links (what we used)
Navigate to the docs index, extract all sidebar/nav links:
```python
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://docs.example.com")

links = driver.find_elements(By.CSS_SELECTOR, "nav a, .sidebar a, [class*='menu'] a")
urls = list(set(a.get_attribute("href") for a in links if a.get_attribute("href")))
```

#### Option C: API index endpoint
Some documentation platforms expose a manifest or search index:
```python
# Docusaurus sites often have:
resp = requests.get("https://docs.example.com/search-index.json")
urls = [item["url"] for item in resp.json()]
```

**Save the URL list to a JSON file** — this lets you restart the scraper without re-crawling:
```python
import json
with open("all_urls.json", "w") as f:
    json.dump(sorted(urls), f, indent=2)
```

### Step 2: Set Up Selenium for JS-Rendered Sites

Most modern documentation sites (Docusaurus, GitBook, ReadMe, etc.) render content with JavaScript. Plain `requests` won't work — you need a real browser.

```python
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

def setup_driver():
    options = Options()
    options.add_argument("--headless=new")        # Headless Chrome
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--window-size=1920,1080")  # Full HD for screenshots
    options.add_argument("--disable-gpu")
    driver = webdriver.Chrome(options=options)
    driver.set_page_load_timeout(30)
    return driver
```

**Requirements:**
```bash
pip install selenium requests Pillow
```
You also need ChromeDriver installed and matching your Chrome version.

### Step 3: The File Naming System

This is **critical** for searchability. The naming convention must be:
1. **Deterministic** — given a URL, you can predict the filename without looking it up
2. **Hierarchical** — the category/section is visible in the name
3. **Consistent** — same rules for every file, no exceptions

#### The slug function:

```python
import re

BASE_URL = "https://docs.example.com/docs/"

def clean_slug(url):
    """Convert URL path to a clean, predictable filename slug."""
    # Strip the base URL to get just the path
    slug = url.replace(BASE_URL, "").replace("/", "_").strip("_")
    # Replace non-alphanumeric chars (except hyphens and underscores)
    slug = re.sub(r'[^\w\-]', '_', slug)
    # Truncate to prevent filesystem issues
    return slug[:120] or "home"
```

**Examples of what this produces:**

| URL Path | Slug | Filename |
|----------|------|----------|
| `/docs/ghl/contacts/create-contact` | `ghl_contacts_create-contact` | `ghl_contacts_create-contact.md` |
| `/docs/Authorization/OAuth2.0` | `Authorization_OAuth2_0` | `Authorization_OAuth2_0.md` |
| `/docs/ghl/calendars/get-slots` | `ghl_calendars_get-slots` | `ghl_calendars_get-slots.md` |

#### Image naming follows the same slug + index:

```
{slug}_00.png      # First inline image
{slug}_01.png      # Second inline image
{slug}_screenshot.png  # Full-page screenshot
```

This means **every image is traceable back to its source page** just by reading the filename.

### Step 4: Content Extraction

For each URL, extract three things: text, images, and a screenshot.

```python
from io import BytesIO
from PIL import Image
import requests
import time

HEADERS = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"}

def get_page_content(driver, url):
    """Navigate to page and extract everything."""
    driver.get(url)
    time.sleep(1.5)  # Let JS render

    # Wait for main content to appear
    try:
        WebDriverWait(driver, 8).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "article, main, .markdown"))
        )
    except Exception:
        time.sleep(1.5)  # Fallback wait

    # --- TITLE ---
    title = driver.title.replace(" | Site Name", "").strip()

    # --- TEXT CONTENT ---
    # Try specific selectors first, fall back to broader ones
    content = ""
    for selector in ["article", "main", ".markdown", "[class*='docItemCol']"]:
        try:
            el = driver.find_element(By.CSS_SELECTOR, selector)
            content = el.text
            break
        except Exception:
            continue
    if not content:
        content = driver.find_element(By.TAG_NAME, "body").text

    # --- IMAGES ---
    slug = clean_slug(url)
    images = extract_images(driver, url, slug)

    # --- SCREENSHOT ---
    screenshot_path = f"images/{slug}_screenshot.png"
    driver.save_screenshot(screenshot_path)

    return {
        "url": url,
        "title": title,
        "content": content,
        "images": images,
        "screenshot": screenshot_path,
    }
```

### Step 5: Image Download with Metadata

Don't just save images — capture metadata (dimensions, format, size) so they're useful later:

```python
def download_image(img_url, name_prefix, idx):
    """Download image with metadata for AI searchability."""
    try:
        resp = requests.get(img_url, headers=HEADERS, timeout=10)
        resp.raise_for_status()

        # Skip tiny images (icons, spacers, tracking pixels)
        if len(resp.content) < 500:
            return None

        # Detect format from content-type
        ct = resp.headers.get("content-type", "")
        ext = "png"
        for fmt, key in [("jpg", "jpeg"), ("jpg", "jpg"), ("gif", "gif"),
                         ("webp", "webp"), ("svg", "svg")]:
            if key in ct:
                ext = fmt
                break

        # Get dimensions (skip for SVG)
        width, height = None, None
        if ext != "svg":
            try:
                img = Image.open(BytesIO(resp.content))
                width, height = img.width, img.height
            except Exception:
                pass

        # Save with predictable name
        filename = f"{name_prefix}_{idx:02d}.{ext}"
        filepath = f"images/{filename}"
        with open(filepath, "wb") as f:
            f.write(resp.content)

        return {
            "src": img_url,
            "local_path": filepath,
            "filename": filename,
            "alt": "",  # Set by caller from img element
            "width": width,
            "height": height,
            "size_kb": round(len(resp.content) / 1024, 1),
            "format": ext.upper(),
        }
    except Exception:
        return None


def extract_images(driver, page_url, slug):
    """Find and download all meaningful images from the page."""
    from urllib.parse import urljoin

    images_data = []
    try:
        article = driver.find_element(By.TAG_NAME, "article")
        img_elements = article.find_elements(By.TAG_NAME, "img")

        for idx, img_el in enumerate(img_elements[:15]):  # Cap at 15 per page
            src = img_el.get_attribute("src") or img_el.get_attribute("data-src") or ""
            alt = img_el.get_attribute("alt") or ""

            if not src or "svg+xml" in src:  # Skip inline SVG data URIs
                continue

            img_url = urljoin(page_url, src)
            img_info = download_image(img_url, slug, idx)
            if img_info:
                img_info["alt"] = alt
                images_data.append(img_info)
    except Exception:
        pass

    return images_data
```

### Step 6: Generate Clean Markdown

Each page gets its own markdown file. Structure it for maximum searchability:

```python
def save_markdown(result, output_dir):
    """Save a single page as a well-structured markdown file."""
    slug = clean_slug(result["url"])
    filepath = f"{output_dir}/{slug}.md"

    with open(filepath, "w", encoding="utf-8") as f:
        # Title as H1 — searchable
        f.write(f"# {result['title']}\n\n")

        # Source URL — for verification and linking back
        f.write(f"Source: {result['url']}\n\n")

        # Screenshot reference
        if result.get("screenshot"):
            f.write(f"Screenshot: {result['screenshot']}\n\n")

        # Images section with metadata
        if result.get("images"):
            f.write("## Images\n\n")
            for img in result["images"]:
                alt = img.get("alt", "")
                f.write(f"- ![{alt}]({img['local_path']})")
                f.write(f" ({img.get('width', '?')}x{img.get('height', '?')}, {img['size_kb']}KB)\n")
            f.write("\n")

        # Separator before main content
        f.write("---\n\n")

        # Full text content — this is what gets searched
        f.write(result["content"])
```

### Step 7: Memory-Safe Scraping Loop

For large documentation sites (hundreds of pages), restart the browser periodically to prevent memory leaks:

```python
def main():
    import json

    with open("all_urls.json") as f:
        urls = json.load(f)

    driver = setup_driver()
    all_docs = []
    errors = []

    try:
        for i, url in enumerate(urls):
            slug = clean_slug(url)
            print(f"  [{i+1}/{len(urls)}] {slug[:70]}")

            try:
                result = get_page_content(driver, url)
                if result:
                    all_docs.append(result)
                    save_markdown(result, ".")
                else:
                    errors.append(url)
            except Exception as e:
                errors.append(url)
                print(f"    -> ERROR: {str(e)[:60]}")

            # CRITICAL: Restart browser every 100 pages to prevent memory bloat
            if (i + 1) % 100 == 0:
                print(f"\n  --- Restarting browser (memory cleanup) ---\n")
                driver.quit()
                driver = setup_driver()

    finally:
        driver.quit()

    # Save master JSON
    with open("ghl_api_full.json", "w", encoding="utf-8") as f:
        json.dump(all_docs, f, indent=2, ensure_ascii=False)

    # Generate INDEX.md
    generate_index(all_docs, errors)
```

### Step 8: Auto-Generate the INDEX.md

The index is the most important file for discovery. Group pages by category:

```python
def generate_index(all_docs, errors):
    """Create a browseable index grouped by API category."""
    # Group by category extracted from URL
    categories = {}
    for doc in all_docs:
        parts = doc["url"].replace(BASE_URL, "").split("/")
        cat = parts[0] if parts else "root"
        # For nested categories like ghl/contacts
        if cat == "ghl" and len(parts) > 1:
            cat = f"ghl/{parts[1]}"
        categories.setdefault(cat, []).append(doc)

    with open("INDEX.md", "w", encoding="utf-8") as f:
        f.write("# API Documentation Index\n\n")
        f.write(f"Total pages: {len(all_docs)}\n")
        f.write(f"Errors: {len(errors)}\n")
        total_imgs = sum(len(d.get("images", [])) for d in all_docs)
        f.write(f"Total images: {total_imgs}\n\n")

        for cat in sorted(categories):
            f.write(f"\n## {cat} ({len(categories[cat])} pages)\n\n")
            for doc in categories[cat]:
                slug = clean_slug(doc["url"])
                img_count = len(doc.get("images", []))
                content_len = len(doc.get("content", ""))
                img_str = f" - {img_count} imgs" if img_count else ""
                f.write(f"- [{doc['title']}]({slug}.md) ({content_len} chars{img_str})\n")

        if errors:
            f.write(f"\n## Errors ({len(errors)})\n\n")
            for url in errors:
                f.write(f"- {url}\n")
```

## Best Practices & Lessons Learned

### Naming
- **Use URL-derived slugs** — makes filenames predictable and reversible
- **Underscores for path separators**, hyphens preserved from original URLs
- **Images share their parent page's slug** + sequential index
- **Screenshots always end in `_screenshot.png`** — easy to glob

### Content Quality
- **Wait for JS rendering** — `time.sleep(1.5)` + WebDriverWait combo catches most cases
- **Target `<article>` first** — avoids capturing nav, footer, sidebar noise
- **Skip images under 500 bytes** — filters out tracking pixels and spacers
- **Cap images at 15 per page** — prevents infinite galleries from bloating storage

### Reliability
- **Restart browser every 100 pages** — Chrome leaks memory in headless mode
- **Set page load timeout** — prevents hanging on slow pages
- **Try/except everything** — one bad page shouldn't kill the whole run
- **Save URL list separately** — lets you resume or re-scrape without re-crawling

### Output Quality
- **One markdown per page** — granular, searchable, git-friendly
- **Master JSON file** — enables programmatic access and building tools
- **INDEX.md with metadata** — character counts and image counts help prioritize reading
- **Source URLs in every file** — always verifiable against the original

## Adapting to Other Documentation Sites

| Site Type | Content Selector | Notes |
|-----------|-----------------|-------|
| Docusaurus | `article`, `.markdown` | Most GHL-style sites use this |
| GitBook | `.page-inner`, `main` | May need to handle iframes |
| ReadMe.io | `.content-body`, `article` | API explorer sections render late |
| Swagger/OpenAPI UI | `.swagger-ui`, `.opblock` | Consider using the JSON spec directly |
| MkDocs | `article`, `.md-content` | Usually simpler, less JS |
| Custom React | `main`, `#content` | Inspect and find the right selector |

## Complete Requirements

```bash
pip install selenium requests Pillow
```

- Python 3.8+
- Chrome browser installed
- ChromeDriver matching your Chrome version (or use `webdriver-manager`):
  ```bash
  pip install webdriver-manager
  ```
  ```python
  from selenium.webdriver.chrome.service import Service
  from webdriver_manager.chrome import ChromeDriverManager
  driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
  ```

## Output Checklist

After running your scraper, verify you have:

- [ ] `all_urls.json` — complete URL list
- [ ] One `.md` file per page with title, source URL, and content
- [ ] `images/` folder with `{slug}_screenshot.png` for every page
- [ ] `images/` folder with `{slug}_{NN}.{ext}` for inline images
- [ ] `INDEX.md` grouped by category with page counts and image counts
- [ ] Master JSON file with all data for programmatic access
- [ ] Zero (or near-zero) errors
