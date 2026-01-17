from playwright.sync_api import sync_playwright
import time

class BrowserAgent:
    def __init__(self, headless=False):
        self.p = sync_playwright().start()
        self.browser = self.p.chromium.launch(headless=headless)
        self.page = self.browser.new_page()

    def open(self, url):
        if not url.startswith("http"):
            url = "https://" + url
        self.page.goto(url)

    def type(self, selector, text):
        self.page.fill(selector, text)

    def press(self, key):
        self.page.keyboard.press(key)

    def click(self, selector):
        self.page.wait_for_selector(selector, timeout=15000)
        self.page.click(selector)

    def extract(self, selector_list, attribute="innerText", timeout=15000):
        # Accepts list of selectors for robustness
        results = []
        for selector in selector_list:
            try:
                self.page.wait_for_selector(selector, timeout=timeout)
                elements = self.page.query_selector_all(selector)
                for el in elements:
                    if attribute == "innerText":
                        results.append(el.inner_text())
                    else:
                        results.append(el.get_attribute(attribute))
                if results:
                    break  # stop at first matching selector with content
            except:
                continue
        return results

    def close(self):
        self.browser.close()
        self.p.stop()
