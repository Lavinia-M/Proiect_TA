import time

from selenium import webdriver
from unittest import TestCase
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager


class Alerts(TestCase):
    JAVASCRIPT_ALERTS_URL = "https://the-internet.herokuapp.com/javascript_alerts"
    ALERT_BUTTON_SELECTOR = (By.XPATH, "//ul/li[1]/button")
    CONFIRM_BUTTON_SELECTOR = (By.XPATH, "//ul/li[2]/button")
    PROMPT_BUTTON_SELECTOR = (By.XPATH, "//ul/li[3]/button")
    RESULT_SELECTOR = (By.ID, "result")

    def setUp(self) -> None:
        self.browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.browser.get(self.JAVASCRIPT_ALERTS_URL)
        self.browser.maximize_window()
        self.browser.implicitly_wait(10)

    def tearDown(self) -> None:
        self.browser.quit()

    def test_simple_alert(self):
        alert_button = self.browser.find_element(*self.ALERT_BUTTON_SELECTOR)
        alert_button.click()

        alert_window = self.browser.switch_to.alert
        alert_window.accept()
        time.sleep(2)

        result = self.browser.find_element(*self.RESULT_SELECTOR)
        assert result.text == "You successfully clicked an alert"

    def test_confirm_ok(self):
        confirm_button = self.browser.find_element(*self.CONFIRM_BUTTON_SELECTOR)
        confirm_button.click()

        confirm_window = self.browser.switch_to.alert
        confirm_window.accept()
        time.sleep(2)

        result = self.browser.find_element(*self.RESULT_SELECTOR)
        assert result.text == "You clicked: Ok"

    def test_confirm_cancel(self):
        confirm_button = self.browser.find_element(*self.CONFIRM_BUTTON_SELECTOR)
        confirm_button.click()

        confirm_window = self.browser.switch_to.alert
        confirm_window.dismiss()
        time.sleep(2)

        result = self.browser.find_element(*self.RESULT_SELECTOR)
        assert result.text == "You clicked: Cancel"

    def test_prompt_ok(self):
        prompt_button = self.browser.find_element(*self.PROMPT_BUTTON_SELECTOR)
        prompt_button.click()

        prompt_window = self.browser.switch_to.alert
        prompt_window.send_keys("Hello! Welcome to our website!")
        prompt_window.accept()
        time.sleep(2)

        result = self.browser.find_element(*self.RESULT_SELECTOR)
        assert result.text == "You entered: Hello! Welcome to our website!"

    def test_prompt_cancel(self):
        prompt_button = self.browser.find_element(*self.PROMPT_BUTTON_SELECTOR)
        prompt_button.click()

        prompt_window = self.browser.switch_to.alert
        prompt_window.dismiss()
        time.sleep(2)

        result = self.browser.find_element(*self.RESULT_SELECTOR)
        assert result.text == "You entered: null"
