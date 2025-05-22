import re
import os
from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=True, slow_mo=500)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://mr-3902-earthling-books.pantheonsite.io/")
    print("Current URL is:", page.url)
    page.get_by_role("link", name="Log in").click()
    page.get_by_role("textbox", name="Email").click()
    page.get_by_role("textbox", name="Email").fill("aravi+siteadmin1@fleetstudio.com")
    page.get_by_role("textbox", name="Email").press("Tab")
    page.get_by_role("textbox", name="Password").fill("Fleet@1994")
    page.get_by_role("button", name="Login").click()
    print("Current URL is:", page.url)
    page.get_by_role("link", name="Da Dashboard").click()
    page.locator("#block-claro-storemanagement").get_by_role(
        "link", name="Menu"
    ).click()
    print("Current URL is:", page.url)
    if (
        page.locator("h1.page-title").inner_text().strip()
        != "Edit menu Main navigation"
    ):
        page.screenshot(path="Menu_screenshot.png", full_page=False)
    page.get_by_role("link", name="Da Dashboard").click()
    page.locator("#block-claro-storemanagement").get_by_role(
        "link", name="Content"
    ).click()
    print("Current URL is:", page.url)
    if page.locator("h1.page-title").inner_text().strip() != "Content":
        page.screenshot(path="Content_screenshot.png", full_page=False)
    page.get_by_role("link", name="Da Dashboard").click()
    page.locator("#block-claro-storemanagement").get_by_role(
        "link", name="Media"
    ).click()
    print("Current URL is:", page.url)
    if page.locator("h1.page-title").inner_text().strip() != "Media":
        page.screenshot(path="Media_screenshot.png", full_page=False)
    page.get_by_role("link", name="Da Dashboard").click()
    page.locator("#block-claro-storemanagement").get_by_role(
        "link", name="Events"
    ).click()
    print("Current URL is:", page.url)
    if page.locator("h1.page-title").inner_text().strip() != "Events":
        page.screenshot(path="Events_screenshot.png", full_page=False)
    page.get_by_role("link", name="Da Dashboard").click()
    page.locator("#block-claro-storemanagement").get_by_role(
        "link", name="Event Tags"
    ).click()
    print("Current URL is:", page.url)
    if page.locator("h1.page-title").inner_text().strip() != "Event tag":
        page.screenshot(path="EventTags_screenshot.png", full_page=False)
    page.get_by_role("link", name="Da Dashboard").click()
    page.get_by_role("link", name="Saved Event Locations").click()
    print("Current URL is:", page.url)
    if page.locator("h1.page-title").inner_text().strip() != "Saved Event Locations":
        page.screenshot(path="Saved_Event_Locations_screenshot.png", full_page=False)
    page.get_by_role("link", name="Da Dashboard").click()
    page.locator("#block-claro-storemanagement").get_by_role(
        "link", name="Site Alerts / Announcements"
    ).click()
    print("Current URL is:", page.url)
    if (
        page.locator("h1.page-title").inner_text().strip()
        != "Manage Site Alerts / Announcements"
    ):
        page.screenshot(
            path="Manage_Site_Alerts_Announcements_screenshot.png", full_page=False
        )
    page.get_by_role("link", name="Da Dashboard").click()
    page.locator("#block-claro-storemanagement").get_by_role(
        "link", name="Staff Review Tags"
    ).click()
    print("Current URL is:", page.url)
    if page.locator("h1.page-title").inner_text().strip() != "Staff Review Tags":
        page.screenshot(path="Staff_Reviews_Tags_screenshot.png", full_page=False)
    page.get_by_role("link", name="Da Dashboard").click()
    page.locator("#block-claro-storemanagement").get_by_role(
        "link", name="Wishlists / Gift Registries"
    ).click()
    print("Current URL is:", page.url)
    if page.locator("h1.page-title").inner_text().strip() != "Wishlists":
        page.screenshot(path="Wishlists_screenshot.png", full_page=False)
    page.get_by_role("link", name="Da Dashboard").click()
    page.locator("#block-claro-storemanagement").get_by_role(
        "link", name="Webforms"
    ).click()
    print("Current URL is:", page.url)
    if page.locator("h1.page-title").inner_text().strip() != "Webforms: Submissions":
        page.screenshot(path="Webforms:_Submissions_screenshot.png", full_page=False)
    page.get_by_role("link", name="Da Dashboard").click()
    page.locator("#block-claro-storemanagement").get_by_role(
        "link", name="Users"
    ).click()
    print("Current URL is:", page.url)
    if page.locator("h1.page-title").inner_text().strip() != "People":
        page.screenshot(path="People_screenshot.png", full_page=False)
    page.get_by_role("link", name="Da Dashboard").click()
    page.locator("#block-claro-storemanagement").get_by_role(
        "link", name="Redirects"
    ).click()
    print("Current URL is:", page.url)
    if page.locator("h1.page-title").inner_text().strip() != "Redirect":
        page.screenshot(path="Redirect_screenshot.png", full_page=False)
    page.get_by_role("link", name="Da Dashboard").click()
    page.locator("#block-claro-createcontent").get_by_role(
        "link", name="Product", exact=True
    ).click()
    print("Current URL is:", page.url)
    if page.locator("h1.page-title").inner_text().strip() != "Add product":
        page.screenshot(path="Add_product_screenshot.png", full_page=False)
    page.get_by_role("link", name="Da Dashboard").click()
    page.locator("#block-claro-createcontent").get_by_role(
        "link", name="Product List"
    ).click()
    print("Current URL is:", page.url)
    if page.locator("h1.page-title").inner_text().strip() != "Create Product List":
        page.screenshot(path="Create_Product_List_screenshot.png", full_page=False)
    page.get_by_role("link", name="Da Dashboard").click()
    page.locator("#block-claro-createcontent").get_by_role(
        "link", name="Page", exact=True
    ).click()
    print("Current URL is:", page.url)
    if page.locator("h1.page-title").inner_text().strip() != "Create Page":
        page.screenshot(path="Create_Page_screenshot.png", full_page=False)
    page.get_by_role("link", name="Da Dashboard").click()
    page.locator("#block-claro-createcontent").get_by_role(
        "link", name="Landing Page"
    ).click()
    print("Current URL is:", page.url)
    if page.locator("h1.page-title").inner_text().strip() != "Create Landing Page":
        page.screenshot(path="Create_Landing_Page_screenshot.png", full_page=False)
    page.get_by_role("link", name="Da Dashboard").click()
    page.locator("#block-claro-createcontent").get_by_role("link", name="Event").click()
    if page.locator("h1.page-title").inner_text().strip() != "Create New Event":
        page.screenshot(path="Create_New_Event_screenshot.png", full_page=False)
    page.get_by_role("link", name="Da Dashboard").click()
    page.locator("#block-claro-createcontent").get_by_role(
        "link", name="Staff Review"
    ).click()
    print("Current URL is:", page.url)
    if page.locator("h1.page-title").inner_text().strip() != "Create Staff Review":
        page.screenshot(path="Create_Staff_Review_screenshot.png", full_page=False)
    page.get_by_role("link", name="Da Dashboard").click()
    page.locator("#block-claro-createcontent").get_by_role(
        "link", name="Catalog"
    ).click()
    print("Current URL is:", page.url)
    if page.locator("h1.page-title").inner_text().strip() != "Create Catalog":
        page.screenshot(path="Create_Catalog_screenshot.png", full_page=False)
    page.get_by_role("link", name="Da Dashboard").click()
    page.locator("#block-claro-createcontent").get_by_role(
        "link", name="Webform"
    ).click()
    print("Current URL is:", page.url)
    if page.locator("h1.page-title").inner_text().strip() != "Webforms":
        page.screenshot(path="Webforms_screenshot.png", full_page=False)
    page.get_by_role("link", name="Da Dashboard").click()
    page.locator("#block-claro-commercemanagement").get_by_role(
        "link", name="E-commerce Settings"
    ).click()
    print("Current URL is:", page.url)
    if page.locator("h1.page-title").inner_text().strip() != "E-commerce Settings":
        page.screenshot(path="Ecommerce_Settings_screenshot.png", full_page=False)
    page.get_by_role("link", name="Da Dashboard").click()
    page.locator("#block-claro-commercemanagement").get_by_role(
        "link", name="Fulfillment Settings"
    ).click()
    print("Current URL is:", page.url)
    if page.locator("h1.page-title").inner_text().strip() != "Fulfillment Settings":
        page.screenshot(path="Fulfillment_Settings_screenshot.png", full_page=False)
    page.get_by_role("link", name="Da Dashboard").click()
    page.locator("#block-claro-commercemanagement").get_by_role(
        "link", name="Pricing by ISBN"
    ).click()
    print("Current URL is:", page.url)
    if page.locator("h1.page-title").inner_text().strip() != "Bulk Price Update":
        page.screenshot(path="BulkPriceUpdate_screenshot.png", full_page=False)
    page.get_by_role("link", name="Da Dashboard").click()
    page.locator("#block-claro-commercemanagement").get_by_role(
        "link", name="Local Store Inventory"
    ).click()
    print("Current URL is:", page.url)
    if page.locator("h1.page-title").inner_text().strip() != "LSI Upload":
        page.screenshot(path="LSI_Upload_screenshot.png", full_page=False)
    page.get_by_role("link", name="Da Dashboard").click()
    page.locator("#block-claro-commercemanagement").get_by_role(
        "link", name="Products"
    ).click()
    print("Current URL is:", page.url)
    if page.locator("h1.page-title").inner_text().strip() != "Products":
        page.screenshot(path="Products_screenshot.png", full_page=False)
    page.get_by_role("link", name="Da Dashboard").click()
    page.locator("#block-claro-commercemanagement").get_by_role(
        "link", name="Product Attributes"
    ).click()
    print("Current URL is:", page.url)
    if page.locator("h1.page-title").inner_text().strip() != "Product attributes":
        page.screenshot(path="Product_attributes_screenshot.png", full_page=False)
    page.get_by_role("link", name="Da Dashboard").click()
    page.locator("#block-claro-commercemanagement").get_by_role(
        "link", name="Product Categories"
    ).click()
    print("Current URL is:", page.url)
    if page.locator("h1.page-title").inner_text().strip() != "Product Category":
        page.screenshot(path="ProductCategory_screenshot.png", full_page=False)
    page.get_by_role("link", name="Da Dashboard").click()
    page.locator("#block-claro-commercemanagement").get_by_role(
        "link", name="Gift Cards"
    ).click()
    print("Current URL is:", page.url)
    if page.locator("h1.page-title").inner_text().strip() != "Gift Cards":
        page.screenshot(path="GiftCards_screenshot.png", full_page=False)
    page.get_by_role("link", name="Da Dashboard").click()
    page.locator("#block-claro-commercemanagement").get_by_role(
        "link", name="Services"
    ).click()
    print("Current URL is:", page.url)
    if page.locator("h1.page-title").inner_text().strip() != "Services":
        page.screenshot(path="Services_screenshot.png", full_page=False)
    page.get_by_role("link", name="Da Dashboard").click()
    page.locator("#block-claro-commercemanagement").get_by_role(
        "link", name="Service Categories"
    ).click()
    print("Current URL is:", page.url)
    if page.locator("h1.page-title").inner_text().strip() != "Service Category":
        page.screenshot(path="Service_Category_screenshot.png", full_page=False)
    page.get_by_role("link", name="Da Dashboard").click()
    page.locator("#block-claro-commercemanagement").get_by_role(
        "link", name="Promotions & Coupons"
    ).click()
    print("Current URL is:", page.url)
    if page.locator("h1.page-title").inner_text().strip() != "Promotions":
        page.screenshot(path="Promotions_screenshot.png", full_page=False)
    page.get_by_role("link", name="Da Dashboard").click()
    page.locator("#block-claro-commercemanagement").get_by_role(
        "link", name="Order Tags"
    ).click()
    print("Current URL is:", page.url)
    if page.locator("h1.page-title").inner_text().strip() != "Order Tag":
        page.screenshot(path="OrderTag_screenshot.png", full_page=False)
    page.get_by_role("link", name="Da Dashboard").click()
    page.locator("#block-claro-commercemanagement").get_by_role(
        "link", name="Manage Orders"
    ).click()
    print("Current URL is:", page.url)
    if page.locator("h1.page-title").inner_text().strip() != "Orders":
        page.screenshot(path="Orders_screenshot.png", full_page=False)
    page.get_by_role("link", name="Da Dashboard").click()
    page.locator("#block-claro-commercemanagement").get_by_role(
        "link", name="Financial Reports"
    ).click()
    print("Current URL is:", page.url)
    if page.locator("h1.page-title").inner_text().strip() != "Financial Reports":
        page.screenshot(path="Financial_Reports_screenshot.png", full_page=False)
    page.get_by_role("link", name="Da Dashboard").click()
    page.locator("#block-claro-commercemanagement").get_by_role(
        "link", name="Reports", exact=True
    ).click()
    print("Current URL is:", page.url)
    if page.locator("h1.page-title").inner_text().strip() != "Reports":
        page.screenshot(path="Reports_screenshot.png", full_page=False)
    page.get_by_role("link", name="Da Dashboard").click()
    page.locator("#block-claro-siteconfiguration").get_by_role(
        "link", name="Site Settings"
    ).click()
    print("Current URL is:", page.url)
    if page.locator("h1.page-title").inner_text().strip() != "Site Settings":
        page.screenshot(path="Staff_Reviews_screenshot.png", full_page=False)
    page.get_by_role("link", name="Da Dashboard").click()
    page.locator("#block-claro-siteconfiguration").get_by_role(
        "link", name="Store Information"
    ).click()
    print("Current URL is:", page.url)
    if page.locator("h1.page-title").inner_text().strip() != "Stores":
        page.screenshot(path="Stores_screenshot.png", full_page=False)
    page.get_by_role("link", name="Da Dashboard").click()
    page.locator("#block-claro-siteconfiguration").get_by_role(
        "link", name="Marketing & Analytics"
    ).click()
    print("Current URL is:", page.url)
    if page.locator("h1.page-title").inner_text().strip() != "Marketing & Analytics":
        page.screenshot(path="Marketing_screenshot.png", full_page=False)
    page.get_by_role("link", name="Da Dashboard").click()
    page.locator("#block-claro-siteconfiguration").get_by_role(
        "link", name="Newsletter Signups"
    ).click()
    print("Current URL is:", page.url)
    if (
        page.locator("h1.page-title").inner_text().strip()
        != "Manage Newsletter Signup forms"
    ):
        page.screenshot(path="ManageNewsletter_screenshot.png", full_page=False)
    page.get_by_role("link", name="Da Dashboard").click()
    page.locator("#block-claro-siteconfiguration").get_by_role(
        "link", name="Design"
    ).click()
    print("Current URL is:", page.url)
    if page.locator("h1.page-title").inner_text().strip() != "Manage Designs":
        page.screenshot(path="Manage_Designs_screenshot.png", full_page=False)
    page.get_by_role("link", name="Da Dashboard").click()
    page.locator("#block-claro-siteconfiguration").get_by_role(
        "link", name="Homepage"
    ).click()
    print("Current URL is:", page.url)
    if page.locator("h1.page-title").inner_text().strip() != "Edit Home page Home Page":
        page.screenshot(path=" Home_Page_screenshot.png", full_page=False)
    page.get_by_role("link", name="Da Dashboard").click()
    page.locator("#block-claro-siteconfiguration").get_by_role(
        "link", name="Default Pages"
    ).click()
    print("Current URL is:", page.url)
    if page.locator("h1.page-title").inner_text().strip() != "Default Pages":
        page.screenshot(path="Default_Pages_screenshot.png", full_page=False)
    page.get_by_role("link", name="Da Dashboard").click()
    page.locator("#block-claro-siteconfiguration").get_by_role(
        "link", name="Store Admins"
    ).click()
    print("Current URL is:", page.url)
    if page.locator("h1.page-title").inner_text().strip() != "Store Admins":
        page.screenshot(path="Store_Admins_screenshot.png", full_page=False)
    page.get_by_role("link", name="Da Dashboard").click()
    page.click("//a[text()='Blog Post']")
    print("Current URL is:", page.url)
    if page.locator("h1.page-title").inner_text().strip() != "Create Blog post":
        page.screenshot(path="CreateBlogpost_screenshot.png", full_page=False)
    page.get_by_role("link", name="Da Dashboard").click()
    page.click("//a[text()='Product Search Categories']")
    print("Current URL is:", page.url)
    if page.locator("h1.page-title").inner_text().strip() != "Product Search Category":
        page.screenshot(path="ProductSearchCategory_screenshot.png", full_page=False)
    page.get_by_role("link", name="Logout").click()


if __name__ == "__main__":
    with sync_playwright() as playwright:
        run(playwright)
