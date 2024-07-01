package HouseAccount;

import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.time.Duration;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

import org.openqa.selenium.By;
import org.openqa.selenium.JavascriptExecutor;
import org.openqa.selenium.Keys;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.testng.annotations.AfterMethod;
import org.testng.annotations.BeforeMethod;
import org.testng.annotations.DataProvider;
import org.testng.annotations.Test;

import ABA.Basepackage.BaseClass;
import Utils.Utility;
import usercheckoutpages.Checkoutpage;

public class HouseAccountGuestcheckout extends BaseClass {

	public HouseAccountGuestcheckout() {
		     super();
	}
	
WebDriver driver;
Checkoutpage checkoutPage;
	
	@BeforeMethod
	public void SetUp() throws InterruptedException {
		
		
		driver = initializebrowserAndOpenwebpage(prop.getProperty("browser"));
		checkoutPage = new Checkoutpage(driver);
		
	}
	
	@AfterMethod
	public void TearDown() {
		
		driver.quit();
	}
	
	
	
	@Test(dataProvider = "DataSupplier")
	public void GuestCheckoutWithUPSGROUND(String testType, String url, String browser, String email, String password, String houseaccountnumber, String preferredname, String phone, String firstname, String lastname, String address, String city, String state, String zipcode) throws InterruptedException {
		if (!testType.equals("Field")) return;
		
		checkoutPage.clickBookImage();
		checkoutPage.clickAddToCart();
        checkoutPage.clickCookieButton();
        checkoutPage.clickYourCartLink();
        checkoutPage.clickCheckoutButton();
        checkoutPage.clickContinueAsGuest();
        checkoutPage.enterEmail(email);
        checkoutPage.enterConfirmEmail(email);
        checkoutPage.enterPreferredName(preferredname);
        checkoutPage.enterPhone(phone);
        checkoutPage.enterGivenName(firstname);
        checkoutPage.enterFamilyName(lastname);
        checkoutPage.enterAddress(address);
        checkoutPage.enterLocality(city);
        checkoutPage.enterAdministrativeArea(state);
        checkoutPage.enterPostalCode(zipcode);
        checkoutPage.selectUPSground();
        Thread.sleep(8000);
        checkoutPage.selectHouseAccount();
        Thread.sleep(8000);
        checkoutPage.enterHouseAccountNumber(houseaccountnumber);
        Thread.sleep(8000);
        checkoutPage.clickContinueToReview();
        checkoutPage.clickCompletePurchase();
    }
        
		
		
	
	
	@Test(dataProvider = "DataSupplier")
	public void GuestCheckoutWithUPSOVERNIGHT(String testType, String url, String browser, String email, String password, String houseaccountnumber, String preferredname, String phone, String firstname, String lastname, String address, String city, String state, String zipcode) throws InterruptedException {
		if (!testType.equals("Field")) return;
		
		
		checkoutPage.clickBookImage();
		checkoutPage.clickAddToCart();
        checkoutPage.clickCookieButton();
        checkoutPage.clickYourCartLink();
        checkoutPage.clickCheckoutButton();
        checkoutPage.clickContinueAsGuest();
        checkoutPage.enterEmail(email);
        checkoutPage.enterConfirmEmail(email);
        checkoutPage.enterPreferredName(preferredname);
        checkoutPage.enterPhone(phone);
        checkoutPage.enterGivenName(firstname);
        checkoutPage.enterFamilyName(lastname);
        checkoutPage.enterAddress(address);
        checkoutPage.enterLocality(city);
        checkoutPage.enterAdministrativeArea(state);
        checkoutPage.enterPostalCode(zipcode);
        checkoutPage.selectUPSovernight();
        Thread.sleep(8000);
        checkoutPage.selectHouseAccount();
        Thread.sleep(8000);
        checkoutPage.enterHouseAccountNumber(houseaccountnumber);
        Thread.sleep(8000);
        checkoutPage.clickContinueToReview();
        checkoutPage.clickCompletePurchase();
		
		
	}
	
