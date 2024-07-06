
from selenium.webdriver.common.by import By

class WebLocators:


   def __init__(self):
       self.usernameLocator = '//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[1]/div/div[2]/input'
       self.forgot_passwordLocator = '//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[4]/p'
       self.usernameLocator1 = '//*[@id="app"]/div[1]/div[1]/div/form/div[1]/div/div[2]/input'
       self.resetLocator = '//*[@id="app"]/div[1]/div[1]/div/form/div[2]/button[2]'

   def enterText(self, driver, locator, textValue):
       driver.find_element(by=By.XPATH, value=locator).send_keys(textValue)


   def clickButton(self, driver, locator):
       driver.find_element(by=By.XPATH, value=locator).click()