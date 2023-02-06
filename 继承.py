# -*- coding: utf-8 -*-
"""
Created on Mon Jan 23 19:52:11 2023

@author: Mora
继承
"""

'''
继承：从已有的类进行扩展，创建出新的类的过程
提供继承信息的类叫做父类（超类、基类），得到继承信息的类叫做子类（派生类）。

继承是一种is-a关系
a student is a person.
a teacher is a person.
a programmer is a person.

子类直接从父类继承公共的属性和行为，再添加自己特有的属性和行为
所以子类一定是比父类更强大的，任何时候都可以用子类对象去替代父类对象。

Python中的继承允许 多重继承， 一个类可以有多个父类。
不过不是必须使用多重继承的场景下，请尽量使用单一继承。一旦出现钻石继承或者菱形继承，就会很复杂，你根本不知道消息是谁发出的。

'''


from abc import abstractmethod
class Person:
    """人"""
    def __init__(self, name, gender):
        self.name = name
        self.gender = gender

    def ear(self):
        print(f'{self.name}正在吃饭')

    def play(self, game_name):
        print(f'{self.name}正在玩{game_name}')


class Student(Person):
    """学生"""
    def study(self, course_name):
        print(f'{self.name}正在学习{course_name}')


class Teacher(Person):
    """老师"""
    def __init__(self, name, gender, title):
        #super():帮你找到你爸爸，再执行爸爸的初始化方法
        super().__init__(name, gender) 
        self.title = title

    def teach(self, course_name):
        print(f'{self.name}正在讲授{course_name}')


teacher = Teacher('扎扎', True, '副教授')
stu = Student('涵涵', False,)

stu.study('python')
teacher.teach('python基础')


'''
两个类之前可能有哪些关系
~ is-a关系：继承 ---> class Student(Person) --->从一个类派生出一个类
~ has-a关系：关联 --->把一个类的对象作为另一个类的属性
    a person has an identity card.
    a car has an engine.
     - （普通）关联
     - 强关联：整体和部分的关联，聚合和合成
~ use-a关系：依赖 --->一个类的对象作为另外一个类的方法的参数或返回值
    a person use a vehicle.

'''

#唐僧去西天取经：has followers, use vehicles(horse, motobike), vehicle has engine
class Vehicle:
    def __init__(self):
        pass
                                
class Horse(Vehicle):
    pass

class Motobike(Vehicle):
    def __init__(self):
        self.engine = Engine()
        
class Engine:
    pass

class Folloers:
    pass

class MrTang:
    def __init__(self):
        self.followers = []

    def drive(self, venicle):
        pass

'''
工资（月薪）结算系统

面向对象编程的四大指出：
~ 抽象(abstraction):提取共性（定义类是一个抽象过程，做数据抽象和行为抽象）。
~ 封装(encapsulation):把数据和操作数据的函数从逻辑上组装成一个整体（对象）。
    --->隐藏实现细节，暴露简单的调用接口。
~ 继承(inheritance):拓展已有的类创建新类，实现对已有类的代码复用。
~ 多态(polymorphism)：给不同的对象发出同样的消息，不同的对象执行了不同的行为。
    --->方法重写(overide)
    
例子：三类员工
- 部门经理：固定月薪，15000元
- 程序员：计算结算月薪，每小时200元
- 销售员：底薪+提成，底薪1800元，销售额5%提成

录入员工信息，自动结算月薪

——————————
子类对父类已有的方法，重新给出自己的实现版本，这个过程叫做 方法重写
在重写方法的过程中，不同的字类可以对父类的同一个方法给出不同的实现版本，那么该方法在运行时就会表现出多态行为。

'''


class Employee:

    def __init__(self, no, name):
        self.no = no
        self.name = name

    @abstractmethod
    def get_salary(self):
        pass


class Manager(Employee):

    def get_salary(self):
        return 15000


class Programmer(Employee):

    def __init__(self, no, name):
        super().__init__(no, name)
        self.workinghour = 0

    def get_salary(self):
        return 200 * self.workinghour


class Salesman(Employee):

    def __init__(self, no, name):
        super().__init__(no, name)
        self.sales = 0

    def get_salary(self):
        return 1800 + 0.05 * self.sales


def main():
    emps = [
        Manager(1122, 'LiuBei'), Programmer(2233, 'ZhuGeLiang'),
        Salesman(3344, 'GuanYu'), Salesman(3344, 'ZhangFei'),
        Programmer(4455, 'PangChong'), Salesman(5566, 'MaChao')
    ]

    for emp in emps:
        if type(emp) == Programmer:
            emp.workinghour = int(input('请输入工作时长'))
        if type(emp) == Salesman:
            emp.sales = int(input('请输入销售额'))
        print(f'{emp.name}的本月工资是{emp.get_salary()}元')

    
    
if __name__ == "__main__":
    main()















