from playwright.sync_api import sync_playwright


class ProductElements:
    logintitle = "//a[@title='Log in']"
    loginname = "#edit-name"
    fillname = "#edit-name"
    fillpassword = "#edit-pass"
    loginsubmission = "#edit-submit"
    dashboardclick = "//a[@title='Dashboard']"
    commonlogout = "//span[text()='Logout']"


class DonationElements:
    productselection = "//a[text()='Product']"
    donationselection = "//a[@href='/product/add/donation']"
    donationtitle = "#edit-title-0-value"
    donationtitlename = "DonationProduct2"
    donationsku = "#edit-variations-entity-sku-0-value"
    donationskuname = "DD002"
    AddMedia = "//input[@value='Add media']"
    insertimage = "input[type='file']"
    imagepath = "IndieCommerce/ProductImages/donationpic.webp"
    filler1 = "//input[@name='media[0][fields][field_media_image][0][alt]']"
    fillertext = "ALTEXT2"
    savedonation = "//button[text()='Save']"
    InsertSelected = "//button[text()='Insert selected']"
    textbox1 = "textbox"
    defaultamount1 = "Default amount"
    textbox2 = "textbox"
    defaultamount2 = "Default amount"
    price = "16.00"
    donationsave = "//input[@value='Save']"


class catagoryelements:
    ProductCatagories = "//a[text()='Product Categories']"
    catagoryterms = "(//a[text()='Add term'])[1]"
    catagoryvalue = "//input[@name='name[0][value]']"
    catagorytitle = "//input[@name='name[0][value]']"
    catagorytitlevalue = "ProductCatagory1"
    saveproductcatagory = "//input[@value='Save']"
    servicecatagory = "//a[text()='Service Categories']"
    servicecatagoryterm = "(//a[text()='Add term'])[1]"
    servicetitle = "#edit-name-0-value"
    servicename = "#edit-name-0-value"
    servicenametitle = "ServiceCatagory1"
    servicesubtitlefield = "#edit-field-preferences-form-0-name"
    servicesubname = "Participant name"
    servicesubmit = "#edit-submit"
