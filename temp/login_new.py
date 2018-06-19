from selenium import webdriver
import time


driver = webdriver.Firefox()
driver.get("http://www.QYER.com/")
print("打印开始页面的title：",driver.title)

# 第一部分：菜单栏定位
# 目的地
# destination = driver.find_element_by_partial_link_text("目的")
# xpath：索引号进行定位-----------------------
# destination = driver.find_element_by_xpath("//li[1]")
# xpath：模糊属性值-----------------------
# destination = driver.find_element_by_xpath("//a[starts-with(@class,'nav')]")
# destination.click()

# 锦囊
# sikl_bag = driver.find_element_by_class_name("nav-span")
# sikl_bag.click()

# 社区
# community = driver.find_element_by_css_selector("li.nav-list:nth-child(3)")
# community.click()

# 商城
# stores = driver.find_element_by_link_text("商城")
# stores.click()

# 机票    文本元素是某元素来匹配,格式：//*[text()="xx"] -----------------------*可以换成标签
# ticket = driver.find_element_by_xpath("//*[text()='机票']")
# ticket.click()

# 酒店民宿   属性中含有某元素来匹配,格式： //*[contains(@属性名,'xxx')] -----------------------
# hotel =driver.find_element_by_xpath("//*[contains(@data-bn-ipg,'index-head-hotel')]")
# hotel.click()

# 独家深度  同时满足两个属性值的元素的匹配，格式：//*[@属性名1=value1 and @属性名2=value2]-----------------------
# Exclusive_deph = driver.find_element_by_xpath("//*[@title='独家深度' and @class='nav-span']")
# Exclusive_deph.click()

# 穷游App  页面元素属性-----------------------
# app = driver.find_element_by_xpath("//a[@href='//app.QYER.com/guide/']")
# app.click()



# 第二部分：中间输入框的定位
# 目的地输入框
mdd = driver.find_element_by_xpath("//input[@class='txt focus placesearch_txt']")
driver.implicitly_wait(10)
mdd.send_keys("日本")
time.sleep(10)
# 拍照
# driver.get_screenshot_as_file("日本.png")


# 做行程

# 买折扣输入框

# 搜索
search = driver.find_element_by_xpath("//button[@class='btn']")
search.click()


# 第三部分：打开的页面句柄的输出
handles = driver.window_handles
print("打印handles：",handles)
# handles索引从0开始
driver.switch_to.window(handles[0])
print("打印选中页面的title：",driver.title)



driver.quit()


