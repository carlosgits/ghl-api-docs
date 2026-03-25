#!/usr/bin/env python3
"""
Scrape entire GHL API documentation via Selenium (renders JS).
Extracts full content, images, and screenshots from each page.
"""

import json
import os
import re
import sys
import time
import hashlib
from pathlib import Path
from urllib.parse import urljoin
from io import BytesIO
from concurrent.futures import ThreadPoolExecutor

if sys.stdout.encoding != "utf-8":
    sys.stdout.reconfigure(encoding="utf-8")

import requests
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from PIL import Image

BASE = "https://marketplace.gohighlevel.com"
OUT_DIR = Path(__file__).parent
IMG_DIR = OUT_DIR / "images"
IMG_DIR.mkdir(exist_ok=True)

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
}


def setup_driver():
    options = Options()
    options.add_argument("--headless=new")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--window-size=1920,1080")
    options.add_argument("--disable-gpu")
    options.add_argument("--disable-extensions")
    driver = webdriver.Chrome(options=options)
    driver.set_page_load_timeout(30)
    return driver


def clean_slug(url):
    """Create a clean filename from URL."""
    slug = url.replace(BASE + "/docs/", "").replace("/", "_").strip("_")
    slug = re.sub(r'[^\w\-]', '_', slug)
    return slug[:120] or "home"


def download_image(img_url, name_prefix, idx):
    """Download an image and save with descriptive name."""
    try:
        resp = requests.get(img_url, headers=HEADERS, timeout=10)
        resp.raise_for_status()
        if len(resp.content) < 500:
            return None

        # Detect extension
        ct = resp.headers.get("content-type", "")
        ext = "png"
        if "jpeg" in ct or "jpg" in ct:
            ext = "jpg"
        elif "gif" in ct:
            ext = "gif"
        elif "webp" in ct:
            ext = "webp"
        elif "svg" in ct:
            ext = "svg"

        # Get dimensions for raster images
        width, height = None, None
        if ext != "svg":
            try:
                img = Image.open(BytesIO(resp.content))
                width, height = img.width, img.height
            except Exception:
                pass

        filename = f"{name_prefix}_{idx:02d}.{ext}"
        filepath = IMG_DIR / filename
        with open(filepath, "wb") as f:
            f.write(resp.content)

        return {
            "src": img_url,
            "local_path": str(filepath),
            "filename": filename,
            "width": width,
            "height": height,
            "size_kb": round(len(resp.content) / 1024, 1),
            "format": ext.upper(),
        }
    except Exception:
        return None


def get_page_content(driver, url):
    """Navigate to a page and extract rendered content + images."""
    try:
        driver.get(url)
    except Exception as e:
        return None

    time.sleep(1.5)

    try:
        WebDriverWait(driver, 8).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "article, main, .markdown"))
        )
    except Exception:
        time.sleep(1.5)

    title = driver.title.replace(" | HighLevel API", "").strip()

    # Extract main content text
    content = ""
    try:
        article = driver.find_element(By.TAG_NAME, "article")
        content = article.text
    except Exception:
        try:
            main = driver.find_element(By.CSS_SELECTOR, "main, .markdown, [class*='docItemCol']")
            content = main.text
        except Exception:
            content = driver.find_element(By.TAG_NAME, "body").text

    # Extract inner HTML for images
    images_data = []
    slug = clean_slug(url)
    try:
        article_el = driver.find_element(By.TAG_NAME, "article")
        img_elements = article_el.find_elements(By.TAG_NAME, "img")

        for idx, img_el in enumerate(img_elements[:15]):
            try:
                src = img_el.get_attribute("src") or img_el.get_attribute("data-src") or ""
                alt = img_el.get_attribute("alt") or ""

                if not src or "svg+xml" in src:
                    continue

                img_url = urljoin(url, src)
                img_info = download_image(img_url, slug, idx)
                if img_info:
                    img_info["alt"] = alt
                    images_data.append(img_info)
            except Exception:
                continue
    except Exception:
        pass

    # Take screenshot
    screenshot_path = str(IMG_DIR / f"{slug}_screenshot.png")
    try:
        driver.save_screenshot(screenshot_path)
    except Exception:
        screenshot_path = None

    return {
        "url": url,
        "title": title,
        "content": content,
        "images": images_data,
        "screenshot": screenshot_path,
    }


