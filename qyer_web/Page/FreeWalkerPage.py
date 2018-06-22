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
1.应该可以选择任意一个月
2.最便宜的订单，或者第一个订单
"""

