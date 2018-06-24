# 1.登录海盗商城
# 因为大部分测试用例都会用到登录功能，那么我们可以以把登录功能单独封装成一个方法，每次直接调用这个方法
# 这样以后每次登录就只需要一行方法调用代码即可
# from selenium import webdriver
# from selenium.webdriver import ActionChains
# from selenium.webdriver.common.keys import Keys
#
# driver=webdriver.Chrome()
# driver.get("http://localhost/index.php?m=user&c=public&a=login")
# driver.find_element_by_id("username").send_keys("blx")
# actions = ActionChains(driver)
# actions.send_keys(Keys.TAB).send_keys("blx123").perform()
# actions.send_keys(Keys.ENTER).perform()
import time
from selenium import webdriver

# 文件名、类名、包名都应该以字母开头，可以有数字和下划线
# 不能有空格和中文
from day2.login_test import Login

# 已经创建好一个空白浏览器，后续的所有操作都应该在此浏览器上执行
driver = webdriver.Chrome()
# 每次创建浏览器时，implicitly_wait固定写一次，对在这个浏览器上执行的所有代码都生效
# implicitly_wait主要监测页面的加载时间，检测什么时候页面加载完，什么时候执行后续操作
driver.implicitly_wait(20)
# 实例化对象会占用内存，pycharm会自动帮我们释放内存
# 代码运行完检测到Login（）这个对象，不在被使用，系统会自动释放内存
# 调用登录方法
# 把driver浏览器传入到登录方法中，让登录方法和下面的点击账号设置使用同一个浏览器
Login().LoginWithDefaultUser(driver)
# 2.点击“账号设置”
# 现在文件中没有driver变量，如何处理

driver.find_element_by_link_text("账号设置").click()


# 3.点击“个人资料”
# xpath发放比较通用，可以用工具自动化生成，但是不推荐使用
# 作为一种没有办法时使用的办法
# 因为xpath的可读性和可维护性比较差
driver.find_element_by_xpath("/html/body/div[3]/div/div[1]/div[4]/ul/li[2]/a").click()
# partial_link_text文本可以使用链接的一部分进行元素定位
# 当链接文本过长时，推荐使用partial_link_text
# 使用partial_link_text方法时，可以用链接中的任意一部分，只要这部分文字在网页中唯一即可
#driver.find_element_by_partial_link_text("个人资料").click()


# 4.修改真实姓名
# 如果输入框中原本有内容，那么修改内容时需要先清空原来的值，用clear()方法
# 良好的变成习惯，在每次send之前都应该做clear操作
driver.find_element_by_id("true_name").clear()
driver.find_element_by_id("true_name").send_keys("边边")

# 5.修改性别
# 性别唯一的区别就是value属性的值
# 是否可以通过value属性来定位？
# 要想通过value属性定位有两种方法：xpath和css_slecetor
# 通过css_slecetor定位元素，需要在唯一属性的两边加一对中括号即可
driver.find_element_by_css_selector('[value="2"]').click()
# 在xpath中//表示采用相对路径定位元素，相对路径一般通过元素的特殊属性查找元素
# /表示绝对路径，一般都是从/HTML根节点开始定位元素，绝对路径一般通过元素的位置，层级关系查找元素
# 绝对路径写起来比较长，涉及到的节点比较多，代码稳定性比较差，页面布局发生变化时，收到影响的可能性比较大
# 相对路径查询速度比较慢，可能需要遍历更多的节点
# 工作中一般用css_slecetor
# css_slecetor查询速度比xpath快一点；所有前端开发都会用
# xpath在某些浏览器上支持的不太好
# *表示任意节点
# [@]表示通过属性定位
#driver.find_element_by_xpath('//*[@value="2"]').click()
# javascript的getElementsByClassName()方法可以找到页面上符合条件的所有元素，通过下表选取其中的第那个元素，也可以定位
# selenium可不可以用这种思路来定位元素？
# 要找页面上符合条件的唯一元素，就用此方法
#driver.find_elements_by_id("xb")[2].click()

# 6.修改生日
#一下一下选择是可以的 但是稳定性比较差，并且很难修改日期
#右键检查可以发现，日历控件其实是一个输入框
# 因为readonly属性，写一个javascri脚本删除这个属性
driver.execute_script('document.getElementById("date").removeAttribute("readonly")')
driver.find_element_by_id("date").clear()
driver.find_element_by_id("date").send_keys("2018-06-03")


# 7.修改qq
driver.find_element_by_id("qq").clear()
driver.find_element_by_name("qq").send_keys("123456781")

# 8.点击确定，保存成功
driver.find_element_by_class_name("btn4").click()
time.sleep(3)
driver.switch_to_alert().accept()