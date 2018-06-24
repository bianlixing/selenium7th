import csv
# 每个测试用例对应着不同的csv文件
# 每条测试用例都会打来一个csv文件，所以每次也应该关闭该文件



class CsvFileManager3:
    @classmethod
    def read(self):
        path = 'C:/Users/51Testing/PycharmProjects/selenium7th/test_Data/test_data.csv'
        file = open(path)
        try: # try尝试执行以下代码
            data_table = csv.reader(file)
            a = [1,2,3,4,5]
            a[6]
            # 如何保证无论程序执行过程中是否报错，都能正常关闭该文件
            # 使用try...finally
            for item in data_table:
                print(item)
        # 方法最后应该添加close方法
        finally: # 无论try是否报错，都会执行finally下边的代码

            file.close()
            print("file.close() method is execute")



# 前面是一个普通方法，不能直接执行，需要调用才能执行，所以写下边这三行代码来调用上面的方法         
# 如果想在自己的方法里测试一下这个方法：
if __name__ == '__main__':
    # 后面加个（）代表实例化对象
    # csvr = CsvFileManager2()
    # csvr.read()

    # 如果在上面加上classmethod，表示这个方法可以直接用类调用
    # 如果在方法上写一个classmethod，就不需要先实例化对象才能调用了
    CsvFileManager3.read()