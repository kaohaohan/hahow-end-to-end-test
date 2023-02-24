from seleniumpagefactory.Pagefactory import PageFactory
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains


class Classroom(PageFactory):

    def __init__(self, driver):
        self.driver = driver



    locators = {
        "bookmark_course": (By.XPATH,"//*[@id='main-screen']/div/div[2]/div[1]/div[3]/div[1]/a[3]" ),
        "click_chart":(By.XPATH,"//*[@id='main-screen']/div/div[2]/div[1]/div[3]/div[2]/button[2]/span"),
        "qa_button": (By.XPATH, "//*[@id='main-screen']/div/div[6]/div/div[4]/div/div/div[2]/div[1]/div/div[2]/div[2]/textarea"),
        "qa_send_button": (By.XPATH, "//button[text()='留言']"),
        "play_video":(By.XPATH,"//*[@id='main-screen']/div/div[1]/div[1]/div[2]/div[1]/div/div/div[1]/div[2]/div[1]/button[2]"),
        "volume_slider": (By.ID, "plyr-volume-6286")



    }

    def bookmark_course_in_classroom(self):
        """
       點擊收藏
        """

        time.sleep(3)
        self.driver.execute_script("window.scrollBy(0, 400)")
        time.sleep(3)
        # self.wait.until(EC.presence_of_element_located(self.locators["bookmark_course"]))
        element = self.driver.find_element(*self.locators["bookmark_course"])
        ActionChains(self.driver).move_to_element(element).perform()
        element.click()
        time.sleep(3)
        return self





    def click_chart(self):
        """

        點擊購物車
        """
        self.driver.find_element(*self.locators["click_chart"]).click()
        time.sleep(5)
        return self

    def play_video(self):
        """

        點擊播放影片
        """
        self.driver.get("https://hahow.in/courses/627387c6f91c780007db0e2b/main")
        time.sleep(3)
        self.driver.find_element(*self.locators["play_video"]).click()
        time.sleep(5)
        return self

    def adjust_sound_volume(self):
        """

    還弄不出來
        """
        self.driver.get("https://hahow.in/courses/627387c6f91c780007db0e2b/main")
        # Find the volume slider element and its current position
        slider = self.wait.until(EC.presence_of_element_located((By.ID, "plyr-volume-6286")))

        slider.click_and_hold().move_by_offset(50, 0).release().perform()
        time.sleep(3)

        return self

    def send_qa_message(self,message):
        """
        購課前問答留言

        """
        self.driver.execute_script("window.scrollBy(0, 1000)")
        time.sleep(5)

        # 點擊"購課前問答"按钮並留言再送出
        self.driver.find_element(*self.locators["qa_button"]).send_keys(message)
        self.driver.find_element(*self.locators["qa_send_button"]).click()
        time.sleep(10)