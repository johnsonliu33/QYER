from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait


class Comm(object):
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(5)
        self.driver.maximize_window()


    def locateElement(self,locate_type,value):
        el = None
        if locate_type == "id":
            el = self.driver.find_element_by_id(value)
        elif locate_type == 'name':
            el = self.driver.find_element_by_name(value)
        elif locate_type == 'class':
            el = self.driver.find_element_by_class_name(value)
        elif locate_type == 'text':
            el = self.driver.find_element_by_link_text(value)
        elif locate_type == 'xpath':
            el = self.driver.find_element_by_xpath(value)
        elif locate_type == 'css':
            el = self.driver.find_element_by_css_selector(value)
        elif locate_type == 'tag':
            el = self.driver.find_element_by_tag_name(value)

        # 如果el不为None,则返回
        if el is not None:
            return el

    # 单个元素定位
    def loca_element(self, loc, timeout=10, poll=0.5):
        return WebDriverWait(self.driver, timeout, poll).until(lambda x: x.find_element(*loc))

    # 定位多个元素
    def loca_elements(self, loc, timeout=10, poll=0.5):
        return WebDriverWait(self.driver, timeout, poll).until(lambda x: x.find_elements(*loc))

    # 点击元素
    def click_element(self, loc):
        self.loca_element(loc).click()

    # 输入
    def input_text(self, loc, text):
        self.loca_element(loc).send_keys(text)

    # 打开url
    def open_url(self,url):
        self.driver.get(url)

    # 打印title
    def print_title(self):
        print(self.driver.title)

    # 获取句柄，返回第二个
    def getHandles(self):
        handles = self.driver.window_handles
        # print("打印handles：", handles)
        # handles索引从0开始
        self.driver.switch_to.window(handles[1])

    # 获得frame
    def get_frame(self):
        element = self.driver.find_element_by_tag_name("iframe")

    # 滚动窗口
    def scrollbar(self,x,y):
        js = "window.scrollTo(%d,%d)"%(x,y)
        # js = "var q=document.documentElement.scrollTop=%d"%num
        # 执行js
        self.driver.execute_script(js)

    # 获取所有的产品，返回第一个
    def all_product(self,cla):
        p_list = self.driver.find_elements_by_class_name(cla)
        # p_text = []
        # for i in p_list:
        #     p_text.append(i.text)
        return p_list[1]



    # 写了这个函数，自动关闭，不用调取
    def __del__(self):
        self.driver.quit()













# if __name__ == '__main__':
    # tool = MyTools()
    # tool.open_url("http://www.qyer.com/")
    # tool.printTitle()
    #
    # tool.locateElement("text", "商城")
    # tool.myClick("text", "商城")
    #
    # tool.printTitle()
    #
    # tool.close()
