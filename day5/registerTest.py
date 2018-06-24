# 导包
import unittest

import time
from selenium import webdriver

# 2 继承unittest.TestCase
from selenium.webdriver.common.by import By

from day5.csvFileManager4 import CsvFileManager4


class RegisterTest(unittest.TestCase):
    # 3 重写setup和teardown
    @classmethod
    def setUpClass(cls):
        cls.driver=webdriver.Chrome()
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()

    @classmethod
    def tearDownClass(cls):
        time.sleep(30)
        cls.driver.quit()

    # 4 编写一个测试用例方法，以test开头的方法

    def test_register(self):
        for row in CsvFileManager4().read('test_data.csv'):
            driver=self.driver
            driver.get("http://localhost/index.php?m=user&c=public&a=reg")
            # find_element(By.NAME,'username')等于之前的写法
            # 这两种方法没有任何区别，但是下面的这种方法扩展性更好，便于框架封装
            driver.find_element(By.NAME,'username').send_keys(row[0])
            driver.find_element(By.NAME,'password').send_keys(row[1])
            driver.find_element(By.NAME,'userpassword2').send_keys(row[2])
            driver.find_element(By.NAME,'mobile_phone').send_keys(row[3])
            driver.find_element(By.NAME,'email').send_keys(row[4])
            # driver.find_element(By.CLASS_NAME,'reg_btn').click()

            # 在for循环中执行测试用例，虽然解决了批量执行的问题，但是如果第一行数据执行失败，后续的数据
            # 先只考虑异常情况，输入完邮箱后，按tab键，检查提示信息是否都是“通过信息验证！”
            # 如何验证？如果页面提示的信息是通过信息验证！，那么测试通过，否则测试失败
            check_tip=driver.find_element(By.CSS_SELECTOR,'form.registerform.sign > ul > li:nth-child(1) > div > span').text
            print(check_tip)
            # check_tip是执行用例时，从网页上抓取得实际结果
            # 通过信息验证 是来自于手工测试用例，在测试用例执行前的期望结果
            # 如果实际结果和期望结果不相等，则认为是缺陷，相等则通过
            # if check_tip=="通过信息验证！":
            #     print("测试通过")
            # else:
            #     print("测试失败")

            #这样通过if..else语句，就可以自动判断测试用例的执行情况

            # 断言的写法
            self.assertEqual(check_tip,'通过信息验证！')
            # 虽然第一行测试数据失败了，但是后面的测试数据是不宜懒前面的数据的
            # 不应该因为第一条失败就导致其他数据不执行测试
            # 所以我们不应该用for循环的方式执行不同的测试数据，因为在一个方法中写的for循环虽然执行了多次，
            # 但是unittest任然认为这是一条记录
            # 一旦断言失败，则就会终止这条测试用例
            # 所以我们应该采用ddt框架实现数据驱动

if __name__ == '__main__':
    unittest.main()