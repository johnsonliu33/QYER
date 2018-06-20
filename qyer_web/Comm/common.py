import time
import allure
from selenium.webdriver.support.wait import WebDriverWait

class Comm(object):
    # 初始化driver
    def __init__(self,driver):
        self.driver = driver


    # 单个元素定位
    def loca_element(self,loc,timeout=10,poll=0.5):
        return WebDriverWait(self.driver,timeout,poll).until(lambda  x:x.find_element(*loc))


    # 定位多个元素
    def loca_elements(self,loc,timeout=10,poll=0.5):
        return WebDriverWait(self.driver, timeout, poll).until(lambda x: x.find_elements(*loc))

    # 点击元素
    def click_element(self,loc):
        self.loca_element(loc).click()


    # 输入
    def input_text(self, loc, text):
        el = self.loca_element(loc)
        el.clear()
        el.send_keys(text)


    def get_screen(self):
        screen_img = "./Screen/%d.png"%int(time.time())
        self.driver.get_screenshot_as_file(screen_img)
        with open(screen_img,"rb") as f:
            allure.attach('错误截图',f.read(),allure.attach_type.PNG)




