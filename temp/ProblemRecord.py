"""
1.注册信息里的：证件类型、日期---
2.如何获取页面里的表单
3.循环遍历页面的所有产品
4.循环获取证件类型
5.assertEqual的使用
6.鼠标的悬停和双击
7.数据代码分离
8.添加用例
9.把页分类
10.如何用一个方法，定位到产品名字，不知绝对路径
11.选择产品变动时，如何定位到，列表选择第一个？
nwe：性别、证件类型
"""

#遍历iframe
# List<WebElement> element=driver.findElements(By.xpath("//iframe"));
# System.out.println("iframe个数"+element.size());
# for(int i=0;i<element.size();i++){
#     String name=element.get(i).getAttribute("src");
#     System.out.println(name);
# }
from selenium import webdriver
from selenium.webdriver import ActionChains
import time
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.select import Select
from qyer.Comm.tools import MyTools

driver = webdriver.Firefox()
# driver.get("http://z.qyer.com/all_1_1000003_14_8616_158,146_0_0/?keyword=%E6%97%A5%E6%9C%AC")
# p_list = driver.find_elements_by_class_name("zw-module-bigcard-h2ul-wrap")
# p_text = []
# for i in p_list:
#     p_text.append(i.text)
#
# p_list[1].click()
driver.get("http://z.QYER.com/deal/111075/?direct=477958")


# 选择日期,提交订单
driver.find_element_by_xpath(".//*[@id='app']/div/div[2]/div/div[1]/div[1]/div[2]/div/div[1]/div[2]").click()
driver.find_element_by_xpath(".//*[@id='app']/div/div[2]/div/div[1]/div[1]/div[2]/div/div[3]/div[4]/div[5]/div[1]").click()
driver.find_element_by_xpath(".//*[@id='lastminuteorderform']/input").click()



#js的脚本语言，距离顶端1000px
js="window.scrollTo(0,500)"
# 运行js
driver.execute_script(js)



# 定位护照等失败
driver.find_element_by_css_selector("#tourist_identity_type-0").click()


# el_list = driver.find_elements_by_css_selector(".qui-inputAutocomplete-ul>li")

# print(el_list)
# for i in el_list:
#     print(i.get_attribute("title"))
#
# for i in range(1,8):
el_list = driver.find_elements_by_id("tourist_identity_type-0")

for el in el_list:
    ActionChains(driver).move_to_element(el).perform()
    time.sleep(1)

# driver.find_element_by_xpath("html/body/div[2]/div[2]/div[5]/div/div[2]/ul/li/ul/li[10]/div/div/div[2]/ul/li[1]").click()
#
driver.find_element_by_xpath( ".//*[@id='tourist_identity_num-0']").send_keys("110222198401262222")
# driver.quit()