# -*- coding: utf-8 -*-
"""
Created on Tue Dec  6 22:49:53 2022

@author: Mora

字符串的使用
"""

随时记住，str类型是不可变类型！！！

1. 转义符
把\后面的字符变成其他的含义

#如果想输出''或者""，要用转义符
a = '\'hello, world\''
print(a)

a = '\'hello, \tworld\''
print(a)

#如果想输出反斜杠\，要输入两个反斜杠\\
a = '\\time up \\now'
print(a)

#如果想读取电脑路径，用正斜杠/；或者在字符串前面加上一个r，表示“原始字符串”
a = r'c:\Users\Administrator\abc\hello.py'

#带占位符的字符串（格式化字符串）
e = f'文件路径:{a}'
print(e)

2. 美国标准信息标位置码：
# ASCII ---> GB2312 ---> BGK(国标码) ---> Unicode (URF-8)
s = '\u9a86\u660a' #unicode编码

3. 字符串的运算
3.1  重复运算
a = 'hello world'
print(a * 5)

print('or' in a) #成员运算：如果or在字符串里，就输出true，不在则输出false

#比较运算（比较字符串的内容，大写的字母在小写的字母前面）
print(a == b)
print(a != b)

b = 'hello, world'
c = 'goodbye , world'

print(b > c)

3.2 循环遍历字符串中的每个字符：
a = 'hello, world'
for i in range(len(a)):
    print(a[i])
    
a = 'hello, world'
for i in a:
    print(i)

3.3 字符串的拼接：
d = 'hello, everybody'
e = '!!!'
f = 'goodbye'
print(d + e + f)

3.4 is运算符


4. 字符串的索引和切片：
#跑马灯文字效果：滚动文字播放
#思路：前后空格，每一次取第2个字符+后面所有的，再把第一个字符加回来；永久循环；每一次隔一段时间，不然会看不清
#怎么只输出一行呢？operating system，清楚屏幕输出的命令

import time

content = '拼搏到无能为力，坚持到感动自己'
while True:
    print(content)
    time.sleep(0.3)#休眠，让程序暂停
    content = content[1:] + content[0]

5. 字符串的操作（字符串的方法）
a = 'hello,world'
a.________

5.1 改变大小写

a = 'hello,world'

print(a.upper()) #所有的字母都大写
print(a.lower()) #所有的字母都小写
print(a.capitalize()) #仅第一个字母大写
print(a.title()) #每一个单词的第一个字母大写

5.2 性质判断

b = 'abc123'
print(b.isdigit()) #判断是不是由数字构成的
print(b.isalpha()) #判断是不是字母构成的
print(b.isalnum()) #判断是不是数字和字母构成的
print(b.isascii()) #判断是不是ASCII码字符构成的

c = '你好呀'
print(c.startswith('你')) #判断字符串是否以指定内容开头
print(c.endswith('啊')) #判断字符串是否以指定内容结尾

5.3 查找有没有某个子串
- index / rindex
- find / rfind

a = 'Oh apple, i love apple.'

#index：从左往右找置顶的子串，可以指定从哪里开始找，默认是0；找到了返回对应的索引（下标），找不到则程序崩溃
# substring:在...下面
# supstrint:在...上面

print(a.index('apple'))   
print(a.index('apple', 10))
print(a.rindex('apple')) 

#find:找不到程序不会崩溃
print(a.find('banana')) #返回-1

6. 排版&格式化输出
#居中，总共80个字符，左右有80个~
a = 'hello, world'
print(a.center(80,'~'))
#右对齐，左边80个字符，有80个~
print(a.rjust(80,'~'))
#左对齐，右边80个字符，有80个~
print(a.ljust(80,'~'))

#总共6个字符，在左边填充0
b = '123'
print(b.zfill(6))

c = 1234
d = 345
#以下三种写法结果是一样的
print('%d + %d = %d' % (c, d, c + d))
print(f'{c} + {d} = {c + d}')
print('{} + {} = {}'. format(c, d, c + d))


7. 字符串的修剪
strip() #去掉左右两边的空格,中间的空格不会去掉
email = ' xiaohanma@futunn.com   '
tel = '    1882384 7560   '

print(email.strip())
print(tel.strip())
print(email.lstrip())
print(email.rstrip())

#字符串替换成新的内容
content = '   扎扎是个大坏蛋   '
print(content.replace('扎扎', '*'))

#以下这种方式可以把空格去掉
print(content.strip().replace('扎扎','*').replace('大坏蛋','*'))

8. 字符串的拆分和合并
#split---> 把字符串拆分成列表
#join--->把列表合并成字符串

content = 'You go your way, I will go mine.'
content = content.replace(',','').replace('.','')
print(content)

#split：默认以空格拆开字符串，拿到的是一个列表
content = 'You go your way, I will go mine.'
print(content.split())

words = content.split()
for word in words:
    print(word)

#以逗号分割，会把前后拆分成为两部分
content3 = content.split(',')
for content in content3:
    print(content)
    print(content3)

#maxsplit：指定最大拆分次数
content = 'You go your way, I will go mine.'
words = content.split(' ', maxsplit = 3 )
print(words)

#rsplit:从右向左拆分，做多允许拆分3次
content = 'You go your way, I will go mine.'
words = content.rsplit(' ', maxsplit = 3 )
print(words)

#join：合并列表
contents = [
    '请不要相信我的美丽'
    '更不要相信我的爱情'
    '因为在涂满油彩的面孔下'
    '有着一颗戏子的心'
    ]

#将列表中的元素用指定的字符串连接
print(' '.join(contents))

9. 字符串的编码和解码，P57，实在是没听下去

#编码：把字符串转换成另外一种字符集,
#str(字符串)---> encode(字符集)---> bytes(字节串)

#解码：

a = '我爱你中国'
b = a.encode('gbk')
print(b) #b'\xce\xd2\xb0\xae\xc4\xe3\xd6\xd0\xb9\xfa'，一个中文对应两个字节
print(type(b)) #<class 'bytes'>

c = b'\xce\xd2\xb0\xae\xc4\xe3\xd6\xd0\xb9\xfa'
print(c.decode('gbk'))  #你要告诉程序，按哪一种字符集进行编码

#如果编码和解码的方式不一致，py可能会产生UnicodeDecode异常，也有可能出现乱码

#作业：了解“百分号编码”、“BASE64编码”和它们的应用场景

9.1 凯撒密码：通过对应字符的替换，实现对明文进行加密的一种方式

'''
abcdefghijklmnopqrstuvwxyz
defghijklmnopqrstuvwxyzabc

明文：attack at dawn.
密文：dwwdfn dw gdzq.

对称加密：加密和解密使用了相同的密银。--->AES
非对称加密：加密和解密使用了不同的密银（公钥、私钥）---> RSA --->适合互联网应用。
'''

#使用translate方法实现转译

message = 'attack at dawn.'
table = str.maketrans('abcdefghijklmnopqrstuvwxyz','defghijklmnopqrstuvwxyzabc')
message.translate(table)
print(message.translate(table))




















