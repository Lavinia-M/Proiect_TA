import time

from selenium import webdriver
from unittest import TestCase
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager


class FormAuthentication(TestCase):
    BASE_URL = "https://the-internet.herokuapp.com"
    FORM_AUTHENTICATION_SELECTOR = (By.XPATH, "//a[@href='/login']")
    LOGIN_BUTTON_SELECTOR = (By.XPATH, "//*[@id='login']/button")

    def setUp(self) -> None:
        self.browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.browser.get(self.BASE_URL)
        self.browser.maximize_window()
        self.browser.implicitly_wait(10)
        form_auth_link = self.browser.find_element(*self.FORM_AUTHENTICATION_SELECTOR)
        form_auth_link.click()

    def tearDown(self) -> None:
        self.browser.quit()

    def test_login(self):
        self.browser.find_element(by=By.ID, value="username").send_keys("Lavinia")
        self.browser.find_element(by=By.ID, value="password").send_keys("password")
        login_button = self.browser.find_element(*self.LOGIN_BUTTON_SELECTOR)
        login_button.click()
        error = self.browser.find_element(by=By.XPATH, value="//*[@id='flash']").text
        expected = "Your username is invalid!"
        self.assertTrue(expected in error, "Error in message text is incorrect")
        self.browser.implicitly_wait(3)
        time.sleep(2)
