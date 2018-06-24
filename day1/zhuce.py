# 在这个python文件中，实现注册功能自动化
from selenium import webdriver
driver=webdriver.Chrome()
# 打开首页
driver.get("http://localhost/")
# 打开注册页面
driver.get("http://localhost/index.php?m=user&c=public&a=reg")

# 注册信息
driver.find_element_by_name("username").send_keys("blx1")
driver.find_element_by_name("password").send_keys("123456")
driver.find_element_by_name("userpassword2").send_keys("123456")
driver.find_element_by_name("mobile_phone").send_keys("13222222222")
driver.find_element_by_name("email").send_keys("1234@qq.com")

# 点击注册
driver.find_element_by_class_name("reg_btn").click()

