from selenium import webdriver
from selenium.webdriver.chrome.options import Options

import time


chromedriver_path = "chromedriver-80"
electron_path = "/Users/davidortiz/net-check/out/Network-Status-Check-darwin-x64/Network-Status-Check.app/Contents/MacOS/Network-Status-Check"

opts = Options()
opts.add_argument("--remote-debugging-port=9222")
#opts.add_argument("--headless")
opts.add_argument("--disable-gpu")
opts.add_argument("--window-size=1920,1080")
opts.add_argument("--start-maximized")
opts.binary_location = electron_path

driver = webdriver.Chrome(executable_path=chromedriver_path, options=opts)

hostNameField = driver.find_element_by_id('hostname')
hostNameField.send_keys(str("https://google.com"))

portField = driver.find_element_by_id('port')
portField.send_keys(str(22))

addBtn = driver.find_element_by_css_selector('input.btn.btn-primary.add-row')
addBtn.click()

time.sleep(5)
driver.close()


# driver.get('https://google.com')

# searchInput = driver.find_element_by_class_name("gLFyf.gsfi")

# searchInput.click()
# searchInput.send_keys(str("Hello"))

# searchBtn = driver.find_element_by_class_name("gNO89b")
# searchBtn.click()
