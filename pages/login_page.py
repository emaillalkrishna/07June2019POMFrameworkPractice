import time
from testdata.data import *


class JenkinLogin:

    def __init__(self, driver):
        self.driver = driver
        self.locate_un_by_name = "j_username"
        self.locate_pn_by_name = "j_password"
        self.locate_signin_button_by_name = "Submit"

    def enter_username(self):
        self.driver.find_element_by_name(self.locate_un_by_name).send_keys(UN)
        time.sleep(2)

    def enter_password(self):
        self.driver.find_element_by_name(self.locate_pn_by_name).send_keys(PW)
        time.sleep(2)

    def click_signinbutton(self):
        self.driver.find_element_by_name(self.locate_signin_button_by_name).click()
        time.sleep(5)
