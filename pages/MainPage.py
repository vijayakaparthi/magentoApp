from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
 
class MainPage():
  #class constructor to initialize driver and action objects
    def __init__(self,driver,action) :
      self.driver=driver
      self.action=action

    def Locators(self):
    # Finding locators for menu items and submenuitems --women->tops->jackets 
     spanMainmenu=self.driver.find_element(By.XPATH,"//a[@id='ui-id-4']/span[2]")
     subMenu1=self.driver.find_element(By.XPATH,"//a[@id='ui-id-9']/span[2]")
     subMenu2=self.driver.find_element(By.XPATH,"//a[@id='ui-id-11']/span[1]")
     self.action.move_to_element(spanMainmenu).pause(2).move_to_element(subMenu1).pause(2).click(subMenu2).perform()

     #finding the size and color locators after selecting the item
     sizeLocatorDiv=self.driver.find_element(By.ID,"option-label-size-143-item-166")
     self.action.move_to_element(sizeLocatorDiv).click().perform()
        
     colorLocatorDiv=self.driver.find_element(By.ID,"option-label-color-93-item-50")

     self.action.move_to_element(colorLocatorDiv).pause(2).click().perform()

     #locator for adding to cart
     addToCartLocator=self.driver.find_element(By.XPATH,"//button[@class='action tocart primary']")
     self.action.move_to_element(addToCartLocator).pause(2).click().perform()

     #locator returns the item selected description--You added Olivia 1/4 Zip Light Jacket to your shopping cart.
     messageLocator=self.driver.find_element(By.XPATH,"//div[@class='messages']/div[1]/div[1]")
     msgLoc=messageLocator.text
     #locator for shopping card towards end
     shoppingcartLocator=self.driver.find_element(By.XPATH,"//a[@class='action showcart']")
     self.action.move_to_element(shoppingcartLocator).pause(2).click().perform()

     # locator for proceed to checkout button
     proceedtoChkOutLocater=self.driver.find_element(By.XPATH,"//button[@id='top-cart-btn-checkout']")
     time.sleep(5)
     self.action.move_to_element(proceedtoChkOutLocater).pause(2).click().perform()
    
     # locator for order summary
     orderSummaryLocater=self.driver.find_element(By.XPATH,"//div[@class='opc-block-summary']/span[1]")
     ordersummarytext=orderSummaryLocater.text
    
     orderSumDetail1=self.driver.find_element(By.XPATH,"//div[@class='title']/strong[1]/span[1]")
     orderSumDetail2=self.driver.find_element(By.XPATH,"//div[@class='title']/strong[1]/span[2]")
        
     time.sleep(4)
     self.driver.find_element(By.ID,"customer-email").send_keys("kapvij@gmail.com")
     self. driver.find_element(By.NAME,"firstname").send_keys("vijaya")
     self.driver.find_element(By.NAME,"lastname").send_keys("kaparthi")
      #time.sleep(5)
     self.driver.find_element(By.NAME,"street[0]").send_keys("3456 Lomita Blvd")
      #time.sleep(5)
     self.driver.find_element(By.NAME,"city").send_keys("Lomita")
      #self.driver.find_element(By.NAME,"region_id").click()
      #time.sleep(5)
     element=self.driver.find_element(By.NAME,"region_id")
     select = Select(element)
     select.select_by_value("12")          
     self.driver.find_element(By.NAME,"postcode").send_keys("90505")
     self.driver.find_element(By.NAME,"telephone").send_keys("9495993935")
      #time.sleep(5)      
      #shipping $0.00 selection
     self.driver.find_element(By.XPATH,"//*[@id='checkout-shipping-method-load']/table/tbody/tr[1]/td[2]/span/span").click()
       #click on next button
     self.driver.find_element(By.XPATH,"//*[@id='shipping-method-buttons-container']/div/button").click()
     time.sleep(5)
    # shippinginfo=self.driver.find_element(By.CLASS_NAME,"billing-address-details")
    # print(shippinginfo.text)
     #placeorder
     self.driver.find_element(By.XPATH,"//*[@id='checkout-payment-method-load']/div/div/div[2]/div[2]/div[4]/div/button").click()   

     #span_tag=self.driver.find_elements(By.XPATH,"//span[@data-ui-id='page-title-wrapper']")
     #span_tag=self.driver.find_element(By.XPATH,"//div[@class='page-wrapper']/main/div[@class='page-title-wrapper']/h1/span[@data-ui-id='page-title-wrapper']").text
     time.sleep(10)
     span_tag = self.driver.find_element(By.XPATH,"//*[contains(text(), 'Thank you for your purchase!')]")
     
     print(span_tag.text)
     return [msgLoc,ordersummarytext,orderSumDetail1.text +' '+ orderSumDetail2.text]

      

      