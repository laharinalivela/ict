import time

from selenium import webdriver


driver = webdriver.Chrome()


driver.get("https://www.ictcircle.com/dashboard")
time.sleep(3000000000)

my_acct_tab = driver.find_element_by_link_text("analytics")
my_acct_tab.click()
time.sleep(40000000000)