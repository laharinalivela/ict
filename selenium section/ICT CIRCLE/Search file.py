import time

import driver as driver
from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
driver: WebDriver = webdriver.Firefox()
driver.maximize_window()
driver.implicitly_wait(5)
driver.get("https://www.ictcircle.com")
driver.find_element(By.CSS_SELECTOR, "img[alt='Cancel']").click()
field= driver.find_element(By.ID, 'search')
field.send_keys('dell')
field.send_keys(Keys.ENTER)
driver.find_element(By.CSS_SELECTOR, "span[class='w-6 h-6  text-indigo-700']").click()
driver.find_element(By.CSS_SELECTOR, "a[class='relative flex items-center my-1 justify-center rounded-md border "
                                     "border-transparent bg-gray-100 px-8 py-2 text-sm font-medium text-gray-900"
                                     " hover:bg-gray-200']").click()
time.sleep(3)
driver.find_element(By.CSS_SELECTOR, 'button[class="flex flex-row items-center p-2  text-sm gap-1"]').click()
driver.implicitly_wait(10)

