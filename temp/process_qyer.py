from temp.util import Commm
from selenium.webdriver.support.select import Select


class Process(Commm):
    def process(self):
        # 打开网页
        self.open_url("http://www.QYER.com/")
        self.print_title()
        # 点击商城
        self.locateElement("text","商城").click()
        self.print_title()
        # 输入要去的国家
        self.locateElement("id","zwhomeSearchText").send_keys("日本")
        self.locateElement("xpath",".//*[@id='zwhomeSearchs']/form/div/button").click()
        self.print_title()
        # 选择目的地属性
        # 一般是title标签的
        self.locateElement("text","自由行").click()
        self.locateElement("text","北京/天津").click()
        self.locateElement("text","札幌").click()
        self.locateElement("text","三月").click()
        # # 选择一个产品
        # self.locateElement("xpath","html/body/div[6]/div[1]/div[1]/div/div[2]/div[1]/h2/a").click()
        # # self.locateElement("text","北京直飞札幌8天7晚自由行（登别洞爷湖+滑雪破冰船+温泉酒店+签证/保险/WiFi/精美路书/7*24小时行中保障）")
        # # 选择新打开的页面
        # self.getHandles()
        # self.print_title()
        #
        # # 选择日期,提交订单
        # # 点击22日
        # self.locateElement("xpath",".//*[@id='app']/div/div[2]/div/div[1]/div[1]/div[2]/div/div[3]/div[4]/div[5]/div[1]").click()
        # # 点击立即预订
        # self.locateElement("xpath",".//*[@id='lastminuteorderform']/input").click()
        # self.print_title()
        #
        # # 填写旅客信息
        # self.locateElement("xpath",".//*[@id='tourist_firstname-0']").send_keys("黄")
        # self.locateElement("xpath", ".//*[@id='tourist_lastname-0']").send_keys("志伟")
        # self.locateElement("xpath", ".//*[@id='tourist_firstname_en-0']").send_keys("HUANG")
        # self.locateElement("xpath", ".//*[@id='tourist_lastname_en-0']").send_keys("ZHIWEI")
        # self.locateElement("xpath", "html/body/div[2]/div[2]/div[4]/div/div[2]/ul/li/ul/li[5]/div/div/div/div[2]/label[1]").click()
        # self.locateElement("xpath", ".//*[@id='tourist_nationnality-0']").send_keys("中国")
        # # 时间
        # self.locateElement("xpath", ".//*[@id='tourist_birthday-0']").click()
        # el1 = self.locateElement("xpath",".//*[@id='ui-datepicker-div']/div/div/select[1]")
        # sel_obj = Select(el1)
        # sel_obj.select_by_visible_text("1988")
        # el2 = self.locateElement("xpath",".//*[@id='ui-datepicker-div']/div/div/select[2]")
        # sel_obj = Select(el2)
        # sel_obj.select_by_visible_text("8月")
        # self.locateElement("xpath",".//*[@id='ui-datepicker-div']/table/tbody/tr[4]/td[6]/a").click()
        #
        # self.locateElement("xpath", ".//*[@id='tourist_birth_place-0']").send_keys("北京")
        #
        # # 证件类型
        # self.locateElement("css","#tourist_identity_type-0").click()
        # self.locateElement("xpath","html/body/div[2]/div[2]/div[4]/div/div[2]/ul/li/ul/li[10]/div/div/div[2]/ul/li[2]").click()
        #
        # self.locateElement("xpath", ".//*[@id='tourist_identity_num-0']").send_keys("110222198401262222")
        # # 时间
        # self.locateElement("xpath", ".//*[@id='tourist_identity_validity-0']").click()
        # el3 = self.locateElement("xpath",".//*[@id='ui-datepicker-div']/div/div/select[1]")
        # sel_obj = Select(el3)
        # sel_obj.select_by_visible_text("2022")
        # el4 = self.locateElement("xpath", ".//*[@id='ui-datepicker-div']/div/div/select[2]")
        # sel_obj = Select(el4)
        # sel_obj.select_by_visible_text("2月")
        # self.locateElement("xpath",".//*[@id='ui-datepicker-div']/table/tbody/tr[4]/td[2]/a").click()
        # self.locateElement("xpath", ".//*[@id='tourist_identity_place-0']").send_keys("北京")
        # self.locateElement("xpath", ".//*[@id='contacts_name']").send_keys("黄春景")
        # self.locateElement("xpath", ".//*[@id='input-phone-code']").send_keys("13391562333")
        # self.locateElement("xpath", ".//*[@id='contacts_email']").send_keys("123123@qq.com")
        # # 点击同意
        # self.locateElement("xpath", "html/body/div[2]/div[2]/div[8]/div/div/div[2]").click()
        #
        # el5 = self.locateElement("css",".fast-content-title")
        # print(el5.text)


if __name__ == '__main__':
    # 创建对象
    p = Process()
    # 调用方法
    p.process()
# self.driver.get_screenshot_as_file("p.png")