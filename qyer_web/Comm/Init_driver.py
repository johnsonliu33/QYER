# _*_coding:utf-8_*_
def init_driver(browers):
    # 创建一个浏览器
    driver = browers()
    # 显示等待
    driver.implicitly_wait(5)
    # 窗口最大化
    driver.maximize_window()

    return driver

