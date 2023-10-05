#
#
# from selenium import webdriver
# from selenium.webdriver.chrome.webdriver import WebDriver
# from selenium.webdriver.common.by import By
# driver: WebDriver = webdriver.Firefox()
# driver.maximize_window()
# driver.implicitly_wait(2)
# driver.get("https://the-internet.herokuapp.com/windows")
#
# driver.find_element(By.CSS_SELECTOR, "a[href='/windows/new']").click()
#
# # windowsOpened = driver.window_handles
# #
# # driver.switch_to.window(windowsOpened[1])
# print(driver.find_element(By.TAG_NAME, 'h3').text)
from driver import driver

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# Assuming you have already initialized the driver.
# driver = webdriver.Chrome()

# Navigate to the page where the element is present

try:
    # Wait for the element to be clickable (maximum 10 seconds)
    wait = WebDriverWait(driver, 10)
    element = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "a[href='/windows/new']")))

    # Click the element
    element.click()
except Exception as e:
    print(f"An error occurred: {e}")
