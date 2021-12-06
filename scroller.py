from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from dotenv import load_dotenv
import time
import os

# Driver setup
driver_options = webdriver.ChromeOptions()
driver_options.add_argument('--ignore-certificate-errors')
driver_options.add_argument('--ignore-certificate-errors-spki-list')
driver_options.add_argument('--ignore-ssl-errors')

# Accept website url
# url = input('Enter website link: ')
url = 'https://9gag.com/funny'

# Load enviorment variables
load_dotenv()
email = os.environ.get('EMAIL')
password = os.environ.get('PASSWORD')

# Start selenium slow scroller
driver = webdriver.Chrome('chromedriver.exe', options=driver_options)
driver.set_window_position(-2000, 0)
driver.maximize_window()
driver.implicitly_wait(30)
driver.get(url)

# Login functionality START

# Locate login button and click on it
login_button = driver.find_element_by_xpath('//a[@href="/login"]')
login_button.click()

# Locate email input and enter email
email_input = driver.find_element_by_id('login-email-name')
email_input.send_keys(email)

# Locate password input and enter password
password_input = driver.find_element_by_id('login-email-password')
password_input.send_keys(password)

# Login button click
login_submit_button = driver.find_element_by_xpath('//input[@type="submit"]')
login_submit_button.click()

# Login functionality END

# Scrolling functionality START
current_window_position = 0

while True:
    # driver.execute_script("window.scrollTo(0, 800);")
    driver.execute_script("window.scrollTo(" + str(current_window_position) +
                          ", " + str((current_window_position + 500)) + ");")
    current_window_position = current_window_position + 500
    time.sleep(5)

# Scrolling functionality END
