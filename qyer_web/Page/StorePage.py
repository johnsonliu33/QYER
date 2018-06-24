# _*_coding:utf-8_*_
from qyer_web.Comm.common import Comm
import qyer_web.Page


class StorePage(Comm):
    def __init__(self,driver):
        # 子类重写了父类同名方法 然后调用父类同名方法
        Comm.__init__(self,driver)

    # 输入城市，点击搜索
    def search_city(self,city):
        self.input_text(qyer_web.Page.search_city,city)
        self.click_element(qyer_web.Page.search_button)



