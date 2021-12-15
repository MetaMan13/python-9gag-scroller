from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from dotenv import load_dotenv
from termcolor import colored
import time
import os


def enterTopic():
    topic = input('Please enter a 9gag topic: ')
    topic = urls.get(topic)
    return topic


# Driver setup
driver_options = webdriver.ChromeOptions()
driver_options.add_argument('--ignore-certificate-errors')
driver_options.add_argument('--ignore-certificate-errors-spki-list')
driver_options.add_argument('--ignore-ssl-errors')

urls = {
    'funny': 'https://9gag.com/funny',
    'funny-fresh': 'https://9gag.com/funny/fresh',
    'nsfw': 'https://9gag.com/nsfw',
    'nsfw-fresh': 'https://9gag.com/nsfw',
    'girl': 'https://9gag.com/girl',
    'girl-fresh': 'https://9gag.com/girl/fresh',
    'wtf': 'https://9gag.com/wtf',
    'wtf-fresh': 'https://9gag.com/wtf/fresh',
    'cryptocurrency': 'https://9gag.com/cryptocurrency',
    'cryptocurrency-fresh': 'https://9gag.com/cryptocurrency/fresh',
    'anime-and-manga': 'https://9gag.com/anime-manga/fresh',
    'anime-and-manga-fresh': 'https://9gag.com/anime-manga/fresh',
    'random': 'https://9gag.com/random',
    'random-fresh': 'https://9gag.com/random/fresh',
    'animals': 'https://9gag.com/animals',
    'animals-fresh': 'https://9gag.com/animals/fresh',
}

print('\n' + colored('Available 9gag topics:',
      'green', None, ['dark', 'underline']) + '\n')
for i, url in enumerate(urls):
    print(colored('[' + url + '] => ', 'yellow') + urls.get(url))

url = enterTopic()

while(url == None):
    print(colored('Sorry that topic is not available, please choose again!', 'red'))
    url = enterTopic()

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
