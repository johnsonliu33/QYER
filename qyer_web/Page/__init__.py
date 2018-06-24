from selenium.webdriver.common.by import By
# conf_day = (By.XPATH,"//*[contains(@text='29')]")

# HomePage
shangcheng = (By.XPATH,".//*[@id='app']/div/div[2]/div[1]/header/div/div[1]/ul/li[5]/a/span[1]")
#StorePage
search_city = (By.ID,"zwhomeSearchText")
search_button = (By.XPATH,".//*[@id='zwhomeSearchs']/form/div/button")
#FreeWalkerPage
free_month = (By.XPATH,".//*[@id='app']/div/div[2]/div[2]/div[1]/div[2]/div/div[2]/div[2]/div/ul/li[5]/a")
free_order = (By.XPATH,".//*[@id='app']/div/div[2]/div[2]/div[2]/div/div/div[1]/div[1]/div/div[2]/div[1]/h2/a")
#OrderPage
conf_month = (By.XPATH,".//*[@id='app']/div/div[2]/div[2]/div[1]/div[1]/div[2]/div/div[1]/div[3]")
conf_day = (By.XPATH,".//*[@id='app']/div/div[2]/div[2]/div[1]/div[1]/div[2]/div/div[3]/div[5]/div[5]/div[2]")
conf_submit = (By.XPATH,".//*[@id='lastminuteorderform']/input")
#PassengerInfoPage
info_chinese_xing = (By.XPATH,".//*[@id='tourist_firstname-0']")
info_chinese_ming = (By.XPATH,".//*[@id='tourist_lastname-0']")
info_pin_xing = (By.XPATH,".//*[@id='tourist_firstname_en-0']")
info_pin_ming = (By.XPATH,".//*[@id='tourist_lastname_en-0']")
info_sex = (By.XPATH,"html/body/div[2]/div[2]/div[4]/div/div[2]/ul/li/ul/li[5]/div/div/div/div[2]/label[1]")
info_nation = (By.XPATH,".//*[@id='tourist_nationnality-0']")
info_birthday_cal = (By.XPATH,".//*[@id='tourist_birthday-0']")
info_birthday_year = (By.XPATH,".//*[@id='ui-datepicker-div']/div/div/select[1]/option[85]")
info_birthday_month = (By.XPATH,".//*[@id='ui-datepicker-div']/div/div/select[2]/option[1]")
info_birthday_day = (By.XPATH,".//*[@id='ui-datepicker-div']/table/tbody/tr[5]/td[4]/a")
info_birthday_place = (By.XPATH,".//*[@id='tourist_birth_place-0']")
info_ID = (By.XPATH,".//*[@id='tourist_identity_type-0']")
# /li[1]/span/em 1是护照
info_ID_passport = (By.XPATH,"html/body/div[2]/div[2]/div[4]/div/div[2]/ul/li/ul/li[10]/div/div/div[2]/ul/li[1]/span/em")
info_ID_num = (By.XPATH,".//*[@id='tourist_identity_num-0']")
info_ID_due = (By.XPATH,".//*[@id='tourist_identity_validity-0']")
info_ID_due_year = (By.XPATH,".//*[@id='ui-datepicker-div']/div/div/select[1]/option[5]")
info_ID_due_month = (By.XPATH,".//*[@id='ui-datepicker-div']/div/div/select[2]/option[2]")
info_ID_due_day = (By.XPATH,".//*[@id='ui-datepicker-div']/table/tbody/tr[4]/td[2]/a")
info_ID_place = (By.XPATH,".//*[@id='tourist_identity_place-0']")
info_con_name = (By.XPATH,".//*[@id='contacts_name']")
info_con_tel = (By.XPATH,".//*[@id='input-phone-code']")
info_con_email = (By.XPATH,".//*[@id='contacts_email']")
info_con_wechat = (By.XPATH,".//*[@id='contacts_wechat']")
info_remark = (By.XPATH,".//*[@id='message_msg']")
info_submit = (By.XPATH,"html/body/div[2]/div[2]/div[7]/div/div/div[2]")
