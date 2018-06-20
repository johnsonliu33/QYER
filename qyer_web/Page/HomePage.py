# 导入定位元素
import qyer_web.Page
# 继承Comm
from qyer_web.Comm.common import Comm


class HomePage(Comm):
    def __init__(self, driver):
        Comm.__init__(self, driver)
        # 子类重写了父类同名方法 然后调用父类同名方法


    # 打开url
    def open_url(self,url):
        self.driver.get(url)


    # 点击商城
    def click_shopping(self):
        self.click_element(qyer_web.Page.shangcheng)


