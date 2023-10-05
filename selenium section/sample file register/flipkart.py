import time

from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
driver: WebDriver = webdriver.Firefox()
driver.maximize_window()
# driver.get('https://www.flipkart.com/account/login?ret=%2Faccount%2F%3Frd%3D0%26link%3Dhome_account')
#
# driver.find_element(By.CSS_SELECTOR, "input[class='_2IX_2- VJZDxU']").send_keys('9381248750')
#
# driver.find_element(By.CSS_SELECTOR, "button[class='_2KpZ6l _2HKlqd _3AWRsL']").click()
#
# time.sleep(4)
#
# driver.find_element(By.CSS_SELECTOR, "button[class='_2KpZ6l _14EHzR _3dESVI']").click()

driver.get('https://www.flipkart.com/')
