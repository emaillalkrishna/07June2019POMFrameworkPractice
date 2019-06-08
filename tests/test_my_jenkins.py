from selenium import webdriver
import time
import pytest


@pytest.fixture(scope="session")
def test_launch_browser():
    global driver
    driver = webdriver.Chrome(executable_path="C:/Users/LAL KRISHNA/PycharmProjects/15may2019/drivers/chromedriver.exe")
    driver.get("http://localhost:8080/login?from=%2F")
    driver.maximize_window()
    driver.implicitly_wait(30)

def test_login(test_launch_browser):
    driver.find_element_by_name("j_username").send_keys("admin")
    driver.find_element_by_name("j_password").send_keys("manager")
    driver.find_element_by_name("Submit").click()
    time.sleep(5)


def test_logout(test_launch_browser):
    driver.find_element_by_xpath("//*[text()='log out']").click()
