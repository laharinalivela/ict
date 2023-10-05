# import time

from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
driver: WebDriver = webdriver.Firefox()
driver.maximize_window()
driver.implicitly_wait(5)
driver.get("https://www.ictcircle.com")


driver.find_element(By.CSS_SELECTOR, "img[alt='Cancel']").click()


# driver.find_element(By.CSS_SELECTOR, 'button[class="text-gray-900 bg-white border border-gray-300 focus:outline-none '
#                                      'hover:bg-gray-100 focus:ring-0  font-medium rounded-lg text-sm px-3 py-2.5 mr-2 '
#                                      'dark:bg-gray-800  dark:text-white dark:border-gray-600 dark:hover:bg-gray-700 '
#                                      'dark:hover:border-gray-600"]').click()
# driver.find_element(By.CSS_SELECTOR, "a[class='w-full px-6 py-3 bg-[#7f56d9] hover:bg-[#6141a5] dark:text-white"
#                                      " font-medium rounded-lg flex space-x-3 justify-center md:ml-5 lg:ml-0 ']").
#                                      click()


# driver.find_element(By.CSS_SELECTOR, "div[type='submit']").click()

# driver.find_element(By.CSS_SELECTOR, "div[class='px-6 py-3 text-center rounded-full border font-medium   text-white "
#                                      " w-2/3 text-xl font-poppins  bg-[#0ba5ec]']").click()

# driver.find_element(By.ID, 'zsiq_agtpic').click()
# driver.find_element(By.CSS_SELECTOR, 'input[class="sbold"]').send_keys('Lahari Nalivela')






# business_types =driver.find_element(By.ID, 'react-select-4-input')
# business_types.send_keys('Reseller')
#
# for business_type in business_types:
#     if business_type.text == "Reseller":
#         business_type.click()
#         break
#
# time.sleep(2)

