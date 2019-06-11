from testdata.data import *

from selenium import webdriver
import pytest

# @pytest.fixture(scope="class")
@pytest.fixture(scope="session")
def test_launch_browser(request):
    global driver
    driver = webdriver.Chrome(MY_CHROME_PATH)
    driver.get(JENKIN_URL)
    driver.maximize_window()
    driver.implicitly_wait(30)

    request.cls.driver = driver

    yield
    driver.quit()