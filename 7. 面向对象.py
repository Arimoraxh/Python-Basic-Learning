# -*- coding: utf-8 -*-
"""
Created on Sun Jan 22 12:04:29 2023

@author: Mora
面向对象的编程
"""

'''
1. 概述
从指令编程 ---> 面向过程（函数）编程  程序简单的时候没毛病
编程范式，也就是程序设计的方法论分为两种：面向对象编程 / 函数式编程

对象：是可以接收消息的实体，通过对给对象发消息达到解决问题的目标

对象 = 数据 + 函数（方法），也就是将数据和操作数据的函数从逻辑上变成了一个整体

类：将有共同特征（包括静态特征和动态特征）的对象共同特征抽取出来之后得到的一个抽象概念

简单地说，类是对象的模板，有了类才能创建出一种类型的对象

面向对象编程的路径：
1.定义类
    ~ 数据抽象：找到和对象相关的静态特征
    ~ 行为抽象：找到和对象相关的动态特征
2.造对象
3.给对象发消息

'''

'''
class 类：
    def __init__(类的名字，类的参数)：
        类的名字.类的参数 = ？
        
    def 方法(类的名字，方法的参数)：
        
'''

class Student:
    
    #数据抽象（属性）
    def __init__(self, name, age):
    #在创建完对象之后 会自动调用, 它完成对象的初始化的功能
        self.name = name
        self.age = age
        
    #行为抽象（方法）
    def eat(self):
        print(f'{self.name}正在吃饭')
        
    def study(self, course_name):
        print(f'{self.name}正在学习{course_name}')
        
    def play(self, game_name):
        print(f'{self.name}正在玩{game_name}')
        
        
'''
2. 创建对象的方法 / 给对象发消息

'''
if "__name__" == "__main__":
#from 面向对象 import Student

#第二步：使用构造器语法创建对象  类名(参数1， 参数2...)
    stu1 = Student('小涵', 25)
    stu2 = Student('扎扎', 37)

#第三步，给对方发消息，调用对象的方法，让对象做事情
    stu1.study('Python程序设计')
    stu2.play('吉他')
    
    stu1.age = 1
        

'''
练习1
定义圆类，创建两个圆的对象，通过给对象发消息求解
两个圆 过道58.5元每平米，围墙38.5元每米，r相差3m， 输入小圆的r，求解总计多少钱？

'''
import math

class Circle:
    def __init__(self, radius):
        self.radius = radius
        
    def perimeter(self): #周长
        return 2 * math.pi * self.radius

    def area(self): #面积
        return math.pi * self.radius ** 2

if __name__ == "__main__": #__name__属性是Python的一个内置属性，记录了一个字符串。若是在当前文件，__name__ 是__main__
    
    r = float(input('请输入游泳池的半径'))
    c1, c2 = Circle(r), Circle(r + 3)
    
    fence_price = c2.perimeter() * 38.5
    aisle_price = (c2.area() - c1.area()) * 38.5
    
    print(f'总计：{fence_price + aisle_price: .2f}元')


'''
创建一个时钟对象，可以 显示 时/分/秒， 让他 运转起来（走字）。
'''

import time

class Clock:
    def __init__(self, hour=0, minute=0, second=0):
        self.hour = hour
        self.minute = minute
        self.second = second
        
    def show(self):
        """显示时间"""
        return f'{self.hour:0>2d}:{self.minute:0>2d}:{self.second:0>2d}'

    def run(self):
        """走字"""
        self.second +=1
        if self.second == 60:
            self.second = 0
            self.minute += 1
            if self.minute == 60:
                self.minute = 0
                self.hour += 1
                if self.hour == 24:
                    self.hour = 0
                    
if __name__ == "__main__":
    clock = Clock(11,15,20) #输入起始的时间点
    while True:
        print(clock.show())
        time.sleep(1)
        clock.run()
        
        
