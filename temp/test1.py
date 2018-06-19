from selenium import webdriver
import time
# 创建一个浏览器对象driver
driver = webdriver.Chrome()
# 访问浏览器
driver.get("http://www.baidu.com")
#用于获取当前窗口句柄
s = driver.current_window_handle
print(type(s))
print(s)
# 窗口最大化
driver.maximize_window()
# 获取窗口的尺寸
print(driver.get_window_size())
# 设置窗口的尺寸
# driver.set_window_size(400,400)
# 隐式等待，通过一定的时长等待页面上某一元素加载完成
driver.implicitly_wait(10)
# 获取浏览器的位置
print(driver.get_window_position())
# 设置浏览器的位置
# driver.set_window_position(4,4)
# 刷新
driver.refresh()
# 获取当前访问页面的url
print(driver.current_url)
# 获取标题
print(driver.title)
# 拍照
# driver.get_screenshot_as_file("baidu.jpg")
el = driver.find_element_by_id("kw")
el.send_keys("python")
# 停留2m
time.sleep(3)
# 清楚文本
el.clear()
# 停留2m
time.sleep(3)
driver.get("http://www.sogou.com")
print(driver.current_url)
# # 停留2m
time.sleep(3)
# 退回
driver.back()
print(driver.current_url)
# # 停留2m
time.sleep(3)
# butt = driver.find_element_by_id("su")
# # 点击搜索按钮
# butt.click()
driver.quit()

# driver.close()