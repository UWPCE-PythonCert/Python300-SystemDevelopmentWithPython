import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox()
url = "http://localhost:8000/slides/index.html"
driver.get(url)
assert "Isilon" in driver.title

body = driver.find_element_by_xpath('//body')
body.send_keys(Keys.ARROW_RIGHT)
body.send_keys(Keys.ARROW_RIGHT)
body.send_keys(Keys.ARROW_RIGHT)
body.send_keys(Keys.ARROW_RIGHT)

time.sleep(1)
elem = driver.find_element_by_id("selenium")
assert "Selenium" in elem.text
driver.close()
