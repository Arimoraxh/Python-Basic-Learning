# -*- coding: utf-8 -*-
"""
Created on Thu Dec  1 21:48:19 2022
列表学习

@author: Mora
"""

1. 列表的操作
1.1 列表的创建
a. 方式一：字面量语法
#直接去给list赋值
list1 = ['apple','orange','pitaya','durian']

b. 方式二：构造器语法
#用一个表达式
list2 = list(range(1, 10))

c. 方式三：生成式语法/推导式语法
#i的处理+循环
list3 =[i ** 2 for i in range(1, 10)]
print(list3)

1.2 获取列表元素的个数 --->len()

1.3 遍历列表中的元素
for i in range(len(list1))
    print(list[i])

for i, x in enumerate(list1):
    print(i, x)

1.4 列表相关的运算
#重复运算
list4 = [1, 10, 100] * 5

#成员运算，结果是True/False
print(10 in list4)
print(5 not in list4)

1.5 列表的合并
list5 = [1, 3, 5, 7]
list6 = [4, 4, 8]
temp = list5 + list6
print(temp)

1.6 列表的比较
list7 = list(range(1, 10, 2))
list8 = [1, 3, 5, 7, 9]
#比较两个列表的元素是否一一相等
print(list7 == list8)
print(list7 != list8)
print(list7 > list8)

1.7 添删改查
1.7.1 添加元素
items = ['banana', 'grape', 'apple', 'waxberry', 'pitaya']

items.append('blueberry')
items.insert(1, 'watermelon')
print(items)

1.7.2 删除元素
items = ['banana', 'grape', 'apple', 'waxberry', 'pitaya', 'apple']
items.pop(4)
items.remove('apple')#看官方文档才知道，只删了第一个apple
print(items)

1.7.3 清空元素
items.clear()

1.7.4 查找元素
items = ['banana', 'grape', 'apple', 'waxberry', 'pitaya']
if 'strawberry' in items:
    print(items.index('strawberry'))

1.7.5 扩展元素
list6.extend(list5)
    
print(items.index('waxberry'))
#输出的是：3

1.7.4 反转
items.reverse()

1.7.5 排序
items.sort()

nums = ['1', '10', '234', '2', '35', '100']
nums2 = [int(num) for num in nums] #把列表当中的字符串变成整数
nums2.sort()
print(nums2)

或者下面这种写法：
nums = ['1', '10', '234', '2', '35', '100']
nums.sort(key = int) #排序的规则是 把元素变成整数 对整数进行排序 
print(nums)

2. 排序算法

2.1 简单选择排序
思想：每次从剩下的元素中选择最小的，依次加入到新的列表中

nums = [35, 12, 99, 58, 67, 42, 49 , 31, 33]
#设一个排好了序的新列表
sorted_nums = []

while len(nums) > 0:
    min_value = min(nums)
    sorted_nums.append(min_value)
    nums.remove(min_value)

print(sorted_nums)

2.2 




2.3 冒泡排序
思想：元素两两比较，如果前面的元素大于后面的元素，就交换两个元素的位置

nums = [35, 12, 99, 58, 67, 42, 49, 31, 33]
nums = [9, 1, 2, 3, 4, 5, 6, 7, 8]
for i in range(1, len(nums)):    #找到规律之后是j - i次
    swapped = False   #先假设没有发生过交换
    for j in range(len(nums) - i):
        if nums[j] > nums[j + 1]:
            nums[j], nums[j + 1] = nums[j + 1], nums[j] 
            swapped = True
    if not swapped:
        break
        
print(nums)

#修正代码，提升效率：

2.4 搅拌排序（鸡尾酒排序）


3.列表的应用
import random
names = [
    '小白', '小黑', '小A', '小B', '小C', '小黄', '小红'    
    ]
#用random.sample()函数进行无放回抽样
print(random.sample(names, k = 5))

#用random.choices()函数进行有放回抽样，可以重复抽中
print(random.choices(names, k = 5))

#用random.choices()函数进行随机选择一个元素
print(random.choice(names))

#实现列表中数据的随机打乱
random.shuffle(names)

'''
例题：幸运的女人
有15个男人和15个女人坐船出海，船坏了，需要把其中15个人扔到海里，其他人才能活下来；
所有人围成一圈，由某个人从1开始依次报数，报到9的人被扔到海里，下一个人重新从1开始报数，
直到将15个人扔到海里；最后，15个女人都幸存了下来，15个男人都被扔到了海里。
问原先哪些位置是男人，哪些位置是女人。

'''
#第一种解题思路：把所有的人赋为True，被扔掉的标为False
#我需要以下几个数字：
index = 用于记位置，index只能小于等于30
counter = 计算器，计算扔掉的有多少个数，counter == 15时，停止循环
num = 报数，num为9的时候被扔掉，对应index的值改为false，num重新回到0
因此：

persons = [True] * 30
index, counter, num = 0, 0, 0

while counter < 15:
    if persons[index] == True:  #加上这一句判断，让已经运算过了的不要再计数
        num += 1
    
        if num == 9:
            persons[index] = False
            counter += 1
            num = 0
            print(index, num)   
        
    index += 1    
    if index == 30:
        index = 0
        
