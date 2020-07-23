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
# adds the first url list
time.sleep(3)
hostNameField = driver.find_element_by_id('hostname')
time.sleep(3)
hostNameField.send_keys(str('https://google.com'))
time.sleep(3)
portField = driver.find_element_by_id('port')
portField.send_keys(str(22))
time.sleep(3)
addBtn = driver.find_element_by_css_selector('input.btn.btn-primary.add-row')
addBtn.click()

# adds a second url list
time.sleep(3)
hostNameField = driver.find_element_by_id('hostname')
time.sleep(2)
hostNameField.clear()
hostNameField.send_keys(str('saucelabs'))
time.sleep(3)
portField = driver.find_element_by_id('port')
portField.clear()
time.sleep(2)
portField.send_keys(str(4446))
time.sleep(3)
addBtn = driver.find_element_by_css_selector('input.btn.btn-primary.add-row')
addBtn.click()

# deletes a row
time.sleep(2)
checkBox = driver.find_element_by_name('record')
checkBox.click()
time.sleep(2)
deleteRow = driver.find_element_by_class_name('delete-row')
deleteRow.click()

# selects left nav list
time.sleep(3)
loadUrls = driver.find_element_by_id('load-urls')
loadUrls.click()
time.sleep(2)
submit = driver.find_element_by_id('loadurls_submit')
submit.click()

# selects run check
time.sleep(3)
runCheck = driver.find_element_by_id('runcheck')
runCheck.click()
time.sleep(5)

# selects save list from left nav
time.sleep(3)
saveList = driver.find_element_by_id('convert-table')
saveList.click()
time.sleep(3)
close = driver.find_element_by_class_name('.btn.btn-primary')
close.click()


driver.close()
