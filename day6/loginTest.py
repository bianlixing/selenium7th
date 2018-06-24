from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC # 将expected_conditions重命名为EC
from selenium.webdriver.support.wait import WebDriverWait

driver=webdriver.Chrome()

driver.get("http://localhost/index.php?m=user&c=public&a=login")
driver.find_element_by_id("username").send_keys("blx")
driver.find_element_by_name("password").send_keys("blx123")
driver.find_element_by_class_name("login_btn").click()
# 因为中间存在一个登录成功页面，所以不能直接点击该链接
#解决办法：三种方式：time.sleep(),隐式等待，显示等待
# 显示等待
WebDriverWait(driver,20,0.5).until(EC.invisibility_of_element_located(By.LINK_TEXT,'进入商城购物'))
# 这句显示等待相当于time.sleep(20)的优化版，作用是相同的
driver.find_element_by_link_text("进入商城购物").click()