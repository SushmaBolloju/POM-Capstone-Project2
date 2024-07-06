
from selenium.webdriver.common.by import By

class WebLocators:


   def __init__(self):
       self.usernameLocator = '//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[1]/div/div[2]/input'
       self.passwordLocator = '//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[2]/div/div[2]/input'
       self.buttonLocator = '//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button'
       self.adminlocator = "/html[1]/body[1]/div[1]/div[1]/div[1]/aside[1]/nav[1]/div[2]/ul[1]/li[1]/a[1]"
       self.menu_itemslocator = '/html/body/div/div[1]/div[1]/header/div[2]/nav/ul/li'
   def enterText(self, driver, locator, textValue):
       driver.find_element(by=By.XPATH, value=locator).send_keys(textValue)


   def clickButton(self, driver, locator):
       driver.find_element(by=By.XPATH, value=locator).click()