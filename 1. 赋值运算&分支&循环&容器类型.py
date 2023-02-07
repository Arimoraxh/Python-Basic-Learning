# -*- coding: utf-8 -*-
"""
Created on Mon Nov  7 18:02:32 2022

@author: Mora
"""

print("hello, world!")

print('100+200 =', 100 + 200)

#运算符训练
a = 10
b = 3
a += b
a *= (a + 2)
print(a)

#输入输出训练，输入的内容会被认为是str，所以要转换成float
r = float(input('请输入圆的半径: '))
p = 2 * 3.1416 * r
s = 3.1416 * r * r
print('周长: %.2f' % p)
print('面积: %.2f' % s)

#同理，输出的是整数
r = int(input('r ='))
p = 1+r
print(r,p)

#格式化输出：使用占位符 %d表示整数，%f表示小数
a = float(input('请输入a的值='))
b = float(input('请输出b的值='))

print('%f//%f = %f' % (a, b, a//b))

#赋值运算符
a = 3
b = 4
a += b
print(a)

#逻辑运算符：把多个布尔值处理成一个布尔值，做一个布尔值的组合
#and：而且，只要有一个是错的，就是错的
#or:或者，但凡有一个是真的，就是真的
#not:真的变成假的，假的变成真的
#关系运算、比较预算的优先级，高于逻辑运算
#and和or也是短路运算符，先看左边的成立不成立，如果左边的不成立，右边的看了也是白看，用的时候一定要小心，容易有坑！！！

print(True or False or False)
print(True and False and True)

#例：判断a是不是一个大于50的偶数
a = int(input('a = '))
if a > 50:
    and
    a % 2 ==0
    print ('a 是大于50的偶数')
    
a = int(input('a = '))
flag1 = a > 50 
flag2 = a % 2 == 0
print(flag1 and flag2)

#练习1：输入一个年份，判断这个年份是不是闰年
#规则：四年一闰，百年不闰，四百年又闰
#解题思路：
a = int(input('年份 = '))
flag1 = a % 4 ==0
flag2 = a % 100 != 0
flag3 = a % 400 ==0
if (flag3 or flag2 and flag1) == True:
    print('a是闰年')
else:
    print('a不是闰年')

#练习2：输入三条边的长度，判断他们是否构成三角形
#规则：三角形的两边之和大于第三边
a = int(input('a = '))
b = int(input('b = '))
c = int(input('c = '))
if ((a + b > c) and (b + c > a) and (c + a > b)) == True:
    print('是一个三角形')
else:
    print('不是一个三角形')
    
#嵌套层次：代码越扁平越好；if else里面可以嵌套if else
#代码块：保持相同缩进的是同一个代码块
#练习：个人所得税计算器。规则：
#收入额为E，应纳税所得额为I=Max[E-3500,0]，税率为R，速算扣除数T为I×R-D，税后收入A=E-T
#第一次写的方案

E = int(input('请输入你的税前收入='))
if 0 < E <= 3500:
    A = E
    print('你的税后收入为',A)
else: 
    I = E - 3500
    if 3500 < E <= 5000:
        R = 0.03
        A = E - I * R
        print('你的税后收入为',A)  
    elif 5000 < E <= 8000:
        R = 0.1
        D = 105
        T = I * R - D
        A = E - T
        print('你的税后收入为',A)  
    elif 8000 < E <= 12500:
        R = 0.2
        D = 555
        T = I * R - D
        A = E - T
        print('你的税后收入为',A)  
    elif 12500 < E <= 38500:
        R = 0.25
        D = 1005
        T = I * R - D
        A = E - T
        print('你的税后收入为',A)  
    elif 38500 < E <= 58500:
        R = 0.3
        D = 2755
        T = I * R - D
        A = E - T
        print('你的税后收入为',A)  
    elif 58500 < E <= 83500:
        R = 0.35
        D = 5505
        T = I * R - D
        A = E - T
        print('你的税后收入为',A)
    elif E > 83500:
        R = 0.45
        D = 13505
        T = I * R - D
        A = E - T
        print('你的税后收入为',A)

#第二次写的方案
E = int(input('请输入你的税前收入='))
if 0 < E <= 3500:
    A = E
    print('你的税后收入为',A)
else: 
    I = E - 3500
    if E <= 5000:
        R = 0.03
        T = 0
    elif E <= 8000:
        R = 0.1
        D = 105
    elif E <= 12500:
        R = 0.2
        D = 555
    elif E <= 38500:
        R = 0.25
        D = 1005
    elif E <= 58500:
        R = 0.3
        D = 2755 
    elif E <= 83500:
        R = 0.35
        D = 5505
    elif E > 83500:
        R = 0.45
        D = 13505
    T = I * R - D
    A = E - T
    print('你的税后收入为',A)
    
#

E = int(input('请输入你的税前收入='))
if 0 < E <= 3500:
    
    A = E
    print('你的税后收入为',A)
else: 
    I = E - 3500
    if E <= 5000:
        R = 0.03
        T = 0
    elif E <= 8000:
        R = 0.1
        D = 105
    elif E <= 12500:
        R = 0.2
        D = 555
    elif E <= 38500:
        R = 0.25
        D = 1005
    elif E <= 58500:
        R = 0.3
        D = 2755 
    elif E <= 83500:
        R = 0.35
        D = 5505
    elif E > 83500:
        R = 0.45
        D = 13505
    T = I * R - D
    A = E - T
    print(f'你的税后收入为:{A:.2f}元')#输出的格式

#循环结构
#for i in range 内置语句range
#range(101):用来生产0到100的整数，取不到101
#range(1,101):用来生产1到100范围的整数，前面是闭区间，后面是开区间
#range(1,101,2):用来生产1到100的奇数，2是步长，即每次数值递增的值
#range(100,0,-2):用来生产100到0的偶数，-2是步长，即每次数值递减的值

#例题：计算从1到100的求和
total = 0

for i in range(101):
    total += i
    i +=1
    #如果在这个缩进打一个print(total)，就会有每一次加和的结果
print(total)

#第二种写法：利用函数sum
print(sum(range(1,101)))

#例题：找出100~999之间的水仙花数（各位数字的立方和刚好等于这个数本身）
# 153 = 1^3 + 5^3 + 3^3

for num in range(100,999):
    a = num // 100          #除以100取最大的商 = 1
    b = num // 10 % 10      #15 % 10 = 余5
    c = num % 10            #153 % 10 = 3
    if  a**3 + b**3 +c**3 == num:
        print(num)

#解法2
for num in range(100,1000):
    x = 0
    y = num
    while y !=0:
        a = y % 10
        y = y // 10
        x = x + a**3
    if x == num:
        print(num, '是水仙花数')

#补充练习：输入一个正整数N，将N进行翻转 
#记住破解的方法：在循环中，设置一个数为最后要被对比的数字
#想要取前一位就是//后%余

n = int(input('输入一个正整数'))
total = 0 #翻转后的数
while n > 0:
    total = total * 10 + n % 10
    n = n // 10
print(total)
    
#例题：输入一个正整数，判断它是不是质数，质数的意思就是，不能够被i和它本身以外整除
#解题思路：输入一个数，如果符合条件则是，不符合为否；遍历从2到他本身的所有数，看能不能被这中间的数整除。
#问题：输出了一堆n是质数。解决：加一个分支结构

n = int(input('输入一个正整数'))
a = True
for i in range(2,n):
    if n % i == 0:
        a = False
        break

if a == True:
    print('n是质数')
else:
    print('n不是质数')
---------------------------------------------
n = int(input('输入一个正整数'))
a = True
for i in range(2, int(n ** 0.5) +1):
    if n % i == 0:
        a = False
        break

if a == True:
    print('n是质数')
else:
    print('n不是质数')

#例题：输入一个正整数，输出小于n的所有质数
#解题思路：输入一个数，遍历从2到他自己的数，只要符合条件"能整除1和自身以外的任一数”则输出
n = int(input('输入一个正整数'))

for n in range(2,n):
    n_is_prime = True
    
    for i in range(2, int(n ** 0.5) +1):
        if n % i == 0:
            n_is_prime = False
            break
        
    if n_is_prime == True:
        print(n)

n = int(input('输出一个整数'))
print(n * (n + 1) * 0.5)

'''
例题：输入N，按照如下所示的规律进行打印：
N = 5
1
22
333
4444
55555

解题思路：①输入N，遍历小于N的数字n ②输出n个n ③输出的格式
'''
N = int(input('输出一个整数'))
for n in range(N + 1):
    for i in range(n):
        print(n,end = ' ')
    print('\n')

'''
输入三角形三边的长，如果能构成三角形就计算周长和面积；
如果不能构成三角形，提示用户重新输入，直到正确
解题思路：①输入长 ②判断是否构成三角形 ③如果构成，计算并停止循环；如果不构成，继续循环
'''
xunhuan = 1
while xunhuan == 1:
    
    a = int(input('输入一条边的长'))
    b = int(input('输入第二条边的长'))
    c = int(input('输入第三条边的长'))

    if a + b > c and a + c > b and a + b > c:
        perimeter = a + b + c
        p = (a + b + c) / 2
        s = p * (p - a) * (p - b) * (p - c) ** 0.5
        break
        
    else:
        print('不是三角形，请再来一遍！')

print('三角形的周长是',perimeter, '面积是', s)

'''
百钱百鸡问题
公鸡值钱5，母鸡值钱3，3只小鸡值钱1，用百钱买百鸡，问公鸡、母鸡、小鸡各多少只？

解题思路：①遍历x,y,z, ②如果符合条件，则输出x,y,z ③如果不符合条件，继续循环
x最大为20，y最大为33，z取0,3,6,9,最大为100
'''

for x in range(0, 21):
    for y in range(0, 34):
        for z in range(0, 100, 3):
            if x + y + z == 100 and 5 * x + 3 * y + z / 3 == 100:
                print('公鸡有', x, '母鸡有', y, '小鸡有', z)

'''
五个人（ABCDE)去捕鱼，捕了不计其数的鱼，然后累了去睡觉。
第二天，A醒过来把鱼分成了5份，扔掉多余的1条，然后拿走自己的1份
B第二个醒过来，以为鱼没有分过，把剩下的鱼分成了5份，扔掉多余的1条，拿走自己的1份
C、D、E依次醒过来，按照同样的方法来分鱼，他们最少捕了多少条鱼？

解题思路：①设鱼数为n，是整个循环当中最大的数，
②如果（n-1）% 5 == 0，可以继续执行5次分鱼的循环，
③如果5次循环之后这个数还是可以模除5，说明这个数是符合条件的数；如果不能，说明是错的，不用除5次了，继续遍历下一个n
④在所有符合条件的数里，要选择最小的数，所以整个循环在输出第一个n之后就break。

'''
#解法1：从小数到大
i = 1
n = 1
while i <= 5:
    n = 5 * n + 1 
    i +=1
            
print('最少捕了鱼数为', n)

#解法2：从大数到小
for n in range(5, 100000000):
    left = n
    n_is_prime = True
    
    i = 1
    while i <= 5:
        if (left - 1) % 5 == 0:
            left = (left-1) * 0.8 
            i +=1
            
        else:
            n_is_prime = False
            break
        
    if n_is_prime == True:
        print('最少捕了鱼数为', n)
        break

'''
例题：猜数字游戏
计算机产生一个 1-100的随机数，人输入自己猜的数字
计算机给出对应的提示“大一点”，“小一点”，或“恭喜你猜对了 ”，直到猜中为止
如果猜的次数超过7次，计算机温馨提示“智商余额明显不足”。

'''  
import random  
com_answer = random.randrange(1, 101)

i = 1
while i <= 7:
    your_answer = int(input('猜猜这个数字是几'))
        
    if your_answer == com_answer:
        print('恭喜你猜对了')
        break
    
    elif your_answer > com_answer:
        print('小一点')
        
    elif your_answer < com_answer:
        print('大一点')
            
    i += 1

if i > 7:
    print('智商余额明显不足')
    
#函数：相对独立且会被重复使用的功能
#将来想使用这些功能的时候，不用再复制黏贴代码，而是直接通过调用函数来做到。

'''

def f(x, a, b,):
    
    return y

放上自变量，返回因变量，把y赋给一个结果
可以没有因变量，也可以没有自变量；可以给自变量输入默认值，如果调用时没输入就自动用默认值

注意：函数的前后需要两个空行

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

--------------------------------------------

#容器型数据类型
# 列表（list）
# 元组（tuple）
# 集合（set）
# 字典（dict）

num = [10, 100, 1000]
print(type(num))

#列表专题
#1. 列表的遍历：把每个元素取出来

nums = [35, 98, 12, 27, 66]
#       0 , 1 , 2 , 3 , 4    ---正向索引
#       -5, -4, -3, -2, -1   ---负向索引
#取每一个元素：

for i in range(5):
    print(nums[i])

for i in range(-5, 0):
    print(nums[i]) 

#len() ---> length ---> 列表中有多少个元素
#通过len，把列表中的所有元素取出来
#第一种写法：只读
for i in range(len(nums)):
    print(nums[i])

#第二种写法：原来for循环可以不调用range！！---读&写操作
for num in nums:
    print(num)

#给列表中的元素加序号
for i in range(len(nums)):
    print(i, nums[i]) #给列表中的元素加序号
    nums[i] = 100     #改写
print(nums)

#先通过enumerate函数对列表进行预处理
for i, num in enumerate(nums):
    print(i, num)

#列表的应用案例：数据描述型计算和推断型统计
#输入10个整数，计算平均值、方差、标准差，找出最大值和最小值
nums = []   #尽量用一个复数形式
for _ in range (10):  #当想要循环多次，但是这个元素在后面me有用的时候，用一个下划线代替
    num = int(input('请输入数据：'))
    nums.append(num)
    
print (nums)    
mean_value = sum(nums) / len(nums)
variance = (num - mean_value) ** 2 / len(nums)
standard_var = variance ** 0.5
max_value, min_value = max(nums), min(nums)
    
    
print(f'均值：{mean_value}')
print(f'方差：{variance}')
print(f'标准差:{standard_var}')
print(f'极值：{max_value - min_value}')

#向列表中添加10个随机整数，找出其中第2大的元素
import random

nums = []
for _ in range (10):
    num = random.randrange(1, 100) 
    nums.append(num)
    
print(nums)

#通过max找到第一大的元素
max_value = max(nums)

#通过remove删除指定的元素
nums.remove(max_value)

print(max(nums))

------------第二种写法-----------

import random

nums = []
for _ in range (10):
    num = random.randrange(1, 100) 
    nums.append(num)
print(nums)
'''
判断前面两个数和其他数n，先使得数1一定大于数2，checklist：

①数1>数2>数n,输出数2 √
②数1>数n>数2,输出数n √
③数n>数1>数2输出数1 √

'''
max1, max2 = nums[0], nums[1]
if max1 < max2:
    max1, max2 = max2, max1
    
for i in range(2, len(nums)):
    if nums[i] > max2:
        max2 = nums[i]
    elif nums[i] > max1:
        max1, max2 = nums[i], max1

print(max2)

#列表的生成式语法

import random

nums = [random.randrange(1,100) for _ in range (10)]

print(nums)






































