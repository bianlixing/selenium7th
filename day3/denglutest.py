# selenium执行javascript中的两个关键字：return（返回值） 和 arguments（参数）
import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select

driver=webdriver.Chrome()
driver.implicitly_wait(20)
driver.get("http://localhost/")

# 点击登录链接
# 用javascript的方法找登录链接的代码：
#document.getElementsByClassName("site-nav-right fr")[0].childNodes[1]
# 用selenium找登录链接的代码：
# drover.find_element_by_link_text("登录")
# 某些元素用selenium的方法找元素比JavaScript更容易
# 但是selenium不支持removeAttribute的方法
# 但是selenium找到的登录链接和JavaScript扎到的是同一个元素
# 我们可以不可以用selenium找到元素之后，转换成JavaScript的元素
# 这样以后再写JavaScript时就容易很多，不需要childNodes这种方法
login_link = driver.find_element_by_link_text("登录")
# 把原来的JavaScript看成是一个无参无返方法，现在直接从外面传入一个页面元素，变成一有参午饭的方法
# 把selenium找到的元素传入到JavaScript这个方法里，代替原来的JavaScript定位元素
# arguments参数的复数形式，【0】表示第一个擦书，指的就是js后面的login_link
# 所以下边这句代码相当于把driver.find_element_by_link_text("登录")带入到JavaScript语句中。
# 变成driver.find_element_by_link_text("登录").removeAttribute('target')(此句不合理)
# argument是参数数组，指的是js字符串后面所有的参数，一般只用到argument【0】，即js后面的第一个字符串
driver.execute_script("arguments[0].removeAttribute('target')",login_link)
login_link.click()

# 登录
driver.find_element_by_name("username").send_keys("blx")
ActionChains(driver).send_keys(Keys.TAB).send_keys("blx123").send_keys(Keys.ENTER).perform()
# driver.find_element_by_name("password").send_keys("blx123")
# driver.find_element_by_class_name("login_btn").click()
# 返回商城主页
driver.find_element_by_link_text("进入商城购物").click()
# 搜索iphone
driver.find_element_by_name("keyword").send_keys("iphone")
driver.find_element_by_name("keyword").submit()
# driver.find_element_by_class_name("btn1").click()
# 购买商品，点击商品图片（用这种方法在实现一次窗口切换）
#css_selector:body > div.shop_last.w1100 > div.other_shopl.fl > div:nth-child(3) > div.other_user_shop_shop > div > div.shop_01-imgbox > a > img
# 复制出来的css比较长，我么你可以适当的缩减长度，我们定位元素的目标节点是最后一个节点，最后一个节点是不能被删除的，> 表示前面是父节点，后面是子节点。
# 每个节点的第一个单词是标签名，如：a，div, body
#小数点后面表示class属性
# :nth-child(3)，nth表示第几个，第n个，child表示子节点，所以:nth-child(3)表示当前标签是它父节点的第二个子节点
# xpath中是目标属性所在的路径
by_link=driver.find_element_by_xpath("/html/body/div[3]/div[2]/div[3]/div/div[1]/a")
# 目标节点一定是a节点，才能删除目标属性
driver.execute_script("arguments[0].removeAttribute('target')",by_link)
by_link.click()
# 加入购物车
driver.find_element_by_id("joinCarButton").click()

driver.find_element_by_css_selector(".shopCar_T_span3").click()

# 点击结算按钮
# 在每个class前面都加一个小数点，并且都去掉中间的空格，就可以同时用两个class属性定位
driver.find_element_by_css_selector(".shopCar_btn_03.fl").click()
# 点击添加新地址
driver.find_element_by_css_selector(".add-address").click()

# 输入收货人等信息地区是难点
driver.find_element_by_css_selector('[name="address[address_name]"]').send_keys("bb")
driver.find_element_by_css_selector('[name="address[mobile]"]').send_keys("13211111111")
# 下拉框是一种特殊的网页元素，对下拉框的操作和普通网页元素不太一样
# selenium为这种特殊的元素专门创建了一个类，叫select类
dropdown1=driver.find_element_by_id("add-new-area-select")
# dropdown1的类型是一个普通的网页元素
# 这句话的意思 是把一个普通的网页元素转化为下拉框
print(type(dropdown1)) # dropdown1是webelement类型
# webelement类中只有click和send_keys，没有选择下拉框选项的方法
select1 = Select(dropdown1)
print(type(select1)) # select1是Select类型
# 转换成select类型后，网页元素是不变的，但是select类有选择选项的方法
select1.select_by_value("320000")
time.sleep(2)
select1.select_by_visible_text("辽宁省")

# 找到沈阳市
# 因为是动态id 所以不能通过id定位
# 因为class重复，所以不能直接用class定位
# 可以用find_element的方法先找到页面中所有class=add-new-area-select的元素，然后再通过数组的方式选择第几个页面元素，类似于JavaScript方法
dropdown2=driver.find_elements_by_class_name("add-new-area-select")[1]
select2=Select(dropdown2)
select2.select_by_visible_text("沈阳市")

# 选择区
# 可以用tag_name定位
# tag_name这个方法大多数情况是可以找到许多元素的
# 所以find_element_tag_name这个方法很少用
# 但是find_elements_tag_name这个方法用的比较多
dropdown3=driver.find_elements_by_tag_name("select")[2]
# dropdown3=driver.find_elements_by_class_name("add-new-area-select")[2]
Select(dropdown3).select_by_visible_text("铁西区")

driver.find_element_by_css_selector('[name="address[address]"]').send_keys("xxx街道xxx号")
driver.find_element_by_css_selector('[name="address[zipcode]"]').send_keys("101110")
# 点击确定，保存输入
driver.find_element_by_css_selector(".aui_state_highlight").click()