print(persons)

--------------------------

#第二种解题思路：被扔掉的从列表中删除;
#输出的列表是一串数字。。。期望结果是输出女还是男，因此判断如果数字在列表中，就输出女，反之输出男
persons = [i for i in range(1, 31)]
for _ in range (15):
        persons = persons[9:] + persons[:8] #丢掉所有8的数
for i in range (1, 31):
    print( if i in persons else '男', end = ' ')


'''
例题：用一个列表保存54张扑克牌，先洗牌
再按斗地主的发牌方式把牌发给三个玩家，多的3张牌给第一个玩家（地主）
最后把每个玩家手上的牌显示出来

'''
import random

colors = ['黑桃','梅花','方块','红桃']
numbers = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
cards = []

for i in range(len(colors)):
    for j in range(0,len(numbers)):
        cards.append(f'{colors[i]}{numbers[j]}')

cards.append('小王')
cards.append('大王')

random.shuffle(cards)

player1 = []
player2 = []
player3 = []

#52/3 = 17 余 1
for _ in range (17):

#斗地主的发牌方式：按顺序去发，发了就删掉了
    player1.append(cards.pop())
    player2.append(cards.pop())
    player3.append(cards.pop())

player1.extend(cards)

print(f'第一个玩家收到的牌是{player1}')
print(f'第二个玩家收到的牌是{player2}')
print(f'第三个玩家收到的牌是{player3}')


4. 嵌套列表
list1 = []
list2 = [ list3, list4, list5 ]

'''
例题：保存5个学生3门课程的成绩
'''
import random

students = ['李白', '张飞', '关羽', '赵云', '马超']
courses = ['语文', '数学', '英语']

scores = [[random.randrange(60,101)for _ in range (3)]for _ in range (5)]
print(scores)

#for i, student in enumerate(students):
#    for j, course in enumerate(courses):
        
#        print(f'{student}的{course}成绩是{scores[i][j]}')

#查询每个学生的成绩平均值
#统计每门课的最高分和最低分

#for i, student in enumerate(students):
#    average = sum(scores[i]) / len(courses)
#    print(f'{student}三门课的平均成绩是{average:.1f}')

for j, course in enumerate(courses):
    temp = [scores[i][j] for i in range(len(students))]
    print(f'{course}的最高分是{max(temp)}')
    print(f'{course}的最低分是{min(temp)}')

【元组的使用】
1. 定义
是不可变的容器，1元组一定要打一个逗号，不然就只是一个字符串

2. 计算
#重复运算
fruits = ('apple', 'banana', 'grape', 'waxberry')
print(fruits * 3) 

#成员运算
print('apple' in fruits)
print('grape' not in fruits)

#合并运算:直接用加号
fruits2 = ('pitaya', 'litchi')
fruits3 = fruits1 +fruits2
print(fruits3)

#索引和切片
print(fruits[3])
fruits[4] = 'pingguo' × 不行，元组不能进行修改
print(fruitse[1:4:2] #隔一个取一个
print(fruits[::-1]) #反向切片，把所有的内容翻转过来，原理：从第一个到最后一个，倒着来

#不可以删除，不可以用del，不可以用append、pop、remove

#解包：too many values to unpack (expected 2)
a, b = 5, 10, 15

#解包：*x = 元祖里面剩下的数字都打包给这个值
a, b, *c = 5, 10, 15, 20, 25
print(c)


a, *b, c = 5, 10, 15, 20, 25
print(b)

或者b如果用不上的话，就把b变成_
a, *_, c = 5, 10, 15, 20, 25


"""
作业:一个列表中有很多重复元素，写一段代码去掉列表中的重复元素

思路：新建一个列表，如果元素在原本的列表里面，就加到新列表里
"""
items = [15, 12, 12, 15, 12, 35, 47, 45, 35, 12]
new_items = []

for item in items:
    if item not in new_items:
        new_items.append(item)
        
print(new_items)

"""
作业：有一个放整数的列表，找出列表中出现次数最多的元素。

思路：用counter算出数字出现了多少次，假设第一个是最多次的，遍历每一个元素，如果后面元素出现的次数大于第一个
则替换第一个成为最大的，最终输出max_counter

"""

nums = [10, 10, 1, 1, 10, 100, 100, 1, 10]   


item, max_counter = nums[0], nums.count(nums[0])

for num in nums[1:]:
    num_counter = nums.count(num)
    
    if num_counter > max_counter:
        item, max_counter = num, num_counter
        

print(item, max_counter) 

#如果有2个以上元素最多，且同样多：
#需要把item换成列表，而不是单纯的一个元素；且如果出现次数比原来的多，那就把原来的列表清空掉换成新的列表

nums = [10, 10, 1, 1, 10, 100, 100, 1, 10, 1]   

items, max_counter = [nums[0]], nums.count(nums[0])

for num in nums[1:]:
    num_counter = nums.count(num)
    
    if num_counter > max_counter:
        items.clear()
        items.append(num)
        max_counter = num_counter
    elif num_counter == max_counter:
        if num not in items:  
            items.append(num)
        
print(items)
        
    



























