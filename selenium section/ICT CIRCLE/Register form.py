from telnetlib import EC

from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common import keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import wait

driver: WebDriver = webdriver.Firefox()
driver.maximize_window()
driver.implicitly_wait(5)
driver.get("https://www.ictcircle.com")


driver.find_element(By.CSS_SELECTOR, "img[alt='Cancel']").click()

driver.find_element(By.ID, 'signup').click()



u_name = driver.find_element(By.ID, 'first_name')
u_name.send_keys('lahari')
u_name = driver.find_element(By.ID, 'last_name')
u_name.send_keys('nalivela')
u_name = driver.find_element(By.ID, 'name')
u_name.send_keys('wmlit')
element= driver.find_element(By.CSS_SELECTOR, 'input[id="react-select-4-input"]')
element.send_keys("Distributor")
element.send_keys(Keys.ENTER)

element1= driver.find_element(By.ID, 'react-select-5-input')
element1.send_keys('India')
element1.send_keys(Keys.ENTER)
element2= driver.find_element(By.ID, 'react-select-6-input')
element2.send_keys('Andhra Pradesh')
element2.send_keys(Keys.ENTER)
u_name = driver.find_element(By.ID, 'email')
u_name.send_keys('nalivelalahari@gmail.com')
u_name = driver.find_element(By.ID, 'password')
u_name.send_keys('Wml@1234')
u_name = driver.find_element(By.ID, 'confirm-password')
u_name.send_keys('Wml@1234')
element3= driver.find_element(By.ID, 'react-select-7-input')
element3.send_keys('91 IN')
element3.send_keys(Keys.ENTER)
u_name = driver.find_element(By.ID, 'phone_number')
u_name.send_keys('9381248750')
element4= driver.find_element(By.ID, 'react-select-8-input')
element4.send_keys("Email")
element4.send_keys(Keys.ENTER)
check_box= driver.find_element(By.XPATH, '//input[@type="checkbox"][1]')
check_box.click()
u_name = driver.find_element(By.ID, 'submit')
u_name.click()


