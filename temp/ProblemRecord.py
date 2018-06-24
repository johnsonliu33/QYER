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


driver = webdriver.Chrome()
driver.maximize_window()
driver.get("http://z.qyer.com/deal/107249/?direct=568152")

# #js的脚本语言，距离顶端1000px
js="window.scrollTo(0,500)"
# 运行js
driver.execute_script(js)

# 选择日期,提交订单
driver.find_element_by_xpath(".//*[@id='app']/div/div[2]/div[2]/div[1]/div[2]/div[2]/div[2]/div/div/input").click()
for i in range(2):
    driver.find_element_by_xpath("html/body/div[3]/div[1]/div/div[1]/button[4]").click()
    time.sleep(2)

driver.find_element_by_xpath("html/body/div[3]/div[1]/div/div[2]/table[1]/tbody/tr[5]/td[5]/div/span").click()



# 定位护照等失败
# driver.find_element_by_css_selector("#tourist_identity_type-0").click()


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



# driver.quit()