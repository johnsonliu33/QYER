import time

from qyer_web.Comm.common import Comm
import qyer_web.Page


class OrderPage(Comm):
    def __init__(self,driver):
        Comm.__init__(self,driver)

    def confirm_month(self):
        self.click_element(qyer_web.Page.conf_month)

    def confirm_day(self):
        self.click_element(qyer_web.Page.conf_day)

    def confirm_submit(self):
        self.click_element(qyer_web.Page.conf_submit)

