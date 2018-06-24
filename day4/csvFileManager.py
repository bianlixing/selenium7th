# 要想读取csv文件，首先要导入csv代码库
# 这个csv也不用下载，是python内置的代码库
# 如果要读取excel需要下载相应的代码库：xlrd
# 怎么下载：1.通过命令下载：在dos窗口中，输入pip install -U xlrd
# selenium离线包，也可以通过命令行在线安装：pip install -U selenium 或者pip3 install -U selenium
# -U表示升级到最新版的意思；pip是python语言最常用的项目管理工具，和java中的maven类似
# 如果即装了2 又装了3 那么可能需要pip该称号pip3
# 方式2: 点击File--settings--project下边的project Interpreter--点击右上角+号，搜xlrd--选中并安装
import csv

# 2 指定要读取的文件的路径
path = 'C:/Users/51Testing/PycharmProjects/selenium7th/test_Data/test_data.csv'
# 因为字符串中包含反斜线\t等，怎么办？
# 方法1：每个反斜线前面加一个反斜线，进行转译
# 方法2：把每个反斜线都改成正斜线
# 相比第二种方法更好一点，因为java python都是跨平台语言
# 在字符串中两个反斜线会自动转换成一个反斜线
# 反斜线在windows用反斜线表示目录结构，但是在linux操作系统中，只有正斜线才能表示目录、
# 如果用双反斜线，则代码不能跨平台，limux用不了
# 如果用正斜线，代码可以同时在linux和windows中执行
# 方法3：在字符串外面加上字母r，会认为中间所有的代码都不存在转义字符
# path = r'C:\Users\51Testing\PycharmProjects\selenium7th\test_Data\test_data.csv'
# print(path)

# 3 打开路径所对应的文件
# 'r' 读模式 写不写都可以，open默认就是r模式
file = open(path,'r')
# 4 读取文件内容，通过什么读取？用我们导入的csv代码库
# reader()方法时专门用来读取文件的
data_table = csv.reader(file)

# 5 打印data_table中的每一行数据，写一个for-each循环
# for是循环的关键字，item代表每一行，每循环一次，item就代表最新的一行数据
# data_table表示整个文件中的所有数据
for item in data_table:
    print(item)

# 很多测试用例可能都需要从Excel中读取数据，所以我们应该对这些代码做一个简单的封装，建一个文件叫csvFileManager2，把以上代码封装到一个方法中
# 并且在创建一个文件读取封装的方法