#如果想要传入现在是几点，可以把位置参数改为关键字参数，这样输入就必须在所有的参数加上参数名    
    #def __init__(self, *,hour=0, minute=0, second=0):    

'''
定义描述三角形的类，提供计算周长和面积的方法

'''
class Triangle:
    
    def __init__(self, a, b, c):
        if a + b > c and b + c > a and a + c > b:
            self.a = a
            self.b = b
            self.c = c
        else:
            raise ValueError('无效的边长')
            
    def perimeter(self):
        return self.a + self.b + self.c
    
    def area(self):
        half = self.perimeter() / 2
        return(half * half - self.a) * (half - self.b) * (half - self.c) ** 0.5

'''
我们在类里面写的函数，通常称之为方法，他们基本上都是发给对象的消息，
但是有的时候，我们的消息并不是想发给对象，而是想发给这个类
这个时候可以使用静态方法 或者叫  类方法

静态方法 - @staticmethod（装饰器语法）
类方法 - @classmethod（装饰器语法）
'''


class Triangle2:

    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
        
        if not Triangle2.is_valid(a, b, c):
            #raise 引发错误
            raise ValueError('无效的边长，无法构成三角形！')

   # @classmethod
   # def is_valid(cls, a, b, c):  告诉这个消息是发给类的，不是发给对象的
   #     return a + b > c and b + c > a and a + c > b

    @staticmethod
    def is_valid(a, b, c):
        return a + b > c and b + c > a and a + c > b

    def perimeter(self):
        return self.a + self.b + self.c

    def area(self):
        half = self.perimeter() / 2
        return(half * half - self.a) * (half - self.b) * (half - self.c) ** 0.5


if __name__ == "__main__":
    try:
        t = Triangle2(1, 2, 4)

        print(t.perimeter())
        print(t.area())
    except ValueError as err:
        print(err)


#try后面只会执行1行，如果没有try...except结构，程序直接崩溃，如果有except捕捉到了异常，代码可以转到except处执行

'''
扑克游戏

我们通过构造器语法创建的对象基本都在堆空间，而对象的引用通常是放在栈上的，
通过对象引用（变量）就可以访问到对象并向其发消息

如果对象没有被引用，那么python解释器的自动内存管理会对其进行空间回收的处理
常量池
'''


'''
python中的魔术方法--->有特殊用途和意义的方法
    - __init__ --->初始化方法，在调用构造器语法创建对象的时候会被自动调用
    - __str__ --->获得对象的字符串表示，在调用print函数输出对象时会被调用
    - __repr__ --->获得对象的字符串表示，把对象放到容器中，用print输出容器时会自动调用
        representation

'''
from enum import Enum

class Suite(Enum):
    SPADE, HEART, CLUB, DIAMOND = range(4)

#for suite in Suite:
    #print(suite.value)
    
class Card:
    """牌"""

    def __init__(self, suite:Suite, face:int):
        """
        Parameters
        ----------
        suite : 花色
        face : 点数

        Returns
        -------
        None.
        """
        self.suite = suite
        self.face = face
        
    def __str__(self):
        #返回一个对象的描述信息，把对象的地址返回为字符串
        return self.show()

    def show(self):
        """牌"""
        suites = ['♠', '❤', '♣', '◇']
        faces = ['', 'A', '2', '3', '4', '5', '6',
                 '7', '8', '9', '10', 'J', 'Q', 'K']
        return f'{suites[self.suite.value]}{faces[self.face]}'?????????


def main():
    card1 = Card('H', 1)
    card2 = Card('S', 13)
    card3 = Card('D', 9)
    card4 = Card('C', 11)
    print(card1.show(), card2.show(), card3.show(), card4.show())
    #print(card1 is card2)：身份运算符，判断两个对象是否都引用了同一个对象
    print(card1, card2, card3, card4)  # <__main__.Card object at 0x000002693DB7D2E0>


if __name__ == "__main__":
    main()





















