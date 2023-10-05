from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Replace 'your_url_here' with the actual URL of the webpage containing the dropdown
driver = webdriver.Chrome()
driver.get('https://www.ictcircle.com/user/signup')

# Replace 'Your_XPath' with the correct XPath expression to identify the dropdown element
dropdown_xpath = "react-select-4-input"

# Wait until the dropdown is visible (you can use any other suitable expected condition)
wait = WebDriverWait(driver, 10)
dropdown = wait.until(EC.visibility_of_element_located((By.XPATH, dropdown_xpath)))

# Use the Select class to work with the dropdown
select = Select(dropdown)

# You can select by index, value, or visible text
# Example: Selecting by index (indexing starts from 0)
select.select_by_index(1)  # This will select "Option 2"

# Example: Selecting by value
select.select_by_value("option3")  # This will select "Option 3"

# Example: Selecting by visible text
select.select_by_visible_text("Option 1")  # This will select "Option 1"

# Close the browser when done
driver.quit()
