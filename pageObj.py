from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
import pytest
from pages.MainPage import MainPage

   
def test_menus():
  options = webdriver.ChromeOptions()
  options.add_experimental_option("detach", True)
  driver = webdriver.Chrome(options=options)
  driver.implicitly_wait(10)
  driver.maximize_window()
  driver.get("https://magento.softwaretestingboard.com/")
  action = ActionChains(driver)
  #creating the object of mainpage from mainpage class and call to locators method
  menuObj=MainPage(driver,action)     
    #the locators method returns a list object with 3 items as mentioned in the assertion
    
  listobj= menuObj.Locators()  
  #validate order summary    
  assert listobj[0]=="You added Olivia 1/4 Zip Light Jacket to your shopping cart."
  assert listobj[1]=="Order Summary"
  assert listobj[2]=="1 Item in Cart"
 # assert listobj[3]=="Thank you for your purchase!"

 # last_msg=menuObj.shippinglocators()   
  
  