# 这个文件用来实现一个登录功能
# 1.打开浏览器
# 从selenium项目中调用网络驱动
import time
from selenium import webdriver


# 给浏览器命名为driver（固定使用dirver）
driver=webdriver.Ie()
# 设置智能等待:一旦找到页面元素，马上执行后面的语句
# 如果超过20面仍然找不到页面元素，那么程序将会报超时错误
driver.implicitly_wait(20)
# 2.打开海盗商城主页
driver.get("http://localhost/")
# 3.打开登陆页面
driver.get("http://localhost/index.php?m=user&c=public&a=login")
# 4.输入用户名和密码
driver.find_element_by_id("username").send_keys("blx")
driver.find_element_by_name("password").send_keys("blx123")

# 5. 点击登录按钮
#所有在调用方法，都会有提示信息，没有提示信息说明没有此方法
driver.find_element_by_class_name("login_btn").click()
# 6. 检查是否登陆成功
# 找到xpath元素，.text表示获取这个元素的文本信息
#alt+enter 导包快捷键，选import this time 选最短的time
# tiem.sleep这个方法提供了一种固定的时间等待
# 意义是点击登录按钮后 等5秒后 在检查用户名是否正常显示
# 弊端：因为网络延迟，不确定每次等待的时间为多少秒合适
# 解决办法：用智能等待代替固定等待
#time.sleep(5)
username_text=driver.find_element_by_xpath("/html/body/div[2]/div[1]/div[1]/div[2]/a[1]").text

print(username_text)
# 可以通过if语句判断页面显示的文本和预期的文本是否一致，来判断测试用例执行是否成功
if username_text=='您好 blx':
     print("测试执行通过")
else:
     print("测试失败")
# 因为selenium主要做回归测试，所以测试脚本都是pass的，只有开发做了代码变更，我们的测试用例才有可能失败。
# 一般工作中不用if else语句做判断，后面讲详细讨论这个问题

# 7.点击“进入商城购物按钮”
#driver.find_element_by_xpath("/html/body/div[3]/div/div[2]/dl[1]/dd/div/p/a").click()
# xpath缺点：定位元素的可读性比较差
# 链接文本的方式：可读性更好
driver.find_element_by_link_text("进入商城购物").click()
# 8 在商城主页，输入搜索条件iphone
driver.find_element_by_name("keyword").send_keys("iphone")
# 9 点击搜索按钮
driver.find_element_by_class_name("btn1").click()
# 10 在搜索结果中点击第一个商品的图片
driver.find_element_by_xpath("/html/body/div[3]/div[2]/div[3]/div/div[1]/a/img").click()
# 关闭selenium正在工作的窗口
driver.close()
# 窗口切换
driver.switch_to.window(driver.window_handles[1])
# 11 点击：加入购物车
driver.find_element_by_id("joinCarButton").click()