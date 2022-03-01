class Book:
    def __init__ (self,name,author,publisher,year):
        self.name = name
        self.author = author
        self.publisher = publisher
        self.year = year
    def info(self):
        return "書名：{}\n作者：{}\n出版社：{}\n年份：{}\n".format(self.name,self.author,self.publisher,self.year)