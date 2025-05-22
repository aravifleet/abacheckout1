from playwright.sync_api import sync_playwright


class BasePage:
    BASE_URL = "https://dev-sourcetax1708102111.pantheonsite.io/"
    ABA_USERNAME = "ssanguraj+sa@fleetstudio.com"
    ABA_PASSWORD = "King@1997$"

    def __init__(self, playwright):
        self.browser = playwright.chromium.launch(headless=False)
        self.page = self.browser.new_page()

    def go_to_home(self):
        self.page.goto(self.BASE_URL)

    def close_browser(self):
        self.browser.close()
