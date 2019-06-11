class JenkinLogout:
    def __init__(self, driver):
        self.driver = driver
        self.locate_logout_button_by_xpath = "//*[text()='log out']"

    def click_on_logout(self):
        self.driver.find_element_by_xpath(self.locate_logout_button_by_xpath).click()

