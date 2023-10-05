
# import pdb

from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
driver: WebDriver = webdriver.Firefox()
driver.maximize_window()
driver.get("https://www.ictcircle.com/user/login")
u_name = driver.find_element(By.ID, 'email')
u_name.send_keys('nalivelalahari@gmail.com')
u_name = driver.find_element(By.ID, 'password')
u_name.send_keys('Wml@124')
u_name.clear()
u_name.send_keys('Wml@1234')

u_name = driver.find_element(By.ID, 'submit')
u_name.click()






















# u_name = driver.find_element(By.ID, 'forget_password')
# u_name.click()
# u_name = driver.find_element(By.ID, 'email')
# u_name.send_keys('nalivelalahari@gmail.com')
# u_name = driver.find_element(By.ID, 'submit')
# u_name.click()

# driver.get('')
# u_name = driver.find_element(By.ID, 'identifierId')
# u_name.send_keys('nalivelalahari@gmail.com')
# u_name.find_element(By.CLASS_NAME, 'VfPpkd-RLmnJb')
# u_name.click()
# u_name = driver.find_element(By.NAME, 'Passwd')
# u_name.send_keys('Lahari123@')
# u_name = driver.find_element(By.CLASS_NAME, 'VfPpkd-RLmnJb')
# u_name.click()
# u_name = driver.find_element(By.ID, 'password')
# u_name.send_keys('Wml@1234')
# u_name = driver.find_element(By.ID, 'confirm_password')
# u_name.send_keys('Wml@1234')
# u_name = driver.find_element(By.ID, 'submit')
# u_name.click()
# pdb.set_trace()
