# _*_coding:utf-8_*_
from qyer_web.Comm.common import Comm
import qyer_web.Page


class PassengerInfoPage(Comm):
    def __init__(self,driver):
        Comm.__init__(self,driver)


    def information(self,chinese_xing,chinese_ming,
                    ping_xing,pin_ming,nation,birthday_place,
                    ID_num,ID_place,con_name,con_tel,con_email,con_wechat,remark):
        """
        self,chinese_xing,chinese_ming,
                    ping_xing,pin_ming,nation,birthday,birthday_place,
                    ID,ID_num,ID_due_day,ID_place,con_name,con_tel,con_email,con_wechat,remark
        """
        self.input_text(qyer_web.Page.info_chinese_xing,chinese_xing)
        self.input_text(qyer_web.Page.info_chinese_ming,chinese_ming)
        self.input_text(qyer_web.Page.info_pin_xing,ping_xing)
        self.input_text(qyer_web.Page.info_pin_ming,pin_ming)
        self.click_element(qyer_web.Page.info_sex)
        self.input_text(qyer_web.Page.info_nation,nation)
        # 选择日历
        self.click_element(qyer_web.Page.info_birthday_cal)
        # 选择年
        self.click_element(qyer_web.Page.info_birthday_year)
        # 选择月
        self.click_element(qyer_web.Page.info_birthday_month)
        # 选择日
        self.click_element(qyer_web.Page.info_birthday_day)
        self.input_text(qyer_web.Page.info_birthday_place,birthday_place)
        self.click_element(qyer_web.Page.info_ID)
        self.click_element(qyer_web.Page.info_ID_passport)

        self.input_text(qyer_web.Page.info_ID_num,ID_num)
        self.click_element(qyer_web.Page.info_ID_due)
        # 选择年
        self.click_element(qyer_web.Page.info_ID_due_year)
        # 选择月
        self.click_element(qyer_web.Page.info_ID_due_month)
        # 选择日
        self.click_element(qyer_web.Page.info_ID_due_day)
        self.input_text(qyer_web.Page.info_ID_place,ID_place)
        self.input_text(qyer_web.Page.info_con_name,con_name)
        self.input_text(qyer_web.Page.info_con_tel,con_tel)
        self.input_text(qyer_web.Page.info_con_email,con_email)
        self.input_text(qyer_web.Page.info_con_wechat,con_wechat)
        self.input_text(qyer_web.Page.info_remark,remark)
        self.click_element(qyer_web.Page.info_submit)



"""
1.日期
2.证件

"""