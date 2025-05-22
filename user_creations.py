from playwright.sync_api import sync_playwright


BASE_URL = "https://mr-3909-earthling-books.pantheonsite.io/"
ABA_USERNAME = "aba_administrator@example.com"
ABA_PASSWORD = "wyfavf4TCG7nhj9ckp3"


def launch_and_login(playwright):
    browser = playwright.chromium.launch(headless=False, slow_mo=500)
    page = browser.new_page()
    page.goto(BASE_URL)
    page.click("//a[@title='Log in']")
    page.click("#edit-name")
    page.fill("#edit-name", ABA_USERNAME)
    page.fill("#edit-pass", ABA_PASSWORD)
    page.click("#edit-submit")
    page.click("//a[@title='Dashboard']")
    return browser, page


def siteadmin_operations(playwright):
    browser, page = launch_and_login(playwright)
    page.click("//a[text()='Users']")
    page.click("//a[text()='Add user']")
    page.fill("#edit-mail", "aravi+sa1@fleetstudio.com")
    page.fill("#edit-pass-pass1", "Fleet@1994")
    page.fill("#edit-pass-pass2", "Fleet@1994")
    page.click("//label[text()='Site Administrator']")
    page.click("//label[@for='edit-terms-of-use']")
    page.press("#edit-submit", "Enter")
    close_browser(browser)


def Content_editor_operations(playwright):
    browser, page = launch_and_login(playwright)
    page.click("//a[text()='Users']")
    page.click("//a[text()='Add user']")
    page.fill("#edit-mail", "aravi+ce1@fleetstudio.com")
    page.fill("#edit-pass-pass1", "Fleet@1994")
    page.fill("#edit-pass-pass2", "Fleet@1994")
    page.click("//label[text()='Content Editor']")
    page.click("//label[@for='edit-terms-of-use']")
    page.press("#edit-submit", "Enter")
    close_browser(browser)


def order_manager_operations(playwright):
    browser, page = launch_and_login(playwright)
    page.click("//a[text()='Users']")
    page.click("//a[text()='Add user']")
    page.fill("#edit-mail", "aravi+odman1@fleetstudio.com")
    page.fill("#edit-pass-pass1", "Fleet@1994")
    page.fill("#edit-pass-pass2", "Fleet@1994")
    page.click("//label[text()='Order Manager']")
    page.click("//label[@for='edit-terms-of-use']")
    page.press("#edit-submit", "Enter")
    close_browser(browser)


def blog_author_operations(playwright):
    browser, page = launch_and_login(playwright)
    page.click("//a[text()='Users']")
    page.click("//a[text()='Add user']")
    page.fill("#edit-mail", "aravi+ba1@fleetstudio.com")
    page.fill("#edit-pass-pass1", "Fleet@1994")
    page.fill("#edit-pass-pass2", "Fleet@1994")
    page.click("//label[text()='Blog Author']")
    page.click("//label[@for='edit-terms-of-use']")
    page.press("#edit-submit", "Enter")
    close_browser(browser)


def customer_operations(playwright):
    browser, page = launch_and_login(playwright)
    page.click("//a[text()='Users']")
    page.click("//a[text()='Add user']")
    page.fill("#edit-mail", "aravi+customer1@fleetstudio.com")
    page.fill("#edit-pass-pass1", "Fleet@1994")
    page.fill("#edit-pass-pass2", "Fleet@1994")
    page.click("//label[text()='Customer']")
    page.click("//label[@for='edit-terms-of-use']")
    page.press("#edit-submit", "Enter")
    close_browser(browser)


def close_browser(browser):
    browser.close()


if __name__ == "__main__":
    with sync_playwright() as playwright:
        siteadmin_operations(playwright)
        Content_editor_operations(playwright)
        order_manager_operations(playwright)
        blog_author_operations(playwright)
        customer_operations(playwright)
