from qyer_web.Page.HomePage import HomePage
from qyer_web.Page.StorePage import StorePage


class Page_Obj:
    def __init__(self,driver):
        self.driver = driver

    def open(self):
        return HomePage(self.driver)

    def store(self):
        return StorePage(self.driver)

        # def login(self):
        #     print("这是一个登陆页面")
        #
        # def logout(self):
        #     print("这是一个退出页面！")
        #