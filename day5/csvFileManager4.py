# 1 导包
import csv

import os


class CsvFileManager4:
    def read(self,filename):
        list=[]  # 声明一个空列表
        # 指定csv文件的路径
      #  path=r'C:\Users\51Testing\PycharmProjects\selenium7th\test_Data\test_dataa.csv'
        # 这样生成的path路径有一个缺点，可移植性比较差
        # 在公司中一个项目往往是多人协作完成，每个人把项目存放的位置不同，项目换了不同的路径，需要每次修改代码
        # 更好的方法是：
        # os.path.dirname(__file__)这是一个固定写法，用来获取当前文件的目录结构
        # os表示操作系统，path表示路径，dirname表示目录名，__file__是python内置的变量，表示当前文件
        base_path=os.path.dirname(__file__)
        print(base_path)
        # 用base_path的好处：无论项目放在任何路径下，都可以找到该文件的绝对路径
        # 真正想要的是csv文件的路径，不是代码文件的路径，二者区别在于：
        # 所以通过base_path计算出csv的值
        path=base_path.replace('day5','/test_Data/'+filename)
        print(path)

        # 3 打开指定文件，用open方法
       #  file=open(path,'r')
        # 每次打开文件最后都应该关闭文件，释放磁盘空间
        # 用try..finally的方法也不是很好
        # 更常用的方法是with... as....的语法结构
        with open(path,'r') as file:
            data_table=csv.reader(file)
        # 4 循环遍历数据表找那个的每一行
            for row in data_table:
                print(row)
        # 打印出数据不是目的，目的是测试用例需要调用这些数据
        # 所以要给这个方法设一个返回值，把数据提取出来
        # 5 声明一个二维列表，保存data_table中的所有数据
                list.append(row) # append 表示追加数据
        # 在read方法的结尾返回这个列表
        return list
    # 这个方法写完之后，是不是所有的测试用例都应该从这个方法读取csv数据?
    # 不可能为每个测试用例都单独写一个方法
    # 目前这个路径是写死的，只能读test_data.csv这个文件
    # 一个csv文件只适合保存一组测试用例的数据
    # 不同的测试用例应该有不同额csv文件
    # 应该把csv文件名作为一个参数传入 在read方法中加一个filename参数作为csv文件名，将filename加到path中，


if __name__ == '__main__':
    list=CsvFileManager4().read('test_data.csv')
    print(list[1][0])