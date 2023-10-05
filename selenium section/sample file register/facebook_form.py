import pdb
import random
import string

from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By

driver: WebDriver = webdriver.Chrome ( )

# driver.maximize_window()
# driver.get('https://rahulshettyacademy.com/')
# print(driver.title)
# print(driver.current_url)
# //input[@type='email']
driver.get ('https://rahulshettyacademy.com/seleniumPractise/#/')
driver.find_element (By.NAME, "email").send_keys ("hello@gmail.com")
driver.find_element (By.ID, "exampleInputPassword1").send_keys ("1234")
driver.find_element (By.ID, "exampleCheck1").click ( )

pdb.set_trace ( )
