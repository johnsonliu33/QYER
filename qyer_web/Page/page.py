from qyer_web.Page.OpenPage import OpenPage


class Page_Obj:
    def __init__(self,driver):
        self.driver = driver

    def open(self):
        return OpenPage(self.driver)

    # def login(self):
    #     print("这是一个登陆页面")
    #
    # def logout(self):
    #     print("这是一个退出页面！")
    #
    # def home(self):
    #     print("这是网站主页面！")