from seleniumpagefactory.Pagefactory import PageFactory
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import random


class Course_List_Page(PageFactory):

    def __init__(self, driver):
        self.driver = driver
        self.wait =WebDriverWait(self.driver, 10)


    locators = {
        "free_filter": (By.XPATH, "//a[contains(text(),'免費')]"),
        "course_elements": (By.CSS_SELECTOR, ".css-r2al97"),
        "explore_button": (By.XPATH, "//*[@id='header']/nav/div/div[2]/div/ul[1]/li[1]/div/div"),
        "click_all_courses":(By.XPATH, "//span[text()='所有影音課程']"),
        "click_hot_course":(By.XPATH,"//*[@id='main-screen']/div/div[1]/div[1]/div[1]/a[1]"),
        "course":(By.CSS_SELECTOR,"#main-screen > div > div.container > div:nth-child(2) > div > div > div")



    }

    def click_explore(self):
        """

       點擊探索>進入所有課程
        """
        self.explore_button.click()
        time.sleep(2)
        self.driver.find_element(*self.locators["click_all_courses"]).click()
        time.sleep(2)
        return self



    def go_to_course(self):
        """

        在所有課程介面沒能點擊 收藏成功

        """
        # self.driver.get("https://hahow.in/courses?page=1&campaign=HOT")

        self.driver.find_element(*self.locators["click_hot_course"]).click()
        time.sleep(3)
        ##先找到父節點
        course= self.driver.find_element(*self.locators["course"])
        ##在找到子節點
        enter_cards =course.find_elements(By.CLASS_NAME,"sc-10r5mg2-0")

        time.sleep(4)
        #隨機取得一門課程
        random_index = random.randint(0, len(enter_cards) - 1)
        card = enter_cards[random_index]
        time.sleep(3)
        #找到課程的課程名稱
        course_title_ele = card.find_element(By.TAG_NAME,'h4').text
        print(course_title_ele)

        card.click()
        time.sleep(3)
        #找到classroom的課程名稱
        course_title_in_class = self.driver.find_element(By.TAG_NAME, 'h1').text
        print(course_title_in_class)
        #確認課程名稱是否正確
        assert course_title_in_class == course_title_ele
        return self












