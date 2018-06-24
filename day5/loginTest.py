import unittest

import time
from selenium.webdriver.common.by import By

from day5.mytestCase import MyTestCase


class LoginTest(MyTestCase):
    # 这时 这个类不需要写setup和teardown方法
    # 直接写测试用例方法即可
    def test_login(self):
        driver=self.driver
        driver.get("http://localhost/index.php?m=user&c=public&a=login")
        driver.find_element(By.NAME,'username').send_keys('blx')
        driver.find_element(By.NAME,'password').send_keys('blx123')
        old_title=driver.title
        driver.find_element(By.CLASS_NAME,'login_btn').click()
        # 写一个断言自动判断登录是否成功
        time.sleep(5)
        new_title=driver.title
        # 这时如果新标题和旧标题不相等，就说明页面发生了跳转，如果相等就说明没有登录成功
        print("旧页面："+old_title)
        print("新页面："+new_title)
        self.assertNotEqual(old_title,new_title)



if __name__ == '__main__':
    unittest.main()