def main():
    print("=" * 60)
    print("GHL API Documentation Scraper")
    print("=" * 60)

    # Load URLs
    urls_file = OUT_DIR / "all_urls.json"
    with open(urls_file) as f:
        all_urls = json.load(f)

    print(f"\nTotal URLs to scrape: {len(all_urls)}")

    driver = setup_driver()
    all_docs = []
    errors = []

    try:
        for i, url in enumerate(all_urls):
            slug = clean_slug(url)
            print(f"  [{i+1}/{len(all_urls)}] {slug[:70]}")

            try:
                result = get_page_content(driver, url)
                if result:
                    all_docs.append(result)

                    # Save individual markdown
                    md_path = OUT_DIR / f"{slug}.md"
                    with open(md_path, "w", encoding="utf-8") as f:
                        f.write(f"# {result['title']}\n\n")
                        f.write(f"Source: {result['url']}\n\n")
                        if result['screenshot']:
                            f.write(f"Screenshot: {result['screenshot']}\n\n")
                        if result['images']:
                            f.write("## Images\n\n")
                            for img in result['images']:
                                f.write(f"- ![{img.get('alt', '')}]({img['local_path']}) ")
                                f.write(f"({img.get('width', '?')}x{img.get('height', '?')}, {img['size_kb']}KB)\n")
                            f.write("\n")
                        f.write("---\n\n")
                        f.write(result['content'])

                    # Log images found
                    if result['images']:
                        print(f"    -> {len(result['images'])} images saved")
                else:
                    errors.append(url)
                    print(f"    -> ERROR: No content")

            except Exception as e:
                errors.append(url)
                print(f"    -> ERROR: {str(e)[:60]}")

            # Restart driver every 100 pages to prevent memory issues
            if (i + 1) % 100 == 0:
                print(f"\n  --- Restarting browser (memory cleanup) ---\n")
                driver.quit()
                driver = setup_driver()

    finally:
        driver.quit()

    # Save master JSON
    print(f"\nSaving master documentation...")
    master = OUT_DIR / "ghl_api_full.json"
    with open(master, "w", encoding="utf-8") as f:
        json.dump(all_docs, f, indent=2, ensure_ascii=False)

    # Create index
    index_path = OUT_DIR / "INDEX.md"
    with open(index_path, "w", encoding="utf-8") as f:
        f.write("# GoHighLevel API V2 - Complete Documentation\n\n")
        f.write(f"Total pages scraped: {len(all_docs)}\n")
        f.write(f"Errors: {len(errors)}\n")
        total_imgs = sum(len(d.get('images', [])) for d in all_docs)
        f.write(f"Total images: {total_imgs}\n\n")

        # Group by category
        cats = {}
        for doc in all_docs:
            parts = doc['url'].replace(BASE + "/docs/", "").split("/")
            cat = parts[0] if parts else "root"
            if cat == "ghl" and len(parts) > 1:
                cat = f"ghl/{parts[1]}"
            if cat not in cats:
                cats[cat] = []
            cats[cat].append(doc)

        for cat in sorted(cats):
            f.write(f"\n## {cat} ({len(cats[cat])} pages)\n\n")
            for doc in cats[cat]:
                slug = clean_slug(doc['url'])
                img_count = len(doc.get('images', []))
                content_len = len(doc.get('content', ''))
                img_str = f" - {img_count} imgs" if img_count else ""
                f.write(f"- [{doc['title']}]({slug}.md) ({content_len} chars{img_str})\n")

        if errors:
            f.write(f"\n## Errors ({len(errors)})\n\n")
            for url in errors:
                f.write(f"- {url}\n")

    print(f"\n{'=' * 60}")
    print(f"DONE! {len(all_docs)} pages scraped.")
    print(f"Images: {total_imgs}")
    print(f"Errors: {len(errors)}")
    print(f"Output: {OUT_DIR}")
    print(f"{'=' * 60}")


if __name__ == "__main__":
    main()
