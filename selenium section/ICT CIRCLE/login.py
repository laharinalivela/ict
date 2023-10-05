import time

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
driver: WebDriver = webdriver.Firefox()
driver.maximize_window()
driver.implicitly_wait(5)
driver.get("https://www.ictcircle.com/user/login")

driver.find_element(By.XPATH, "//input[@name='email']").send_keys('nalivelalahari@gmail.com')
driver.find_element(By.XPATH, "//input[@name='password']").send_keys("Wml@1234")
driver.find_element(By.XPATH, "(//button[normalize-space()='Login'])[1]").click()
# u_name = driver.find_element(By.ID, 'forget_password')
# u_name.click()
# u_name = driver.find_element(By.ID, 'email')
# u_name.send_keys('nalivelalahari@gmail.com')
# # driver.find_element(By.ID, 'submit').click()
# driver.find_element(By.XPATH, "//a[class='font-medium text-indigo-600 hover:text-indigo-500']").click()
time.sleep(3)
field= driver.find_element(By.ID, 'search')
field.send_keys('dell')
field.send_keys(Keys.ENTER)

driver.find_element(By.CSS_SELECTOR, "span[class='w-6 h-6  text-indigo-700']").click()

driver.find_element(By.CSS_SELECTOR, 'svg[class="h-5 w-5 my-auto text-gray-800"]').click()