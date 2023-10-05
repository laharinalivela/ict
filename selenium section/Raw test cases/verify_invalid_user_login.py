from selenium import webdriver
from selenium.webdriver.common.by import By
import time


class InvalidUserLoginError:
    url: str = 'http://demostore.supersqa.com/my-account/'

    invalid_email = 'abc@supersqa.com'

    def __int__(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)
        time.sleep(2)

    def InvalidUserLoginError(self):
        self.driver.get(self.url)

    def input_email(self):
        field = self.driver.find_element((By.ID, 'username'))
        field.send_keys(self.invalid_email)

    def input_password(self):
        field = self.driver.find_element(By.ID, 'password')
        field.send_keys('abcdefg')

    def click_login(self):
        self.driver.find_element(By.NAME, 'lo gin').click()

    def verify_error_message(self):
        pass

    def main(self):
        self.InvalidUserLoginError()
        self.input_email()
        self.input_password()
        time.sleep(2)
        self.click_login()
        self.verify_error_message()
        # self.driver.quit()


if __name__ == '__main__':
    obj = InvalidUserLoginError()
    obj.main()