from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from time import sleep
class Orange:
   def __init__(self, url):

       self.url = url
       self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

   def boot(self):

       self.driver.get(self.url)

       sleep(3)
       #Maximizing window
       self.driver.maximize_window()

   def quit(self):
       #Quiting function
       self.driver.quit()

   # Test case ID: TC_PIM_03
   def login(self):
       self.boot()
       sleep(3)
       try:
           username = self.driver.find_element(By.XPATH,
                                               '//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[1]/div/div[2]/input')
           # Passing the username value
           username.send_keys("Admin")
           password = self.driver.find_element(By.XPATH,
                                               '//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[2]/div/div[2]/input')
           # Passing the password
           password.send_keys("admin123")
           login_button = self.driver.find_element(By.XPATH,
                                                   '//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button')
           # Clicking on the login button
           login_button.click()
       except NoSuchElementException as e:
           print("Error")
       except Exception as e:
           # Handle other exceptions (TimeoutException, WebDriverException, etc.)
           print(f"An error occurred: {e}")

       # Test case ID: TC_PIM_03

   def menu_validation(self):
       sleep(5)
       try:
           admin = self.driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[1]/a/span')
           admin.click()
           sleep(5)
           main_menu_items_text = []
           main_menu_items = self.driver.find_elements(By.XPATH, '/html/body/div/div[1]/div[1]/aside/nav/div[2]/ul/li')
           for item in main_menu_items:
               print(item.text)
               main_menu_items_text.append(item.text)
           main_menu_options = ["Admin", "PIM", "Leave", "Time", "Recruitment", "My Info", "Performance", "Dashboard",
                                "Directory", "Maintenance", "Buzz"]
           for option_text in main_menu_options:
               assert option_text in main_menu_items_text
       finally:
           self.driver.quit()

   # Passing URL to the class Orange
obj = Orange("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
   # calling the function
obj.login()
obj.menu_validation()