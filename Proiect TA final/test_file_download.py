from selenium import webdriver
from unittest import TestCase
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager


class FileDownload(TestCase):
    BASE_URL = "https://the-internet.herokuapp.com"
    FILE_DOWNLOAD_SELECTOR = (By.XPATH, "//a[@href='/download']")

    def setUp(self) -> None:
        self.browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.browser.get(self.BASE_URL)
        self.browser.maximize_window()
        self.browser.implicitly_wait(5)
        file_download_link = self.browser.find_element(*self.FILE_DOWNLOAD_SELECTOR)
        file_download_link.click()

    def tearDown(self) -> None:
        self.browser.quit()

    def test_download_files(self):
        file_1 = self.browser.find_element(By.XPATH, '//*[@id="content"]/div/a[2]')
        file_1.click()

        file_2 = self.browser.find_element(By.XPATH, '//*[@id="content"]/div/a[7]')
        file_2.click()

        file_3 = self.browser.find_element(By.XPATH, '//*[@id="content"]/div/a[11]')
        file_3.click()

        file_4 = self.browser.find_element(By.XPATH, '//*[@id="content"]/div/a[21]')
        file_4.click()
