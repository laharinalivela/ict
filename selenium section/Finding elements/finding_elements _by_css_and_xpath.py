import pdb
import time

from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
driver: WebDriver = webdriver.Chrome()
driver.get("http://demostore.supersqa.com/")
# time.sleep(3)
# driver.quit()
pdb.set_trace()