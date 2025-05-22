from email.mime import base
from click import launch
from playwright.sync_api import sync_playwright
import time
from base_class import BasePage
from product_elements import ProductElements, DonationElements, catagoryelements


def launch_and_login(playwright):
    base = BasePage(playwright)
    base.go_to_home()
    page = base.page
    page.click(ProductElements.logintitle)
    page.click(ProductElements.loginname)
    page.fill(ProductElements.fillname, base.ABA_USERNAME)
    page.fill(ProductElements.fillpassword, base.ABA_PASSWORD)
    time.sleep(3)
    page.click(ProductElements.loginsubmission)
    page.click(ProductElements.dashboardclick)
    return base


def create_donation(playwright):
    base = launch_and_login(playwright)
    page = base.page
    page.click(DonationElements.productselection)
    page.click(DonationElements.donationselection)
    page.fill(DonationElements.donationtitle, DonationElements.donationtitlename)
    page.fill(DonationElements.donationsku, DonationElements.donationskuname)
    time.sleep(2)
    page.click(DonationElements.AddMedia)
    page.set_input_files(DonationElements.insertimage, DonationElements.imagepath)
    page.fill(DonationElements.filler1, DonationElements.fillertext)
    page.click(DonationElements.savedonation)
    page.click(DonationElements.InsertSelected)
    time.sleep(2)
    page.get_by_role(
        DonationElements.textbox1, name=DonationElements.defaultamount1
    ).click()
    page.get_by_role(
        DonationElements.textbox2, name=DonationElements.defaultamount2
    ).fill(DonationElements.price)

    page.click(DonationElements.donationsave)
    page.click(ProductElements.commonlogout)

    base.close_browser


def product_service_catagory(playwright):
    base = launch_and_login(playwright)
    page = base.page
    page.click(catagoryelements.ProductCatagories)
    page.click(catagoryelements.catagoryterms)
    page.click(catagoryelements.catagoryvalue)
    page.fill(catagoryelements.catagorytitle, catagoryelements.catagorytitlevalue)
    page.click(catagoryelements.saveproductcatagory)
    page.click(ProductElements.dashboardclick)
    page.click(catagoryelements.servicecatagory)
    page.click(catagoryelements.servicecatagoryterm)
    page.click(catagoryelements.servicetitle)
    page.fill(catagoryelements.servicename, catagoryelements.servicenametitle)
    page.fill(catagoryelements.servicesubtitlefield, catagoryelements.servicesubname)
    page.click(catagoryelements.servicesubmit)
    page.click(ProductElements.commonlogout)
    base.close_browser


def create_book_variation(playwright):
    base = launch_and_login(playwright)
    page = base.page
    page.click("//a[text()='Product']")
    page.click("//a[@href='/product/add/book_variation']")
    page.click("//input[@value='signed']")
    page.fill(
        "//input[@placeholder='Search by ISBN, book title or product name']",
        "9780063203907",
    )
    page.fill("#edit-variations-entity-sku-0-value", "9780063203907var")
    page.click("#edit-variations-entity-price-0-number")
    page.fill("#edit-variations-entity-price-0-number", "17.00")
    page.click("#edit-actions-submit")
    time.sleep(2)
    page.click(ProductElements.commonlogout)
    base.close_browser


def create_egiftcard(playwright):
    base = launch_and_login(playwright)
    page = base.page
    page.click("//a[text()='Product']")
    page.get_by_role("link", name="E-Gift Card").click()
    page.get_by_role("textbox", name="Title *").click()
    page.get_by_role("textbox", name="Title *").fill("IC-Egiftcard")
    page.get_by_role("textbox", name="SKU *").fill("EGE123456")
    time.sleep(2)
    page.get_by_role("button", name="Add media").click()
    page.set_input_files("input[type='file']", "IndieCommerce/ProductImages/egc.webp")
    page.fill("//input[@name='media[0][fields][field_media_image][0][alt]']", "ALTEXT3")
    page.click("//button[text()='Save']")
    page.click("//button[text()='Insert selected']")
    time.sleep(2)
    page.get_by_role("textbox", name="Default amount *").click()
    page.get_by_role("textbox", name="Default amount *").fill("14")
    page.get_by_role("textbox", name="Maximum amount").click()
    page.get_by_role("textbox", name="Maximum amount").fill("135")
    page.get_by_role("button", name="Save").click()
    page.click(ProductElements.commonlogout)
    base.close_browser


def create_services(playwright):
    base = launch_and_login(playwright)
    page = base.page
    page.click("//a[text()='Product']")
    page.get_by_role("link", name="Service", exact=True).click()
    page.get_by_role("textbox", name="Title *").fill("IC-SERVICE")
    page.get_by_role("textbox", name="Service category *").click()
    page.get_by_role("textbox", name="Service category *").fill("Service catagory1")
    page.get_by_role("textbox", name="SKU *").fill("SS12345")
    time.sleep(2)
    page.get_by_role("button", name="Add media").click()
    page.set_input_files(
        "input[type='file']", "IndieCommerce/ProductImages/services.jpeg"
    )
    page.fill(
        "//input[@name='media[0][fields][field_media_image][0][alt]']", "ALTEXT22"
    )
    page.click("//button[text()='Save']")
    page.click("//button[text()='Insert selected']")
    time.sleep(2)
    page.get_by_role("textbox", name="Price *").click()
    page.get_by_role("textbox", name="Price *").fill("15")
    page.get_by_role("button", name="Save", exact=True).click()
    page.click(ProductElements.commonlogout)
    base.close_browser


