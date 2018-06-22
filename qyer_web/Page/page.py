from qyer_web.Page.FreeWalkerPage import FreeWalkerPage
from qyer_web.Page.HomePage import HomePage
from qyer_web.Page.OrderPage import OrderPage
from qyer_web.Page.StorePage import StorePage


class Page_Obj:
    def __init__(self,driver):
        self.driver = driver

    def open(self):
        return HomePage(self.driver)

    def store(self):
        return StorePage(self.driver)

    def free_walker(self):
        return FreeWalkerPage(self.driver)


    def order(self):
        return OrderPage(self.driver)
