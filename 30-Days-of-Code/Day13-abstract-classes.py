# https://www.hackerrank.com/challenges/30-abstract-classes/problem?h_r=next-challenge&h_v=zen
from abc import ABCMeta, abstractmethod
class Book(object, metaclass=ABCMeta):
    def __init__(self,title,author):
        self.title=title
        self.author=author   
    @abstractmethod
    def display(): pass

#Write MyBook class
class MyBook(Book):
    def __init__(self, title, author, price):
        Book.__init__(self, title,author)
        self.price = price
    def display(self):
        self.title = title
        self.author = author 
        self.price = price
        print('Title: '+ self.title)
        print('Author: '+ self.author)
        print('Price: '+ str(self.price))

title=input()
author=input()
price=int(input())
new_novel=MyBook(title,author,price)
new_novel.display()