def create_physicalgiftcard(playwright):
    base = launch_and_login(playwright)
    page = base.page
    page.click("//a[text()='Product']")
    page.get_by_role("link", name="Gift Card", exact=True).click()
    page.get_by_role("textbox", name="Title *").fill("IC-Giftcard")
    page.get_by_role("textbox", name="SKU *").fill("PGC1122")
    page.get_by_role("button", name="Add media").click()
    time.sleep(2)
    page.set_input_files("input[type='file']", "IndieCommerce/ProductImages/pgc.jpeg")
    page.fill(
        "//input[@name='media[0][fields][field_media_image][0][alt]']", "ALTEXT288"
    )
    page.click("//button[text()='Save']")
    page.click("//button[text()='Insert selected']")
    time.sleep(2)
    page.get_by_role("textbox", name="Default amount *").click()
    page.get_by_role("textbox", name="Default amount *").fill("26")
    page.get_by_role("textbox", name="Maximum amount").click()
    page.get_by_role("textbox", name="Maximum amount").fill("150")
    page.get_by_role("button", name="Save").click()
    page.click(ProductElements.commonlogout)
    base.close_browser


def create_Nonshippableproduct(playwright):
    base = launch_and_login(playwright)
    page = base.page
    page.click("//a[text()='Product']")
    page.get_by_role("link", name="Non-shippable Store").click()
    page.get_by_role("textbox", name="Title *").fill("IC-NON Shippable Merchandise ")
    page.get_by_role("textbox", name="Product Category (value 1) *").fill(
        "ProductCatagory1"
    )
    page.get_by_role("textbox", name="SKU *").fill("NSM12345")
    time.sleep(1)
    page.get_by_role("button", name="Add media").click()
    page.set_input_files(
        "input[type='file']", "IndieCommerce/ProductImages/Nonshippable.webp"
    )
    page.fill(
        "//input[@name='media[0][fields][field_media_image][0][alt]']", "ALTEXT2114"
    )
    page.click("//button[text()='Save']")
    page.click("//button[text()='Insert selected']")
    time.sleep(1)
    page.get_by_role("textbox", name="Price *").click()
    page.get_by_role("textbox", name="Price *").fill("25")
    page.get_by_role("button", name="Save", exact=True).click()
    page.click(ProductElements.commonlogout)
    base.close_browser


def create_storemerchandise(playwright):
    base = launch_and_login(playwright)
    page = base.page
    page.click("//a[text()='Product']")
    page.get_by_role("link", name="Store Merchandise", exact=True).click()
    page.get_by_role("textbox", name="Title *").fill("IC-Store Merchandise")
    page.get_by_role("textbox", name="Product Category (value 1) *").fill(
        "ProductCatagory1"
    )
    page.get_by_role("textbox", name="SKU *").fill("MSW18990")
    time.sleep(1)
    page.get_by_role("button", name="Add media").click()
    page.set_input_files(
        "input[type='file']", "IndieCommerce/ProductImages/merchandise.webp"
    )
    page.fill(
        "//input[@name='media[0][fields][field_media_image][0][alt]']", "ALTEXT2001"
    )
    page.click("//button[text()='Save']")
    page.click("//button[text()='Insert selected']")
    time.sleep(1)
    page.get_by_role("textbox", name="9.99").fill("8")
    page.get_by_role("textbox", name="Price *").click()
    page.get_by_role("textbox", name="Price *").fill("25")
    page.get_by_role("button", name="Save", exact=True).click()
    page.click(ProductElements.commonlogout)
    base.close_browser


def create_Subscription(playwright):
    base = launch_and_login(playwright)
    page = base.page
    page.click("//a[text()='Product']")
    page.get_by_role("link", name="Subscription").click()
    page.get_by_role("textbox", name="Title *").fill("IC-Subscription")
    page.get_by_role("textbox", name="SKU *").fill("SUB01990")
    page.get_by_role("button", name="Add media").click()
    time.sleep(1)
    page.set_input_files(
        "input[type='file']", "IndieCommerce/ProductImages/subscription.jpg"
    )
    page.fill(
        "//input[@name='media[0][fields][field_media_image][0][alt]']", "ALTEXT1800"
    )
    page.click("//button[text()='Save']")
    time.sleep(1)
    page.get_by_role("textbox", name="Price *").click()
    page.get_by_role("textbox", name="Price *").fill("28")
    page.get_by_text("Price USD Format:").click()
    page.get_by_role("textbox", name="Name *").fill("Subscriber Name")
    page.get_by_role("button", name="Save").click()
    page.click(ProductElements.commonlogout)
    base.close_browser


if __name__ == "__main__":
    with sync_playwright() as playwright:
        product_service_catagory(playwright)
        create_donation(playwright)
        create_book_variation(playwright)
        create_services(playwright)
        create_egiftcard(playwright)
        create_physicalgiftcard(playwright)
        create_Nonshippableproduct(playwright)
        create_storemerchandise(playwright)
        create_Subscription(playwright)
