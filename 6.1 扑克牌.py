# -*- coding: utf-8 -*-
"""
Created on Mon Dec  5 16:30:08 2022

@author: Mora
"""
'''
# -*- coding: utf-8 -*-

Created on Thu Dec  1 21:48:19 2022
列表学习

@author: Mora


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




























