# 这种框架的设计思想叫做pageobject设计模式，是一种高级的框架设计思想
# 这种思想主旨是把业务逻辑和代码技术分离开
# 测试用例的类 专门负责业务逻辑
# 元素定位和操作交给pageobject类
# 在pageobject这个类中，把每个网页看成一个类，其中网页中的每个元素看成类中的一个属性
# 针对这个元素的操作，看成类中的一个方法
# 元素的信息，定位是名词性，所以要看成属性（成员变量）
# 元素的操作是动词性，所以被看成是方法
# 下面我们封装一下登录这个网页
# 这个类主要做的就是把元素定位改一个易于理解的名字
from selenium import webdriver
from selenium.webdriver.common.by import By


class LoginPage:
    # 为这个网页创建一个构造函数
    # 在python中构造函数固定名字 __init__（）
    def __init__(self,driver):
        # 因为setUp方法中已经创建了一个浏览器，所以这里不需要再次创建，直接使用setup创建好的即可
        #self.driver=webdriver.Chrome()
        self.driver=driver
        self.url="http://localhost/index.php?m=user&c=public&a=login"

     # 声明一个变量保存元素的定位方式
     # 加上括号叫做python的元组，类似于数组
    # 这句话的意思是申明了一个数组，叫username_input_loc
    # 数组中有两个元素：分别是By.NAME,'username'
    username_input_loc=(By.NAME,'username')
    password_loc=(By.NAME,'password')
    login_loc=(By.CLASS_NAME,'login_btn')

    def open(self):
        self.driver.get(self.url)
    # 给参数（usernme）设置默认值，如果调用方法时，传入一个新的用户名，那么使用新的，
    # 如果调用方法时，不传参，那么使用默认值
    def input_username(self,username='blx'):
        # 这个类中涉及到三个元素定位，元素定位不太稳定，经常需要修改
        # 所以应该把定位方式单独声明成了类中的一个属性
        # *表示给find_element（）这个方法传入的不是一个元组，而是元组中的每个元素分别传入
        self.driver.find_element(*self.username_input_loc).send_keys(username)

    def input_password(self,password='blx123'):
        self.driver.find_element(*self.password_loc).send_keys(password)

    def click_login_button(self):
        self.driver.find_element(*self.login_loc).click()