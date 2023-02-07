# -*- coding: utf-8 -*-
"""
Created on Mon Dec 26 13:04:07 2022

@author: Mora

函数
"""

#函数：相对独立且会被重复使用的功能
#将来想使用这些功能的时候，不用再复制黏贴代码，而是直接通过调用函数来做到。

'''

def f(x, a, b):
    
    return y

放上自变量，返回因变量，把y赋给一个结果
可以没有因变量，也可以没有自变量；可以给自变量输入默认值，如果调用时没输入就自动用默认值

注意：函数的前后需要两个空行

自变量(argument)一般叫做参数(parameter)
因变量一般为返回值(return)

'''

#判断质数题重写
def is_prime(num):
    '''
    
    Parameters
    ----------
    num : 自变量 判断这个数是不是质数

    Returns
    -------
    a : True是质数，False不是质数

    '''
    a = True
    for i in range(2, int(num ** 0.5) + 1 ):
        if num % i == 0:
            a = False
            break

    return a   
    
is_prime(4)
print ("num是质数 ", is_prime(4))

'''
如果给了自变量的值，自变量的值会替换掉参数的默认值
'''
'''
重构：Refactor，不改变代码的功能的前提下，改变代码的结构 ---> exactor method

'''

'''
全局变量和局部变量
全局变量：没有写在任何函数里面的变量
局部变量：定义在函数内部的变量

函数里面的局部变量和全局变量x是两个不同的变量，相互没有关系，各不影响


python程序中搜索一个变量，按照LEGB顺序搜索：
Local(局部作用域) ---> Embeded(嵌套作用域) ---> Global(全局作用域) ---> Built-in(内置作用域) ---> name not defined
Embeded(嵌套作用域)
Built-in(内置作用域) ---> py默认定义好的
'''
x = 100


def foo():
    x = 200 #这是重新定义的局部变量，如果上面的x没有给定义，下面就会输出不了
    print(x) #输出的是200
    
foo()
print(x) #输出的是100，与函数内部的x没有关系

#顺序规则：
x = 100


def foo():
    x = 200
    
    
    def bar():
        x = 300
        print(x)
        
    print(x)
    
    
foo()
print(x)


#如果不想再函数foo中定义局部变量x。想直接使用全局变量x，应该怎么做
#global ---> 声明使用全局变量，或者将一个局部变量放到全局作用域
#但是不作用到local的

x = 100

def foo():
    global x
    x = 200
    
    
    def bar():
        x = 300
        print(x) #300
        
        
    bar()
    print(x) #200
    
foo()
print(x) #200

#如果不想在函数bar找那个定义局部变量x。想直接使用嵌套作用域中的x，应该怎么做？
#nonlocal ---> 声明使用嵌套作用域的变量，不使用局部变量
x = 100

def foo():
    x = 200
    
    
    def bar():
        nonlocal x 
        x = 300
        print(x) #300
        
        
    bar()
    print(x) #300
    
foo()
print(x) #100

'''
example：获取A班和B班的考试成绩的描述型统计信息，比较A班和B班哪个班的学习效果更明显。
'''
import random

classs_a_scores = [random.landrange(50, 101) for _ in range(50)]
classs_b_scores = [random.landrange(50, 101) for _ in range(50)]

print('A班考试成绩描述性统计信息')

'''
摇色子游戏
'''

#通过一个自变量num告诉代码要摇几个色子，适用性更强


def roll_dice(num):
    #双引号+回车，会自动生成一个注释结构
    """
    摇色子
    :param num:色子的数量（对自变量进行说明）
    :return:摇出的点数（对因变量进行说明）  
    """
    total = 0
    for _ in range(num):  # 如果是摇两个色子，可以直接写num=2；如果调用函数的时候没有给自变量，就用默认值
        total += random.randrange(1, 7)
    return total


def win():
    #这里不需要返回值
    """赢"""
    global money
    print('玩家胜！')
    money += bet_money


def lose():
    """输"""
    global money
    print('庄家胜！')
    money -= bet_money


