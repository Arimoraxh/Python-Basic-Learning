# -*- coding: utf-8 -*-
"""
Created on Sat Feb 25 14:52:30 2023

@author: Mora

10. 正则表达式(regular expression)
【用法】编写处理字符串的程序和网页时，用于查找符合某些复杂规则的字符串。
【定义】记录文本规则的代码
【通配符(wildcard)】：*和?。如果想查找word文档，会搜索*.doc。，*会被解释为任意的字符串。
【例子】所有以0开头，后面跟着2-3个数字，然后是一连字号“-”，最后是7或8位数字的字符串(010-12345678)

Python使用正则表达式的两种方式：
~ 不创建正则表达式对象，直接调用函数进行匹配操作
    - match
    - fullmatch
~ 创建正则表达式对象（Pattern），直接调用 函数进行匹配操作
    - compile
    
字符集--->[]--->[a-zA-Z0-9_]{6,20}
"""

'''
例子:网站注册用户名要求必须是字母、数字、下划线，长度在6到20个字符之间
检查用户名是否合法应该怎么做
'''

import re

#验证用户名的合法性 
username = input('请输入用户名:')
matcher = re.match(r'^\w{6,20}$', username)
if matcher is None:
    print('用户名不合法！！')
else:
    print(matcher)
    print(matcher.group())
    

#验证QQ号码的合法性,必须是4位数以上的数字
qq = input('请输入QQ号：')
matcher = re.fullmatch(r'[1-9]\d{4,}', qq)
if matcher is None:
    print('QQ号不合法！！')
else:
    print(matcher.group())


#匹配手机号，必须是1开头，第二位为3-9的数字，总共11位
tel = input('请输入手机号：')
matcher = re.fullmatch(r'1[3-9]\d{9}', tel)
if matcher is None:
    print('手机号不合法！！')
else:
    print(matcher.group())
    

#用创建正则表达式对象的方式，当正则表达式会被反复使用的时候，最好是用这种方式
username = input('请输入用户名:')
username_pattern = re.compile(r'^\w{6,20}$')
print(type(username_pattern))   #<class 're.Pattern'>

#通过给pattern发消息实现匹配检查
matcher = username_pattern.match(username)
print(type(matcher))            #<class 're.Match'>

if matcher is None:
    print('用户名不合法！！')
else:
    print(matcher.group())

'''
————————————————————————————————————————————————————
match - 匹配 - 从头匹配
search - 搜索 - 从任意位置匹配
要求:检查以下这一段话有么有手机号
'''

content = """报警电话：110，我们班是15班，
我的QQ号是957658，我的手机号是13811223344，谢谢！"""

matcher = re.search(r'1[3-9]\d{9}', content)
if matcher is None:
    print('没有找到手机号')
else: 
    print(matcher.group())

#把所有的数字提取出来怎么做? 
#第一种做法，循环
pattern = re.compile(r'\d+')
matcher = pattern.search(content)
while matcher:
    print(matcher.group())  
    matcher = pattern.search(content, matcher.end()) #最新的一次匹配是从上一次匹配结果的字符串开始的

#第二种做法：findall
results = pattern.findall(content)
for result in results:
    print(result)

'''
————————————————————————————————————————————————————
联系：从网页上面获取新闻的标题和链接

'''

#捕获全部的字符，子表达式出现至少1次，且非贪婪
import requests

pattern1 = re.compile(r'href="http.+?"')
resp = requests.get('https://www.sohu.com/')
content = resp.text
matcher = pattern1.search(content)
while matcher:
    print(matcher.group()[6:-1])
    matcher = pattern1.search(content, matcher.end())


pattern2 = re.compile(r'title=".+?"')
titles_list = pattern2.findall(content)
for title in titles_list:
    print(title[7:-1])
    
#问题来了，标题和url两个是分开的，根本没有拼到一起。
#匹配整个a标签，但是只捕获()中的内容--->正则表达式的捕获组

pattern1 = re.compile(r'<a\s.*?href="(.+?)".*?title="(.+?)".*?>')
resp = requests.get('https://www.sohu.com/')
content = resp.text
print(pattern.findall(resp.text))
#for href, title in results:
#    print(title, href)

'''
———————————————————————————————————————————————————
内容的查找和替换
案例：不良内容过滤
re.sub(要替换的内容，替换后的内容，字符串，替换的次数，标志)
'''
import re
content = '马化腾是个沙雕，Fuck you!'
modified_content = re.sub(r'[傻沙煞][逼笔比鄙]|马化腾|fuck|shit','*',content,flags=re.I)
print(modified_content)



'''
———————————————————————————————————————————————————
用正则表达式拆分字符串
re.split(pattern, string, maxsplit=0, flags=0)
'''
import re
poem = '床前明月光，疑是地上霜，举头望明月，低头思故乡。'
sentences_list = re.split(r'[，|。]', poem)
sentences_list = [sentence for sentence in sentences_list if sentence]
print(sentences_list)
for sentence in sentences_list:
    print(sentence)














