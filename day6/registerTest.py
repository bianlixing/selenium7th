import unittest

import time
from selenium import webdriver
from selenium.webdriver.common.by import By

from day5.mytestCase import MyTestCase
from day6.DBconnection import DBConnection


class RegisterTest(MyTestCase):
    def test_regiter(self):
        driver=self.driver
        # 数据库验证测试的正常情况
        self.driver.get('http://localhost/index.php?m=user&c=public&a=reg')
        driver.find_element(By.NAME, 'username').send_keys('blxb')
        driver.find_element(By.NAME, 'password').send_keys('123456')
        driver.find_element(By.NAME, 'userpassword2').send_keys('123456')
        driver.find_element(By.NAME, 'mobile_phone').send_keys('13245678911')
        driver.find_element(By.NAME, 'email').send_keys('456@123.com')
        driver.find_element(By.CLASS_NAME,'reg_btn').click()
        time.sleep(2)
        sql='select*from hd_user order by id desc;'
        new_result=DBConnection().execute_sql_command(sql)
        self.assertEqual('blxb',new_result[1])
        self.assertEqual('456@123.com',new_result[2])
        print(new_result)