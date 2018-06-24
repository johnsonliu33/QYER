# _*_coding:utf-8_*_
from qyer_web.Comm.common import Comm
import qyer_web.Page


class OrderPage(Comm):
    def __init__(self,driver):
        Comm.__init__(self,driver)

    def confirm_month(self):
        # 选择新的页面
        self.getHandles()
        # 滚动页面
        self.scroll()
        self.click_element(qyer_web.Page.conf_month)

    def confirm_day(self):
        self.click_element(qyer_web.Page.conf_day)

    def confirm_submit(self):
        self.click_element(qyer_web.Page.conf_submit)


"""
1.自由选择日期
2.自由选择产品类型

"""