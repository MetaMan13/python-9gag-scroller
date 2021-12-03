from selenium import webdriver
import time

# Driver setup
driver_options = webdriver.ChromeOptions()
driver_options.add_argument('--ignore-certificate-errors')
driver_options.add_argument('--ignore-certificate-errors-spki-list')
driver_options.add_argument('--ignore-ssl-errors')

# Accept website url
url = input('Enter website link: ')

# Start selenium slow scroller
driver = webdriver.Chrome('chromedriver.exe', options=driver_options)
driver.set_window_position(-2000, 0)
driver.maximize_window()
driver.get(url)

current_window_position = 0

while True:
    # driver.execute_script("window.scrollTo(0, 800);")
    driver.execute_script("window.scrollTo(" + str(current_window_position) + ", " + str((current_window_position + 400)) + ");")
    current_window_position = current_window_position + 500
    time.sleep(5)
