import time

from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import wait, expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver: WebDriver = webdriver.Firefox()
driver.maximize_window()
driver.implicitly_wait(5)

driver.get('https://rahulshettyacademy.com/seleniumPractise/#/cart')
driver.find_element(By.CSS_SELECTOR, "search-keyword").send_keys("ber")
time.sleep(2)
results: WebElement = driver.find_element(By.XPATH, "//div[@class='products']/div")
count = len(results)
assert count > 0
for result in results:
    result.find_element(By.XPATH, 'div/button').click()

driver.find_element(By.CSS_SELECTOR, 'img[alt="cart"]').click()
driver.find_element(By.XPATH, "//button[text()='PROCEED TO CHECKOUT']").click()

# some validations
prices = driver.find_element(By.CSS_SELECTOR, "td:nth-child(5) p")
sum = 0
for price in prices:
    sum = sum + int(price.text)
price(sum)
totalAmount = int(driver.find_element(By.CSS_SELECTOR, ".totAmt").text)


driver.find_element(By.CSS_SELECTOR, ".promoCode").send_keys("rahulshettyacademy")
driver.find_element(By.CSS_SELECTOR, ".promoBtn").click()
wait = WebDriverWait(driver, 10)
wait.until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR, ".promoInfo")))
print(driver.find_element(By.CLASS_NAME, "promoInfo").text)