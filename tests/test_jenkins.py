import time
import pytest

from conftest import test_launch_browser
from pages.login_page import JenkinLogin
from pages.home_page import JenkinLogout


@pytest.mark.usefixtures(test_launch_browser)
class Test_Jenkins_Login_Logout:

    def test_login(self):
        driver = self.driver
        lp = JenkinLogin(driver)
        lp.enter_username()
        lp.enter_password()
        lp.click_signinbutton()
        time.sleep(3)

    def test_logout(self):
        driver = self.driver
        hp = JenkinLogout(driver)
        hp.click_on_logout()

