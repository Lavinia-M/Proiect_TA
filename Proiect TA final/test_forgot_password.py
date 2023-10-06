from selenium import webdriver
from unittest import TestCase
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager


class ForgotPassword(TestCase):
    BASE_URL = "https://the-internet.herokuapp.com"
    FORGOT_PASS_SELECTOR = (By.XPATH, "//a[@href='/forgot_password']")
    RETRIEVE_PASS_SELECTOR = (By.ID, "form_submit")

    def setUp(self) -> None:
        self.browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.browser.get(self.BASE_URL)
        self.browser.maximize_window()
        self.browser.implicitly_wait(5)
        forgot_pass_link = self.browser.find_element(*self.FORGOT_PASS_SELECTOR)
        forgot_pass_link.click()

    def tearDown(self) -> None:
        self.browser.quit()

    def test_forgot_password(self):
        self.browser.find_element(by=By.ID, value="email").send_keys('lavinia.m@yahoo.com')
        retrieve_pass_button = self.browser.find_element(*self.RETRIEVE_PASS_SELECTOR)
        retrieve_pass_button.click()
        error = self.browser.find_element(by=By.XPATH, value="/html/body/h1").text
        expected = "Internal Server Error"
        self.assertTrue(expected in error)
        self.browser.implicitly_wait(3)
        