	@Test(dataProvider = "DataSupplier")
	public void GuestCheckoutWithUSPSPRIORITYMAIL(String testType, String url, String browser, String email, String password, String houseaccountnumber, String preferredname, String phone, String firstname, String lastname, String address, String city, String state, String zipcode) throws InterruptedException {
		if (!testType.equals("Field")) return;
		
		checkoutPage.clickBookImage();
		checkoutPage.clickAddToCart();
        checkoutPage.clickCookieButton();
        checkoutPage.clickYourCartLink();
        checkoutPage.clickCheckoutButton();
        checkoutPage.clickContinueAsGuest();
        checkoutPage.enterEmail(email);
        checkoutPage.enterConfirmEmail(email);
        checkoutPage.enterPreferredName(preferredname);
        checkoutPage.enterPhone(phone);
        checkoutPage.enterGivenName(firstname);
        checkoutPage.enterFamilyName(lastname);
        checkoutPage.enterAddress(address);
        checkoutPage.enterLocality(city);
        checkoutPage.enterAdministrativeArea(state);
        checkoutPage.enterPostalCode(zipcode);
        checkoutPage.selectUSPSpriority();
        Thread.sleep(8000);
        checkoutPage.selectHouseAccount();
        Thread.sleep(8000);
        checkoutPage.enterHouseAccountNumber(houseaccountnumber);
        Thread.sleep(8000);
        checkoutPage.clickContinueToReview();
        checkoutPage.clickCompletePurchase();
		
		
	}
	
	@Test(dataProvider = "DataSupplier")
	public void GuestCheckoutWithUPS2DAY(String testType, String url, String browser, String email, String password, String houseaccountnumber, String preferredname, String phone, String firstname, String lastname, String address, String city, String state, String zipcode) throws InterruptedException {

	    if (!testType.equals("Field")) return;
	    
	    checkoutPage.clickBookImage();
		checkoutPage.clickAddToCart();
        checkoutPage.clickCookieButton();
        checkoutPage.clickYourCartLink();
        checkoutPage.clickCheckoutButton();
        checkoutPage.clickContinueAsGuest();
        checkoutPage.enterEmail(email);
        checkoutPage.enterConfirmEmail(email);
        checkoutPage.enterPreferredName(preferredname);
        checkoutPage.enterPhone(phone);
        checkoutPage.enterGivenName(firstname);
        checkoutPage.enterFamilyName(lastname);
        checkoutPage.enterAddress(address);
        checkoutPage.enterLocality(city);
        checkoutPage.enterAdministrativeArea(state);
        checkoutPage.enterPostalCode(zipcode);
        checkoutPage.selectUPS2day();
        Thread.sleep(8000);
        checkoutPage.selectHouseAccount();
        Thread.sleep(8000);
        checkoutPage.enterHouseAccountNumber(houseaccountnumber);
        Thread.sleep(8000);
        checkoutPage.clickContinueToReview();
        checkoutPage.clickCompletePurchase();
	}

	
	 @DataProvider(name = "DataSupplier")
	    public Object[][] DataSupplier() throws IOException {
	        return getDataFromCsv("fielddata.csv");
	    	
	    }
	
	public Object[][] getDataFromCsv(String filePath) throws IOException {
		    String COMMA_DELIMITER = ",";
		    List<List<String>> records = new ArrayList<>();
		    try (BufferedReader br = new BufferedReader(new FileReader(filePath))) {
		        String line;
		        while ((line = br.readLine()) != null) {
		            String[] values = line.split(COMMA_DELIMITER);
		            records.add(Arrays.asList(values));
		        }
		    } catch (Exception e) {
		        e.printStackTrace();
		    }

		    // Debugging: Print the records read from the CSV
		    System.out.println("Records from CSV:");
		    for (List<String> record : records) {
		        System.out.println(record);
		    }

		    // Check if the records list is not empty and the first row has the expected number of columns
		    if (records.size() > 1 && records.get(0).size() == 14) {
		        Object[][] data = new Object[records.size() - 1][records.get(0).size()];
		        for (int r = 1; r < records.size(); r++) {
		            for (int c = 0; c < records.get(r).size(); c++) {
		                data[r - 1][c] = records.get(r).get(c);
		            }
		        }
		        return data;
		    } else {
		        throw new RuntimeException("CSV file does not have the expected number of rows or columns.");
		    }
	 }
}
		


