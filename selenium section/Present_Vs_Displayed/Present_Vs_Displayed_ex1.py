import pdb

from selenium import webdriver

driver = webdriver.Chrome()
driver.implicitly_wait(5)
url = 'file:///C:/Users/Administrator/Desktop/QA%20Automation/selenium%20section/Present_Vs_Displayed/' \
      'Present_Vs_Displayed.html'
driver.get(url)
my_btn1 = driver.find_element('id', 'btn1')
my_btn1_txt = my_btn1.text
print('First button text: {}'.format(my_btn1_txt))
my_btn2 = driver.find_element('id', 'btn2')
my_btn2_txt = my_btn1.text
print('Second button text: {}'.format(my_btn2_txt))
my_btn3 = driver.find_element('id', 'btn3')
my_btn3_txt = my_btn3.text
print('First button text: {}'.format(my_btn3_txt))

pdb.set_trace()
