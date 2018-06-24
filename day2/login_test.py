# 如何把这个文件封装成一个登录方法
# python中类的关键字和Java一样 是class
# python中也有一个个关键字是def（define的缩写）表示定义方法


# 1.打开浏览器
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys

# 首先声明一个类
# python中使用：号代替java中的{}大括号
# 所有属于类中的语句都必须空四个空格
class Login():
    # 声明一个方法
    # def是方法的关键字 表示这是一个方法
    # LoginWithDefaultUser是我们自己随意起的方法名，意思是使用默认账户进行登录
    # 方法后面必须要有括号，可以用来声明参数
    # 括号中默认有一个参数self，self表示类本身，类似于java中的this关键字
    # self参数后面会详细讲述
    # 方法后面也有一个冒号：方法下面的语句还要在锁紧四个空格
    # 以后只需要写一句话调用这个方法
    def LoginWithDefaultUser(self,driver):
        #driver=webdriver.Chrome()lo
        # 2.打开海盗商城网站
        driver.get("http://localhost/index.php?m=user&c=public&a=login")
        # 3.删除登录链接的target属性
        # 执行javascript脚本
        # 在python中字符串可以用单引号，也可以用双引号，如果字符串本身包含双引号，则使用单引号
        driver.execute_script('document.getElementsByClassName("site-nav-right fr")[0].childNodes[1].removeAttribute("target")')
        # document.getElementsByClassName("site-nav-right fr")[0].childNodes[1].removeAttribute("tarfet")
        # 4.点击登录按钮，跳转到登录页面
        driver.find_element_by_link_text("登录").click()

        # 输入用户名
        driver.find_element_by_id("username").send_keys("blx")
        # 输入密码（模拟tab键）
        #ActionChains（类）需要导包
        # action动作行为的意思，chains是链表的意思链表类似于数组
        # 所以ActionChains可以列为一组动作和行为的意思
        # 下边这句表示实例化一个ActionChains这个类的对象，这个对象可以用来执行一组动作行为
        # 和java区别就是去掉了new关键字
        #python语言中实例化对象不需要声明变量的类型
        actions = ActionChains(driver)
        # keys表示键盘上的所有按键
        # 如果使用键盘上任意控件，直接到keys这个类中找
        # 所有action中的方法都必须一perform()结尾才会被执行
        actions.send_keys(Keys.TAB).send_keys("blx123").perform()
        # 7.点击登录按钮
        #ActionChains(driver).send_keys(Keys.ENTER).perform()
        # 假如不支持回车键登录，我们可以直接定位登录按钮
        # 假如有人很难定位登录按钮，我们还可以用submit（）方法
        # submit是提交的意思，用于提交表单
        # 开发通过form表单把信息同时提交到服务器
        # 可以用任何一个元素执行submit（）方法，提交表单中的数据
        # 比如，可以使用户名来提交表单数据
        driver.find_element_by_id("username").submit()