
from selenium import webdriver

from selenium.webdriver import ActionChains

from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By


driver: WebDriver = webdriver.Firefox()
driver.implicitly_wait(5)
driver.get("https://rahulshettyacademy.com/AutomationPractice/")

action = ActionChains(driver)

action.move_to_element(driver.find_element(By.CSS_SELECTOR, 'div[class="mouse-hover"]')).perform()

action.context_click(driver.find_element(By.LINK_TEXT, "Top")).perform()