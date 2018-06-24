# 用unittest写一个后台登录的测试用例
import unittest
# 2 建类 并且继承unittest.testCase
import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.support.select import Select


class LoginTest(unittest.TestCase):
    # 3 重写setup和teardown方法
    @classmethod
    def setUpClass(self):
        # 做web自动化测试，所有的测试用例都要打开浏览器
        self.driver=webdriver.Chrome()
        self.driver.implicitly_wait(10)
        # 窗口最大化的代码，要求驱动版本必须和浏览器精准匹配
        self.driver.maximize_window()

    # 四个空格在ptcharm中可以用tab键代替四个空格
    @classmethod
    def tearDownClass(self):
        # 为了保证看清测试结果，可以在teardown方法中加一个30秒的延时等待
        time.sleep(30)
        # 每次执行完测试用例，应该把打开的浏览器关闭，
        # 释放内存，清除cookie和缓存，为下次执行测试用例做准备
        # 这里调用的driver是声明在setup方法中的一个举报变量
        # 局部变量是不予许被其他方法访问的
        # 所以我们应该把setup方法声明的driver改成一个全局变量
        # 因为self表示类本身，所以我们在变量前加self.，就表示这个变量是属于类的
        self.driver.quit()

    def test_login(self):
        # 每次使用driver变量时，都需要前面加一个self.
        # 所以为了简化代码，可以把成员变量self.driver改写赋值给局部变量driver
        driver=self.driver
        driver.get("http://localhost/index.php?&m=admin&c=public&a=login")
        driver.find_element_by_name("username").send_keys("admin")
        # 有些常用的键可以用转义字符代替，\t表示tab键，\n表示enter键
        ActionChains(driver).send_keys("\tpassword").send_keys("\t1234").send_keys("\n").perform()

    def test_product_add(self):
        driver=self.driver
        # 如果第二个方法重新打开一个浏览器，登录就无效,怎么办？
        # 将setup和teardown改成setupclass和teardownclass
        driver.find_element_by_link_text("商品管理").click()
        driver.find_element_by_link_text("添加商品").click()
        # 除了甩name属性切换frame，也可以通过8种元素定位方法，然后切换
        iframe=driver.find_element_by_id("mainFrame")
        driver.switch_to.frame(iframe)
        # 上边两句话等于sriver.switch_to.frame("mainFrame")
        driver.find_element_by_name("name").send_keys("饮水机")
        # 变量名文件名起名规则：数字，大写字母，下划线，一般要求以字母开头不能用数字开头
        # 如果id属性是纯数字，用#号的方式不能定位，可以用中括号的方式定位
        # 所有属性都可以用【】定位
        driver.find_element_by_css_selector('[id="1"]').click()
        driver.find_element_by_id("2").click()
        driver.find_element_by_id("6").click()
        # ActionChains后面接一个方法，方法中传入要点击的元素
        ActionChains(driver).double_click(driver.find_element_by_id("7")).perform()
        select=Select(driver.find_element_by_name("brand_id"))
        select.select_by_value("1")
        driver.find_element_by_class_name("button_search").click()


if __name__ == '__main__':
    unittest.main()

