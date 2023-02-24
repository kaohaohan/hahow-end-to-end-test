from seleniumpagefactory.Pagefactory import PageFactory, TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Homepage(PageFactory):
    def __init__(self, driver):
        self.wait = WebDriverWait(driver, 10)
        self.driver = driver

    locators = {
        "sign_in": (By.XPATH, "//*[@id='header']/nav/div/div[2]/div/ul[2]/li[2]/a"),
        "email_input": (By.NAME, "email"),
        "password_input": (By.XPATH, "//input[@type='password']"),
        "submit_button": (By.CSS_SELECTOR, "form button[type='submit']"),
        "user_name": (By.XPATH, "/html/body/div[6]/div/div/div/div/div/form/div[1]/div/div/input"),
        "free_filter": (By.XPATH, "//a[contains(text(),'免費')]"),
        "course_elements": (By.CSS_SELECTOR, ".css-r2al97"),
        "close_ad_button": (By.XPATH, "//*[@id='close-button-1454703513202']/span")
    }


    def click_sign_in(self):
        """
        點擊登入頁面

        """
        self.sign_in.click()
        time.sleep(3)
        return self

    def login(self, username, password):
        """

        登入user和密碼 點擊送出
        """
        self.driver.find_element(*self.locators["user_name"]).send_keys(username)
        self.driver.find_element(*self.locators["password_input"]).send_keys(password)
        self.driver.find_element(*self.locators["submit_button"]).click()
        time.sleep(3)
        return self

    def close_ad_button(self):
        """

        關掉廣告
        """
        try:
            ad_close_button = self.wait.until(
                EC.element_to_be_clickable((By.XPATH, "//*[@id='close-button-1454703513202']/span")))
            if ad_close_button.is_displayed():
                ad_close_button.click()
        except TimeoutException:
            pass




