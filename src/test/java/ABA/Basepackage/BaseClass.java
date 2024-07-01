package ABA.Basepackage;

import java.io.File;
import java.io.FileInputStream;
import java.time.Duration;
import java.util.Properties;

import org.openqa.selenium.By;
import org.openqa.selenium.Keys;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.chrome.ChromeDriver;
import org.openqa.selenium.edge.EdgeDriver;
import org.openqa.selenium.firefox.FirefoxDriver;

import Utils.Utility;

public class BaseClass {

	WebDriver driver;
	public Properties prop;
	public Properties dataProp;
	
	public BaseClass() {
		
		prop = new Properties();
		File propfile = new File(System.getProperty("user.dir")+"\\src\\main\\java\\configpropfiles\\config.propertiesfile");
		
		dataProp = new Properties();
		File dataPropfile = new File(System.getProperty("user.dir")+"\\src\\main\\java\\TestData\\testdata.properties");
		
		try {
			FileInputStream fis2 = new FileInputStream(dataPropfile);
			dataProp.load(fis2);
			}catch(Throwable e) {
				e.printStackTrace();
			}
		
		try {
		FileInputStream fis = new FileInputStream(propfile);
		prop.load(fis);
		}catch(Throwable e) {
			e.printStackTrace();
		}
	}
	
	public WebDriver initializebrowserAndOpenwebpage(String Browsername) {
		
		
		if(Browsername.equalsIgnoreCase("chrome")) {
			driver = new ChromeDriver();
			
		}else if(Browsername.equalsIgnoreCase("firefox")) {
			driver = new FirefoxDriver();
			
		}else if(Browsername.equalsIgnoreCase("edge")) {
			driver = new EdgeDriver(); 	
		}
		
		driver.manage().timeouts().implicitlyWait(Duration.ofSeconds(Utility.IMPLICIT_WAIT_TIME));
		driver.manage().timeouts().pageLoadTimeout(Duration.ofSeconds(Utility.PAGE_WAIT_TIME));
		driver.get(prop.getProperty("url"));
		driver.manage().window().maximize();
		driver.findElement(By.partialLinkText("Books")).click();
	    try {
			Thread.sleep(8000);
		} catch (InterruptedException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
	    driver.findElement(By.partialLinkText("Art, Architecture, and Photography")).sendKeys(Keys.ENTER);
	    try {
			Thread.sleep(8000);
		} catch (InterruptedException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
	    driver.manage().window().maximize();
	    
	    return driver;
	}
}
