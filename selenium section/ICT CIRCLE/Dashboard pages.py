import pdb

from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By

driver: WebDriver = webdriver.Chrome()
driver.get("https://www.ictcircle.com/")
u_name = driver.find_element(By.ID, 'about')
print(u_name, 11111111111111)
u_name.click()

u_name = driver.find_element(By.ID, '1')
u_name.click()
u_name = driver.find_element(By.ID, '#\31 ')
u_name.click()

# u_name = driver.find_element(By.ID, 'email')
# u_name.send_keys('nalivelalahari@wmltech.com')
# u_name = driver.find_element(By.ID, 'subscribe')
# u_name.click()


pdb.set_trace()
