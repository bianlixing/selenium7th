import csv
# 把读取文件的代码封装成一个方法
# 不需要继承，所以直接写：就可以
class CsvFileManager2:
    @classmethod
    def read(self):
        path =  'C:/Users/51Testing/PycharmProjects/selenium7th/test_Data/test_data.csv'
        file = open(path)
        # 通过csv代码库读取打开的csv文件，获取文件中所有的数据
        data_table = csv.reader(file)
        # for循环 item每一行 in在数据集 data_table表示数据集
        # data_table中有几行数据，循环几次
        for item in data_table:
            print(item)


# 前面是一个普通方法，不能直接执行，需要调用才能执行，所以写下边这三行代码来调用上面的方法
# 如果想在自己的方法里测试一下这个方法：
if __name__ == '__main__':
    #后面加个（）代表实例化对象
    # csvr = CsvFileManager2()
    # csvr.read()

# 如果在上面加上classmethod，表示这个方法可以直接用类调用
# 如果在方法上写一个classmethod，就不需要先实例化对象才能调用了
    CsvFileManager2.read()