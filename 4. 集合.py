# -*- coding: utf-8 -*-
"""
Created on Wed Dec 21 21:57:26 2022

@author: Mora

集合（set)
"""

'''
1. 集合的特性：无序性、互异性、确定性
什么意思呢？

1.1 无序性：没有set[0],不能够做下标运算，set is not subscriptable.
1.2 互异性：
set1 = {1, 1, 2, 3, 1, 1, 2}
print(set1)

{1, 2, 3}  #out

1.3 确定性


2. 定义集合
set1 = {1, 1, 2, 3, 1, 1, 2}
set2 = {}
空 集合就是字典
列表：list = [1, 1, 2, 3, 1, 1, 2]
元组：anple = (1, 1, 2, 3, 1, 1, 2)

'''

#遍历集合中的元素：
set1 = {1, 1, 2, 3, 1, 1, 2}
for elem in set1:
    print(elem)
    

'''
3. 集合的运算
3.1 成员的运算
注意：集合的成员运算在效率上是远远高于列表的成员运算的
'''

set1 = {1, 1, 2, 3, 1, 1, 2}
set2 = {2, 4, 6, 8}
print(1 in set1)
print(1 not in set1)

#交集:   &
print(set1 & set2)
print(set1.intersection(set2)) #out:{2}

#并集：|
print(set1 | set2)
print(set1.union(set2)) #out:{1, 2, 3, 4, 6, 8}

#差集：取在2里面的，但不在1里面的
print(set1 - set2)
print(set1.difference(set2)) #out:{1, 3}
print(set2 - set1) #out:{8, 4, 6}

#对称差：取1+2，删掉1交2
print(set1 ^ set2)
print((set1 | set2) - (set1 & set2))
print(set1.symmetric_difference(set2)) #out:{1, 3, 4, 6, 8}


'''
4. 集合的操作方法
集合里面不能放列表，可以放字符串、布尔值
集合底层采用了一种高效率的存储方式，即 “哈希存储/散列存储”
哈希码只是一个地址，只是根据哈希码判断这个位置的元素在不在，如果不在就是没有？？
是一种常量级时间复杂度的存储方案

如果一个无法计算哈希码，就不能放到集合中，比如列表、集合、字典。
可变容器不可以计算哈希码，都不能放到集合中作为集合的元素。
百度云盘的极速秒传用的就是哈希码，在百度已经有了存储，只是生成一条记录，标记你也有了

哈希冲突：

列表是“顺序存储”，元素是挨着一个的，
优点：可以随机访问，想访问第多少个就看第多少个；
缺点：查找和判断元素在不在元器中，效率非常低下

'''
#添加元素
set1 = {'apple', 'banana', 'pitaya', 'apple'}

set1.add('grape')
print(set1) 

#删除元素,随机删除
print(set1.pop())

#清空元素
print(set1.clear())

#指定元素删除
print(set1.discard('banana'))


'''
forzenset{}是一种不可变容器
'''

'''
如果想把一个列表进行去重，扔进集合构造器里面就可以
'''

nums = [1, 1, 10, 10, 10, 5, 3, 9, 9]
set2 = set(nums)
print(set2)
list3 = list(set2)
print(list3)














