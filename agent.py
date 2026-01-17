import json
import time
from agent_planner import generate_plan
from browser_agent import BrowserAgent

task = "Search for Python latest version and extract top 3 results content"
actions_text = generate_plan(task)
print("Generated JSON PLAN:\n", actions_text)

# Convert LLM output to Python objects
actions = actions_text  # ensure LLM outputs a list of JSON steps

browser = BrowserAgent(headless=False)

all_extracted = []

for step in actions:
    action_type = step.get("type")
    print(f"\nEXECUTING STEP: {step}")

    if action_type == "OPEN":
        url = step.get("url")
        browser.open(url)
        time.sleep(2)

    elif action_type == "TYPE":
        selector = step.get("selector")
        value = step.get("value")
        browser.type(selector, value)
        time.sleep(1)

    elif action_type == "PRESS":
        key = step.get("value")
        browser.press(key)
        time.sleep(2)  # wait for results to load

    elif action_type == "EXTRACT":
        selectors = step.get("selector_list") or [step.get("selector")]
        attr = step.get("attribute", "innerText")
        extracted = []
        for sel in selectors:
            try:
                elements = browser.page.query_selector_all(sel)
                for el in elements:
                    val = el.get_attribute(attr) if attr != "innerText" else el.inner_text()
                    if val:
                        extracted.append(val)
            except Exception as e:
                continue
        print("EXTRACTED DATA:", extracted)
        all_extracted.extend(extracted)

    elif action_type == "CLICK":
        sel = step.get("selector")
        try:
            el = browser.page.query_selector(sel)
            if el:
                el.click()
                time.sleep(3)  # wait for page load
        except Exception as e:
            print("CLICK failed:", e)

    elif action_type == "DONE":
        print("Task completed.")

# Multi-link handling: open top N links and extract paragraphs
top_links = all_extracted[:3]  # take first 3 links
multi_content = []

for url in top_links:
    print(f"\nOpening {url}")
    try:
        browser.open(url)
        time.sleep(3)
        # wait for main content to load
        try:
            browser.page.wait_for_selector("main, article, div", timeout=10000)
        except:
            pass

        page_paragraphs = []
        selectors = ['p', 'article p', 'div p', 'main p', 'span', 'div[class*="content"]']
        for sel in selectors:
            try:
                elements = browser.page.query_selector_all(sel)
                for el in elements:
                    text = el.inner_text().strip()
                    if text:
                        page_paragraphs.append(text)
            except:
                continue

        print(f"Extracted {len(page_paragraphs)} paragraphs from {url}")
        multi_content.append({"url": url, "content": page_paragraphs})

    except Exception as e:
        print(f"Failed to open {url}: {e}")

# Save all content
with open("multi_extracted_results.json", "w", encoding="utf-8") as f:
    json.dump(multi_content, f, ensure_ascii=False, indent=2)

browser.close()
print("\nAll extracted content saved to multi_extracted_results.json")
