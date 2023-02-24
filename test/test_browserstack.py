



from src.pages.course_list_page import Course_List_Page
from selenium import webdriver
import time
import json
from src.pages.homepage import Homepage
from src.pages.class_room import Classroom

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait


driver = webdriver.Chrome()


def setup_module(module):
    # Create Chrome browser driver
    driver.get("https://hahow.in")
    driver.maximize_window()
    time.sleep(3)

    # 拿token
    with open("local_storage.yaml", "r") as f:
        local_storage = json.load(f)
        token = local_storage["satellizer_token"]
    driver.execute_script(f'window.localStorage.setItem("satellizer_token", "{token}")')
    driver.get("https://hahow.in")
    time.sleep(5)


def test_1():
    """
登入>從首頁>點擊探索>進入課程
    """
    homepage = Homepage(driver)
    homepage.close_ad_button()
    course_page = Course_List_Page(driver)
    course_page.click_explore()

    course_page.go_to_course()





def test2():
    """

    登入情況 在課程頁收藏課程
    登入情況 在課程頁 留言
    """
    classroom = Classroom(driver)
    classroom.play_video()
    # classroom.adjust_sound_volume()
    classroom.bookmark_course_in_classroom()

    #
    classroom.click_chart()
    # classroom.send_qa_message("cool")




def teardown_module(module):
    """
    这是一个module级别的teardown，它会在本module(test_website.py)里
    所有test执行完成之后，被调用一次。
    注意，它是直接定义为一个module里的函数"""
    driver.close()
    print("-------------- teardown after module --------------")


