# 1 打开主页
from selenium import webdriver

driver=webdriver.Chrome()

driver.get("http://localhost")
# 2 点击登录按钮
driver.find_element_by_link_text("登录").click()
# 3 在搜索框输入iphone



# 如何在新的标签页上做操作
# 窗口切换  在浏览器上切换到要切换的窗口
# driver.switch_to.window(第二个窗口的名字)
# 如何获取第二个窗口的名字
# selenium提供了所有窗口名字的集合 handles 是句柄的意思 句柄可理解为名字
# driver.window_handles 可以理解为一个数组，获取第二个窗口的名字
# [1]表示数组的第二个元素
# 所以第二个窗口的名字即为：driver.window_handles[1]
# 所以窗口切换的语句
driver.switch_to.window(driver.window_handles[1])

driver.find_element_by_name("keyword").send_keys("iphone")
# 这就是窗口切换的方法
# [1]表示第二个元素 [-1] 表示最后一个元素
# 在python中元祖和列表可以正着从0开始，可以负着从-1开始，倒数第一个-1，倒数第二个-2
# 所以上面的代码可以修改为
driver.switch_to.window(driver.window_handles[-1])