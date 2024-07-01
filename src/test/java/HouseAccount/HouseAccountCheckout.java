package HouseAccount;

import java.time.Duration;

import org.openqa.selenium.By;
import org.openqa.selenium.JavascriptExecutor;
import org.openqa.selenium.Keys;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.testng.annotations.AfterMethod;
import org.testng.annotations.BeforeMethod;
import org.testng.annotations.Test;

import ABA.Basepackage.BaseClass;

public class HouseAccountCheckout extends BaseClass {
	
	
	public HouseAccountCheckout() {
		super();
	}	
	WebDriver driver;
	
	@BeforeMethod
	public void SetUp() throws InterruptedException {
		
		
		driver = initializebrowserAndOpenwebpage(prop.getProperty("browser"));
		
	}
	
	
	
	@AfterMethod
	public void TearDown() {
		
		driver.quit();
	}
	
	
	@Test
	public void CustomerCheckout() throws InterruptedException {
	    driver.findElement(By.partialLinkText("Log in")).click();
	    driver.findElement(By.id("edit-name")).sendKeys(prop.getProperty("email"));
	    driver.findElement(By.id("edit-pass")).sendKeys(prop.getProperty("password"));
	    driver.findElement(By.id("edit-submit")).sendKeys(Keys.ENTER);
	    driver.findElement(By.partialLinkText("Books")).click();
	   // Thread.sleep(8000);
	   // WebDriverWait wait = new WebDriverWait(driver,Duration.ofSeconds(1000));
	    
	    //wait.until(ExpectedConditions.elem
	    driver.findElement(By.partialLinkText("Art, Architecture, and Photography")).sendKeys(Keys.ENTER);
	   // Thread.sleep(8000);
	    WebElement Cookie1 = driver.findElement(By.xpath("//button[text()='Got it!']"));
		JavascriptExecutor executor = (JavascriptExecutor) driver;
		executor.executeScript("arguments[0].click();", Cookie1);
	    driver.findElement(By.xpath("//*[@id=\"block-bookworm-content\"]/div/div/div/div[3]/div/div[1]/div[1]/div/a/img")).click();
	    driver.findElement(By.xpath("//input[@value='Add to cart']")).sendKeys(Keys.ENTER);
	   // Thread.sleep(7000);
	    driver.findElement(By.xpath("//*[@id=\"block-bookworm-utilitymenu\"]/ul/li[3]/span[1]/a")).click();
		driver.findElement(By.xpath("//button[text()='Checkout']")).sendKeys(Keys.ENTER);
	   // Thread.sleep(15000);
	    driver.findElement(By.xpath("//label[contains(text(),'House Account ')]")).click();
	   // Thread.sleep(8000);
	    driver.findElement(By.xpath("//input[@name='add_payment_method[payment_details][house_account_number]']")).sendKeys(prop.getProperty("houseaccountnumber"));
	   // Thread.sleep(8000);
	    driver.findElement(By.name("apply_coupon")).sendKeys(Keys.TAB);
	    driver.findElement(By.xpath("//input[@value='Continue to review']")).sendKeys(Keys.ENTER);
        driver.findElement(By.xpath("//input[@value='Complete Purchase']")).sendKeys(Keys.ENTER);
        ;
       
		
	}

}
