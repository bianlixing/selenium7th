# 这个文件是用来批量执行unittest的测试用例
#该文是我们这个测试工具的唯一入口
# 1 导入unittest，因为批量执行测试用例的 功能由unittest代码库提供
import smtplib
import unittest

import os
from email.mime.text import MIMEText

from package.HTMLTestRunner import HTMLTestRunner
def send_mail(path):
    # 1 通过path打开生成的测试报告文件
    # html格式不是文本格式，需要制定以二进制的方式打开
    file=open(path,'rb')
    # 2 读取文件的内容作为邮件的征文
    msg=file.read()
    # 把读取出来的内容转换成MIMEText的格式
    # _subtype:邮件类型分三种：纯文本（plain），html，富文本
    mime=MIMEText(msg, _subtype='html', _charset="utf-8")
    # 4 除了征文意外，还需要设置主题，发件人，收件人
    mime['subject']='博为峰测试报告'
    # 发件人：'bwftest126@126.com', 'abc123asd654'
    # 因为发件人需要登录的客户端授权码
    # 第三方登录不能直接用密码，必须用授权码
    mime['From']='bwftest126@126.com'
    mime['To']='blx126youxiang@126.com'
# 传输协议发送邮件
    # 1 实现构造方法
    smtp=smtplib.SMTP()
    # 2 链接126邮箱
    smtp.connect("smtp.126.com")
    # 3 登录邮箱
    smtp.login('bwftest126@126.com', 'abc123asd654')
    # 4 发送邮件
    smtp.send_message(mime,from_addr='bwftest126@126.com', to_addrs='blx126youxiang@126.com')
    #smtp.sendmail(from_addr='bwftest126@126.com', to_addrs='blx126youxiang@126.com',msg=mime.as_string())
    # 5 退出邮箱
    smtp.quit()



if __name__ == '__main__':
    # 2 要想批量执行首先要明确要执行哪些测试用例
    # 只能执行继承了unittest.TestCase的类
    # 比如执行这个项目中所有unittest的测试用例
    # defaultTestLoader是默认的测试用例的加载器，可以用来发现所有的测试用例
    # *表示通配符，可以代替任何字符
    # *Test.py表示已Test.py结尾的所有文件
    # .表示当前路径，即项目的根路径
    # top_level_dir=None可以删掉
    # suite随意起的变量名，suite本身是测试用例集的意思
    suite=unittest.defaultTestLoader.discover('./day5', pattern='*Test.py')
    # 当前文件下的所有测试用例
    #suite=unittest.defaultTestLoader.discover('.', pattern='*.py')
    # 找到测试用例后 执行测试用例
    # TextTestRunner()文本的测试用例的运行器
    # unittest.TextTestRunner().run(suite)

    # 生成HTMLTestRunner测试报告
    # HTMLTestRunner类似于TextTestRunner()，都是执行测试用例，
    # 区别在于他们执行完所有测试用例的输出结果
    # 一个是Text，另一个是HTML
    # Text会被打印到控制台中，HTML会单独生成一个文件
    # 相比于text，html结构更清晰
    # 二者选其一即可，用html代替text
    # HTMLTESTRunner().run(suite)代替TextTestRunner().run(suite)
    # 我们需要把声称的html格式的测试报告保存到一个固定位置，方便查看
    # 在项目根节点下创建一个文件夹，report
    # 以后测试报告就保存在report下边
    # 5 查找report路径
    base_path=os.path.dirname(__file__)
    path=base_path+'/report/test_report.html'
    # 6 创建测试文件
    # html格式不能直接写入，有可能存在图片，所以用wb
    file=open(path,'wb')
    # stream：数据流
    HTMLTestRunner(stream=file, verbosity=1, title='博为峰测试报告', description='测试环境Server2008；浏览器："Chrom"').run(suite)

    # 7 把测试报告作为邮件发送，好处是，可以敲及时提醒的作用
    # 前提条件，准备两个邮箱
    # 版本控制的前提条件申请一个git账号
    # 把html格式的测试报告作为邮件的征文发送

    send_mail(path)
