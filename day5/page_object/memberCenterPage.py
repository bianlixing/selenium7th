from selenium.webdriver.common.by import By


class MemberCenterage:
    def __init__(self,driver):
        self.driver=driver
        self.url="http://localhost/index.php?m=user&c=index&a=index"


    welcome_link_loc=(By.PARTIAL_LINK_TEXT,'您好')

    """这个方法get_welcome_link 用于返回”您好“链接的所有文本内容，这是页面实际结果"""
    def get_welcome_link(self):
        return self.driver.find_element(*self.welcome_link_loc).text

    # 如果当前类中，赋值driver时，没有先用driver=webdriver.Chrom()
    # 那么后面写代码想使用selenium方法时，因为IDE（编译器）不知道driver类型，就不会给出提示
    #