money = 1000
while money > 0:  # 玩家的初始资金是1000，还没输光前都要一直循环

    bet_money = int(input('下注多少钱'))

    #result1 = random.randrange(1, 7) + random.randrange(1, 7)
    first_point = roll_dice(2)  # 把f(x)赋给一个值，num写在f(x)里面
    print(f'摇出了{first_point}点')

    if first_point in (7, 11):
        win()

    elif first_point in (2, 3, 12):
        lose()

    else:
        while True:  # 我不知道循环次数，但是不知道条件，所以在适当的时候用break
            #如果给了自变量，会替换掉函数中的默认值
            curr_point = roll_dice(2)
            print(f'摇出了{curr_point}点')
            if curr_point == first_point:
                win()
                break

            elif curr_point == 7:
                lose()
                break
            else:
                pass
print('玩家破产，游戏结束')




'''重构随机球代码'''

n = int(input('机选几注：'))


def generate():
    """
    生成一组彩票号码

    Returns
    -------
    selected_balls : 存储保存的号码

    """
    red_balls = [i for i in range(1, 34)]
    blue_balls = [i for i in range(1, 17)]
    
    selected_balls = random.sample(red_balls, 6)
    selected_balls.sort()
    
    selected_balls += random.choices(blue_balls, k=1)
    return selected_balls

def display(balls):
    """
    显示一组彩票号码
    ----------
    balls : 装彩票号码对应的球的列表
    """
    for ball in balls:
        print(f'{ball:0>2d}', end=' ')
    print()
    

for _ in range(n):
    display(generate())
    

    
'''
一个函数既完成大乐透，也完成双色球
大乐透的玩法：前区号码和后区号码，前区号码范围为1~35，后区为1~12，大乐透每期从35个前区
号码中开出5个号码，从12个后区号码中开出2个号码作为中奖号码，
竞猜开奖号码的5个前区号码和2个后区号码，顺序不限。

思路：①generate函数中：分别生成两组号码，号码的数量、抽取的数量可以定义。

'''
import random

n = int(input('机选几注：'))


def generate(red_ball_max=33, red_ball_num=6,
             blue_ball_max=16, blue_ball_num=1):
    """
    生成一组彩票号码
    
    Param red_ball_max:红色球的最大值
          red_ball_num:抽取红色球的数量
          blue_ball_max:蓝色球的最大值
          blue_ball_num:抽取蓝色球的数量
    Returns
    -------
    selected_balls : 保存一组彩票号码的列表
    """
    red_balls = [i for i in range(1, red_ball_max + 1)]
    blue_balls = [i for i in range(1, blue_ball_max + 1)]

    selected_balls = random.sample(red_balls, red_ball_num)
    selected_balls.sort()

    selected_balls += random.choices(blue_balls, k=blue_ball_num)
    return selected_balls


def display(balls, red_ball_num=6):
    """
    显示一组彩票号码
    ----------
    Param balls : 装彩票号码对应的球的列表
    """
    for ball in balls[:red_ball_num]:
        print(f'{ball:0>2d}', end=' ')
    print('|', end = ' ')
    for ball in balls[red_ball_num:]:
        print(f'{ball:0>2d}', end=' ')
    print()


print('双色球:')
for _ in range(n):
    display(generate(33, 6, 16, 1))

print('大乐透:')
for _ in range(n):
    display(generate(35, 5, 12, 2), 5)






'''
继续重构，把两组数据编成同一个函数
'''

n = int(input('机选几注：'))


def generate(ball_max, ball_num):
    """
    生成一组彩票号码
    
    Param ball_max:号码的最大值
          ball_num:号码的数量
    Returns
    -------
    selected_balls : 保存一组彩票号码的列表
    """
    balls = [i for i in range(1, ball_max + 1)]
    selected_balls = random.sample(balls, ball_num)
    selected_balls.sort()

    return selected_balls

def make_big_lottery():
    """生成大乐透的号码"""
    return generate(35, 5) + generate(12, 2)


def make_two_colors():
    """生成s双色球的号码"""
    return generate(33, 6) + generate(16, 1)


