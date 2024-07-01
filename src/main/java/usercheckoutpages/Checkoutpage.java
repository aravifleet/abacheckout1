package usercheckoutpages;

import org.openqa.selenium.By;
import org.openqa.selenium.JavascriptExecutor;
import org.openqa.selenium.Keys;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;

public class Checkoutpage {
	
	WebDriver driver;
    JavascriptExecutor executor;
    
    public Checkoutpage(WebDriver driver) {
        this.driver = driver;
        this.executor = (JavascriptExecutor) driver;
    }
    
 // Web elements
    By bookImage = By.xpath("//*[@id=\"block-bookworm-content\"]/div/div/div/div[3]/div/div[1]/div[1]/div/a/img");
    By addToCartButton = By.xpath("//input[@value='Add to cart']");
    By cookieButton = By.xpath("//button[text()='Got it!']");
    By yourCartLink = By.partialLinkText("your cart");
    By checkoutButton = By.xpath("//button[text()='Checkout']");
    By continueAsGuestButton = By.xpath("//input[@value='Continue as Guest']");
    By emailField = By.id("edit-indiecommerce-contact-information-email");
    By confirmEmailField = By.id("edit-indiecommerce-contact-information-email-confirm");
    By preferredNameField = By.id("edit-profile-field-preferred-name-0-value");
    By phoneField = By.xpath("//input[@placeholder='(201) 555-0123']");
    By givenNameField = By.xpath("//input[@name='shipping_information[shipping_profile][address][0][address][given_name]']");
    By familyNameField = By.xpath("//input[@name='shipping_information[shipping_profile][address][0][address][family_name]']");
    By addressField = By.xpath("//input[@name='shipping_information[shipping_profile][address][0][address][address_line1]']");
    By localityField = By.xpath("//input[@name='shipping_information[shipping_profile][address][0][address][locality]']");
    By administrativeAreaField = By.xpath("//select[@name='shipping_information[shipping_profile][address][0][address][administrative_area]']");
    By postalCodeField = By.xpath("//input[@name='shipping_information[shipping_profile][address][0][address][postal_code]']"); 
    By upsGroundOption = By.xpath("//label[contains(text(),'UPS Ground: $10.00 ')]");
    By upsovernight = By.xpath("//label[contains(text(),'UPS Overnight: $30.95')]");
    By ups2day = By.xpath("//label[contains(text(),'UPS 2-Day: $22.95 ')]");
    By uspspriority = By.xpath("//label[contains(text(),'USPS Priority Mail: $12.20 ')]");
    By houseAccountOption = By.xpath("//label[contains(text(),'House Account ')]");
    By houseAccountNumberField = By.name("add_payment_method[payment_details][house_account_number]");
    By continueToReviewButton = By.xpath("//input[@value='Continue to review']");
    By completePurchaseButton = By.xpath("//input[@value='Complete Purchase']");
	
 // Methods to interact with elements
    public void clickBookImage() {
        driver.findElement(bookImage).click();
    }
    
    public void clickAddToCart() {
        driver.findElement(addToCartButton).click();
    }

    public void clickCookieButton() {
        executor.executeScript("arguments[0].click();", driver.findElement(cookieButton));
    }

    public void clickYourCartLink() {
        driver.findElement(yourCartLink).click();
    }

    public void clickCheckoutButton() {
        driver.findElement(checkoutButton).sendKeys(Keys.ENTER);
    }

    public void clickContinueAsGuest() {
        driver.findElement(continueAsGuestButton).click();
    }

    public void enterEmail(String email) {
        driver.findElement(emailField).sendKeys(email);
    }

    public void enterConfirmEmail(String email) {
        driver.findElement(confirmEmailField).sendKeys(email);
    }

    public void enterPreferredName(String preferredName) {
        driver.findElement(preferredNameField).sendKeys(preferredName);
    }

    public void enterPhone(String phone) {
        WebElement element = driver.findElement(phoneField);
        element.sendKeys(phone);
        element.sendKeys(Keys.TAB);
    }

    public void enterGivenName(String givenName) {
        driver.findElement(givenNameField).sendKeys(givenName);
    }

    public void enterFamilyName(String familyName) {
        driver.findElement(familyNameField).sendKeys(familyName);
    }

    public void enterAddress(String address) {
        driver.findElement(addressField).sendKeys(address);
    }

    public void enterLocality(String city) {
        driver.findElement(localityField).sendKeys(city);
    }

    public void enterAdministrativeArea(String state) {
        driver.findElement(administrativeAreaField).sendKeys(state);
    }

    public void enterPostalCode(String postalCode) {
        WebElement element = driver.findElement(postalCodeField);
        element.sendKeys(postalCode);
        element.sendKeys(Keys.TAB);
    }

    public void selectUPSground() {
        driver.findElement(upsGroundOption).click();
    }
    
    public void selectUSPSpriority() {
        driver.findElement(uspspriority).click();
    }
    
    public void selectUPS2day() {
        driver.findElement(ups2day).click();
    }
    
    public void selectUPSovernight() {
        driver.findElement(upsovernight).click();
    }

    public void selectHouseAccount() {
        driver.findElement(houseAccountOption).click();
    }

    public void enterHouseAccountNumber(String houseAccountNumber) {
        driver.findElement(houseAccountNumberField).sendKeys(houseAccountNumber);
    }

    public void clickContinueToReview() {
        driver.findElement(continueToReviewButton).sendKeys(Keys.ENTER);
    }

    public void clickCompletePurchase() {
        driver.findElement(completePurchaseButton).sendKeys(Keys.ENTER);
    }

}
    
    
    
    
    
    
    
    
    
   
