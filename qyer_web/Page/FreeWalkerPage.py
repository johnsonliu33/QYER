# _*_coding:utf-8_*_
from qyer_web.Comm.common import Comm
import qyer_web.Page


class FreeWalkerPage(Comm):
    def __init__(self,driver):
        # 子类重写了父类同名方法 然后调用父类同名方法
        Comm.__init__(self,driver)

    def choice_month(self):
        self.click_element(qyer_web.Page.free_month)

    def choice_order(self):
        self.click_element(qyer_web.Page.free_order)


"""
1.自由选择旅行时间、类型
2.选最便宜的订单，或者指定第几个订单
"""

