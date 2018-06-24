import pytest
import allure
from qyer_web.Page.page import Page_Obj
from qyer_web.Comm.Init_driver import init_driver
from selenium import webdriver


#读取数据
def re_data_list():
    data_list = []
    with open("F:/PythonTest/test/QYER/qyer_web/Data/data.txt","r",encoding='utf-8') as f:
        for i in f.readlines():
            # 截取等号右侧的数据
            data_list.append(eval(i.split("=")[-1]))
        print("data is:",data_list)
    return data_list


class Test_Process:
    def setup_class(self):
        # 创建driver对象和每个页面的对象
        self.driver = init_driver(webdriver.Chrome)
        self.open = Page_Obj(self.driver).open()
        self.store = Page_Obj(self.driver).store()
        self.freeWalker = Page_Obj(self.driver).free_walker()
        self.order = Page_Obj(self.driver).order()
        self.info = Page_Obj(self.driver).passager_info()

        print("start................")


    def teardown_class(self):
        # 写了这个函数，自动关闭，不用调取
        self.driver.quit()
        print("end..................")

    # 格式 @pytest.mark.parametrize("a,b", [(3, 6),(1,8),(2,9)])
    @pytest.mark.parametrize("url,expect,expect1",re_data_list())
    @allure.step(title='HomePage')
    def test_001(self,url,expect,expect1):
        self.open.open_url(url)
        assert expect == self.open.driver.title
        self.open.click_shopping()
        assert  expect1 == self.open.driver.title
        allure.attach('描述', '打开主页，点击商城')


    @allure.step(title='StorePage')
    def test_002(self):
        self.store.search_city("大阪")
        print(self.store.driver.title)
        print(self.store.driver.current_url)
        allure.attach('描述', '输入城市进行搜索')

    @allure.step(title='FreeWalkerPage')
    def test_003(self):
        self.freeWalker.choice_month()
        self.freeWalker.choice_order()
        print(self.freeWalker.driver.title)
        print(self.freeWalker.driver.current_url)
        allure.attach('描述', '选择订单')

    @allure.step(title='OrderPage')
    def test_004(self):
        self.order.confirm_month()
        self.order.confirm_day()
        self.order.confirm_submit()
        print(self.order.driver.title)
        print(self.order.driver.current_url)
        allure.attach('描述', '提交订单')

    @allure.step(title='PassengerInfoPage')
    def test_005(self):
        self.info.information("黄","志伟","huang","zhiwei","中国","北京","G59424083","北京","姚假拉","15001241111","15001241111@163.com","yyyy","备注是我们预定8张")
        print(self.info.driver.title)
        print(self.info.driver.current_url)
        allure.attach('描述', '提交个人预定信息')





        # @pytest.allure.severity(pytest.allure.severity_level.CRITICAL)
        # @allure.step(title='第1个测试')
        # def test_001(self):
        #     # 错误时才会提交截图
        #     assert 0,self.tt.get_screen()


# 阿尔法测试是内部测试，贝特测试用户测试，公测

if __name__ == '__main__':
    # git 用push成功了，add，conmmit不可以

     # pytest.main("-s  po_Run.py")
    # 生成xml文件的报告,其实同ini文件里的命令，但是有时候怎么不能生成呢？
    # 生成后再在命令行里输入下面的转换命令
    pytest.main("-s --alluredir report po_Run.py")

"""
配置文件pytest.ini里面不能有中文
"""

# xml报告转成html格式命令：allure generate report/ -o report/html
