from selenium import webdriver
from selenium.common import NoSuchElementException
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

       # Test case ID: TC_PIM_02

   def adminpage(self):
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
            loginbutton = self.driver.find_element(By.XPATH,
                                              '//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button')
       # Clicking on the login button
            loginbutton.click()
            sleep(5)
            admin = self.driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[1]/a/span')
            admin.click()
            sleep(5)
       # Get the title of the webpage
            title = self.driver.title
       # Validate the title
            expected_title = "OrangeHRM"
            if expected_title in title:
                print("Page title validation successful: Title is OrangeHRM")
            else:
                print("Page title validation failed: Title is not OrangeHRM")
            sleep(5)
            usermanagement = self.driver.find_element(By.XPATH,
                                                 '//*[@id="app"]/div[1]/div[1]/header/div[2]/nav/ul/li[1]/span')
            usermanagement.click()
            sleep(5)
            job = self.driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[1]/header/div[2]/nav/ul/li[2]/span')
            job.click()
            sleep(5)
            organ = self.driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[1]/header/div[2]/nav/ul/li[3]/span')
            organ.click()
            sleep(5)
            qualification = self.driver.find_element(By.XPATH,
                                                '//*[@id="app"]/div[1]/div[1]/header/div[2]/nav/ul/li[4]/span')
            qualification.click()
            sleep(5)
            Nationality = self.driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[1]/header/div[2]/nav/ul/li[5]')
            Nationality.click()
            sleep(5)
            corp = self.driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[1]/header/div[2]/nav/ul/li[6]')
            corp.click()
            sleep(5)
            config = self.driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[1]/header/div[2]/nav/ul/li[7]')
            config.click()
            sleep(5)

       except NoSuchElementException as e:
            print("Error")

       except Exception as e:
# Handle other exceptions (TimeoutException, WebDriverException, etc.)
           print(f"An error occurred: {e}")

       finally:
          self.driver.quit()
   # Passing URL to the class Orange
obj = Orange("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
   # calling the function
obj.adminpage()