def display(balls, first_ball_num):
    """
    显示一组彩票号码
    ----------
    Param balls : 装彩票号码对应的球的列表
    """
    for ball in balls[:first_ball_num]:
        print(f'{ball:0>2d}', end=' ')
    print('|', end = ' ')
    for ball in balls[first_ball_num:]:
        print(f'{ball:0>2d}', end=' ')
    print()


print('双色球:')
for _ in range(n):
    display(make_two_colors(),6)

print('大乐透:')
for _ in range(n):
    display(make_big_lottery(),5)





"""
计算组合数： C(M, N) = M! / N! / (M - N)!
将来可以用自己自定义的函数，也可以用第三方库别人写好的函数
"""
import math

def f(x):
    return math.factorial(x)
    
m = int(input('m = '))
n = int(input('n = '))
    
print(f(m) // f(n) // f(m - n))



#判断质数题再重写
def is_prime(num):
    '''
    Parameters
    ----------
    num : 自变量 判断这个数是不是质数

    Returns
    -------
    是质数返回True，不是质数返回False
    '''

    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False

    return True


for n in range(2, 100):
    if is_prime(n) == True:
        print(n, end=' ')

    
"""
用函数实现求两个数的最大公约数和最小公倍数
解释定义：
几个整数，公有的约数，叫做这几个数的 公约数；其中最大的一个，叫做这几个数的最大公约数。例如：12、16的公约数有1、2、4，其中最大的一个是4，4是12与16的最大公约数，一般记为（12，16）=4。12、15、18的最大公约数是3，记为（12，15，18）=3。
几个自然数公有的倍数，叫做这几个数的 公倍数，其中最小的一个自然数，叫做这几个数的最小公倍数。例如：4的倍数有4、8、12、16，……，6的倍数有6、12、18、24，……，4和6的公倍数有12、24，……，其中最小的是12，一般记为[4，6]=12。12、15、18的最小公倍数是180。记为[12，15，18]=180。若干个 互质数的最小公倍数为它们的乘积的 绝对值。
"""
#设计函数最为重要的原则：单一职责原则（一个函数只做好一个事情），之后换可以灵活组装函数
#写程序的终极原则：高内聚，低耦合。---> high cohesion low coupling

def gcd(x: int, y: int) -> int:
    #欧几里得算法：
    while y % x != 0:
        x, y = y % x, x
        
        return x
    
def lcm(x: int, y: int) -> int:
    #求最小公倍数：
    return x * y // gcd(x, y)

'''
描述性统计
集中趋势：均值、中位数、众数
离散趋势：极差、方差、标准差
'''
import random
import math

def peak_to_peak(data):
    return max(data) - min(data)

def average(data):
    return sum(data) / len(data)

def variance(data):
    x_bar = average(data)
    total = 0
    for num in data:
        total += (num - x_bar) ** 2
    return total / (len(data) - 1)

def standard_deviation(data):
    return math.sqrt(variance(data))

def middle(data):
    #先给data排序
    temp, size = sorted(data), len(data)
    if size % 2 != 0:
        return temp[size // 2]
    else:
        return average(temp[size // 2 - 1: size // 2 + 1])
    
nums = [random.randrange(1, 100) for _ in range(8)]
print(nums)
print(f'均值:{average(nums)}')
print(f'级差:{peak_to_peak(nums)}')
print(f'方差:{variance(nums)}')
print(f'标准差:{standard_deviation(nums)}')
print(f'中位数:{middle(nums)}')

'''
1. 方法一：使用其他文件（模块）中定义的函数，可以通过import导入模块，然后通过“模块名.函数名”的方式
方法二：还有一种做法是直接从模块中导入函数 ---> “from 模块 import 函数”

2. 导入函数的时候可以进行别名：“from 模块 import 函数 as avg, standard_deviation as std”
可以解决命名冲突的问题

3. 解决命名冲突的方式2：使用完全限定名（qualified name）--->[包名.]模块名.函数名

4. 做工程化项目开发时，如果项目中的代码文件非常多，我们可以用包来管理模块，
再通过模块来管理函数，包（package）是文件夹，模块（module）是python文件，
通过这种方式可以解决大型项目团队开发中经常遇到的命名冲突问题。

python中的from、import、as关键字就是专门用来处理包和模块的
'''

'''
例子：utils.foo.say_hello()
utils.bar.say_hello()

'''

'''
在设计函数的时候，函数的参数个数暂时无法确定：可变参数，可以接受0个或任意多个位置参数
arguments：参数，简写args，用*把所有元组当中的元素打包
位置参数--->positional argument
关键字参数--->keyword argument，例如 a=1, b=2, c=3, 参数名=参数值

如果希望既希望加入位置参数，又希望加入关键字参数：
**kwargs--->可以接收0个或任意多个关键字参数--->将所有的关键字参数打包成一个字典

'''
def add(*args, **kwargs):
    print(args,type(args)) #tuple
    print(kwargs,type(kwargs))
    total = 0
    for arg in args:
        if type(arg) in (int, float):
            total += arg
    for kwarg in kwargs:
        if type(kwarg) in (int, float):
            total += kwarg
    return total
    
#print(add())
#print(add(1))
#print(add(1,2))
#print(add(1,2,3))1
#print(add(1,2,3,4))

print(add(1, 2, c=3, b=2, a=1, d='hello'))



def get_shffix(filename: str, has_dot = False):
    """
    Parameters
    ----------
    filename : 文件名
    has_dot : 后缀名是否含有.

    Returns
    -------
    后缀名

    """
    position = filename.rfind('.')
    if position <= 0:
        return ''
    if not has_dot:
        position = position + 1
    return filename[position:] 

#定义函数时，写在*前面的参数称为位置参数，调用函数传递参数时只需要对号入座
#写在*后面的参数称为 命名关键字参数，调用参数传递参数时，必须写成“参数名=参数值”
def get_shffix2(filename, *, has_dot=False):
    position = filename.rfind('.')
    if position <= 0:
        return ''
    if not has_dot:
        position = position + 1
    return filename[position:] 
    

print(get_shffix2('hello.py'), True)
print(get_shffix2('hello.py.txt'))

#调用函数参数时，可以给函数带上名字：这种参数称为关键字参数
print(get_shffix2(has_dot=True, filename='hello.py.txt'))
print(get_shffix2('hello'), True)
print(get_shffix2('hello.'), True)
print(get_shffix2('.hello'), True)

'''

python中的函数是一等函数（一等公民）：
1. 函数本身可以作为函数的参数
2. 函数可以作为函数的返回值
3. 函数可以赋值给变量

如果将函数作为函数的参数或者返回值，这种玩法通常称之为高阶函数
通常使用高阶函数，可以将原本的函数解耦

'''
#乘法和加法运算也可以作为函数，不用写死：
def calculate(init_value, fn, *args, **kwargs):
    pass
#fn ---> 一个实现二元运算的函数，可以做任何一种二元运算
    total = init_value
    for arg in args:
        if type(arg) in (int, float):
            total = fn(total, arg)
    return total

def add(x, y):
    return x + y

def mul(x, y):
    return x * y

def sub(x, y):
    return x - y

#函数可以直接写名字，不用写参数
print(calculate(0, add, 11, 22, 33, 44))
print(calculate(0, sub, 11, 22, 33, 44))


#也可以直接调用operator模块：

from operator import add, sub, mul

def calculate(init_value, fn, *args, **kwargs):
    pass
#fn ---> 一个实现二元运算的函数，可以做任何一种二元运算
    total = init_value
    for arg in args:
        if type(arg) in (int, float):
            total = fn(total, arg)
    return total


#函数可以直接写名字，不用写参数
print(calculate(0, add, 11, 22, 33, 44))
print(calculate(0, sub, 11, 22, 33, 44))
print(calculate(0, mul, 11, 22, 33, 44))

#Lambda函数 ---> 没有名字而且一句话就可以写完的函数
#lambda 参数x, 参数y: 返回值

def calculate(*, op, init_value=0, **kwargs):
    pass

    total = init_value
    for kwarg in kwargs:
        if type(kwarg) in (int, float):
            total = fn(total, kwarg)
    return total

print(calculate(11, 22, 33, 44, op=lambda x, y: x + y))

fn = lambda x, y: x - y
print(calculate(11, 22, 33, 44, op=fn, init_value=100, ))
print(calculate(0, mul, 11, 22, 33, 44))

'''
练习：编写实现对列表元素进行冒泡排序的函数

设计函数的时候，一定要注意函数的无副作用性，调用函数不影响传入的参数。
'''
def bubble_sort(nums, ascending=True, gt=lambda x, y: x > y) :
    """
    冒泡排序
    Parameters
    ----------
    nums：待排序的列表
    ascending: 升序=True，降序=False
    gt：比较两个元素大小的函数

    Returns
    -------
    排序后的列表

    """
    nums = nums[:] #记得将列表复制一份
    for i in range(1, len(nums)):    
        swapped = False   
        for j in range(0, len(nums) - i):
            if gt(nums[j], nums[j + 1]):
                nums[j], nums[j + 1] = nums[j + 1], nums[j] 
                swapped = True
        if not swapped:
            break
    if not ascending:
        nums = nums[::-1]
    return nums

if __name__ == '__main__':
    
    nums = [35, 12, 99, 58, 67, 42, 49, 31, 33]
    #nums = [9, 1, 2, 3, 4, 5, 6, 7, 8]
    
    print(bubble_sort(nums))
    print(nums)
    
    words = ['apple', 'watermelon', 'hello', 'zoo', 'internationalization']
    print(bubble_sort(words, ascending=True, gt=lambda x, y: len(x) > len(y)))

'''
练习：二分查找
'''
def bin_search(items: list, key):
    start, end = 0, len(items) -1 #是list当中元素的索引值
    while start <= end:
        mid = (start + end) // 2
        if key > items[mid]:
            start = mid + 1
        elif key < items[mid]:
            end = mid - 1
        else:
            return mid #返回元素的位置
    return -1

if __name__ == '__main__':
    nums1 = [35, 96, 12, 78, 56, 64, 39, 80]
    print(bin_search(nums1, 12))
    print(bin_search(nums1, 80))
    print(bin_search(nums1, 95))
    #以下顺序的结果和上面的结果是一样的
    nums2 = [12, 35, 39, 56, 64, 78, 80, 96]
    print(bin_search(nums1, 12))
    print(bin_search(nums1, 80))
    print(bin_search(nums1, 95))


'''
函数的递归调用：
函数可以自己调用自己吗？

函数如果直接或间接地调用了自身，这种调用就叫做递归调用（recursion）

每个函数都有属于自己的栈结构，保存现场就是将整个栈结构保存起来
函数执行结束或者执行了return，就会出栈，FILO，first in last out
保存现场 --> 调用函数--> 恢复现场

所以一定要有节制，无休止的调用会将栈空间消耗殆尽，导致程序崩溃，CPython默认支持调用栈大小为1000次，
内存中只有极小的一部分属于栈空间，512k或1M等
如果不能快速收敛，可能产生下面的错误：
RecursionError: maximum recursion depth exceeded

'''
#以下是执行不出来的
def foo():
    print('foo')

def bar():
    foo()
    print('bar')
    
def main():
    a, b = 5, 10
    bar() 
    print(a, b)
    print('Game Over!')
    
if __name__ == '__main__':
    main
    
def foo():
    print('foo')
    foo()
    
def main():
    foo()
    

#以求阶乘为例：
#原代码：n! = n * (n - 1) * (n - 2)... * 2 * 1
def fac(num: int) -> int:
    result = 1
    for i in range(2, num + 1):
        result *= i
    return result

if __name__ == '__main__':
   print(fac(5))
    
#改写的代码：n! = n * (n - 1)!
def fac(num: int) -> int:
    if num == 1:
        return 1
    return num * fac(num - 1)

if __name__ == '__main__':
   print(fac(5))
    
'''
递归函数的两个要点：
1. 递归公式（第n次跟第n-1次的关系）
2. 收敛条件（什么时候停止递归调用）
'''


















