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
        self.browser.implicitly_wait(5)
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

    def test_text_label(self):
        list_login = self.browser.find_elements(By.XPATH, '//label')
        self.assertEqual(list_login[0].text, 'Username', 'Username text is incorrect')
        self.assertEqual(list_login[1].text, 'Password', 'Password text incorrect')

    def test_find_correct_password(self):
        self.browser.find_element(by=By.ID, value="username").send_keys("tomsmith")
        h4_element = self.browser.find_element(by=By.XPATH, value="//h4[@class='subheader']")
        h4_element_text = h4_element.text
        list_words = h4_element_text.split(" ")  # 30 words
        for i in range(len(list_words)):
            self.browser.refresh()
            self.browser.implicitly_wait(5)
            self.browser.find_element(by=By.ID, value="username").send_keys("tomsmith")
            self.browser.find_element(by=By.ID, value="password").send_keys(f"{list_words[i]}")
            self.browser.find_element(by=By.XPATH, value="//button[@type='submit']").click()
            if self.browser.current_url == "https://the-internet.herokuapp.com/secure":
                print(f"\n The secret password is [{list_words[i]}].")
                break
            elif i == len(list_words) - 1:
                print("\n I couldn't find the password!")

