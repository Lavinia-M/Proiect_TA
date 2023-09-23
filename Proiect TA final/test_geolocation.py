import time

from selenium import webdriver
from unittest import TestCase
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager


class Geolocation(TestCase):
    BASE_URL = "https://the-internet.herokuapp.com"
    GEOLOCATION_SELECTOR = (By.XPATH, "//a[@href='/geolocation']")

    def setUp(self) -> None:
        self.browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.browser.get(self.BASE_URL)
        self.browser.maximize_window()
        self.browser.implicitly_wait(10)
        geolocation_link = self.browser.find_element(*self.GEOLOCATION_SELECTOR)
        geolocation_link.click()

    def tearDown(self) -> None:
        self.browser.quit()

    def test_where_am_i(self):
        self.browser.find_element(By.TAG_NAME, 'button').click()
        time.sleep(1)
        self.browser.find_element(By.ID, "map-link").click()
        time.sleep(2)

