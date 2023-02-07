# -*- coding: utf-8 -*-
'''
Created on Wed Dec 21 23:07:25 2022

@author: Mora
字典

'''

'''
当有一个对象，他有非常多复杂的属性数据需要去存储，就引入了字典的概念。

字典 --->元素由键和值两部分构成，冒号前面的称为键，冒号后面的称为值，合在一起为键值对。

dictionatry = {'key':value}
print(dictionary['key'])

冒号前面的key一定是不可变数据类型，字典底层也是哈希存储，

'''

student = {
    'id':1001,
    'name':'xiaohanma',
    'sex':True,
    'weight':190,
    'birthday':'1997-09',
    'favorites':['弹琴','唱歌','编程'],
    'contacts':{
        'QQ':'944820906',
        'tel':'188238475690',
        'email':'xiaohanma@futunn.com'
        }
    }

print(student['name'])
print(student['favorites'])
for fav in student['favorites']:
    print(fav)
print(student['contacts']['tel'])

'''
1. 字典的创建和使用
1.1 字典的字面量语法
1.2 构造器函数语法

'''
student2 = dict(id=1002, name='王大锤',sex=True, birthday='1990-1-1')
print(student2)

'''
1.3 生成式（推导式语法
'''

list1 = [i for i in range(1, 10)]
set1 = {i for i in range(1, 10)}
dic = {i: i**2 for i in range(1, 10)}

print(list1)
print(set1)
print(dic)

'''
1.4 生成器
长得很像元组，但是不是元组的生成器哦！！！

'''

gen_obj = (i for i in range(1, 10))
print(next(gen_obj)) #只有输出的时候才产生对应的数字
print(next(gen_obj))
print(next(gen_obj))

'''
2. 遍历字典当中的所有元素

'''
#2.1 只遍历键：

student = {
    'id':1001,
    'name':'xiaohanma',
    'sex':True,
    'weight':190,
    'birthday':'1997-09',
    'favorites':['弹琴','唱歌','编程'],
    'contacts':{
        'QQ':'944820906',
        'tel':'188238475690',
        'email':'xiaohanma@futunn.com'
        }
    }

for x in student:
    print(x)


#2.2 想取所有值：

for x in student:
    print(x,student[x])
    
#2.3 取所有的值:   dic.values()

for value in student.values():
    print(value)    

#2.4 遍历键值对:   dic.items()
print('-' * 20)
for key, value in student.items():
    print(key, value)
print('-' * 20)


'''
3. 字典的运算

'''

student2 = dict(id=1002, name='王大锤',sex=True, birthday='1990-1-1')
print(student2)

print('name' in student2)  #true
print('age' in student2)   #false
print('address' in student2)  #false

#3.1 赋值
#字典的索引运算放在赋值运算符的左边
#如果索引对应的键是存在的，就更新它的值
#如果字典中没有对应的索引，就增加一组新的“键值对”

student2['name'] = '王美丽'
student2['sex'] = False
student2['address'] = '四川成都'
print(student2)
#out：{'id': 1002, 'name': '王美丽', 'sex': False, 'birthday': '1990-1-1', 'address': '四川成都'}


#3.2 添加元素
#使用get函数通过key获取value时，如果key不存在，不会发生keyerror错误，而是得到一个none（空值）
#get('key',x)：如果key值是有的，返回key的值；如果key没有值，则加上这个key并返回新增的值x
student2 = dict(id = 1002, name = '王大锤',sex = True, birthday = '1990-1-1')
print(student.get('age'))
print(student.get('age', 20)) #out:20
print(student.get('name', '无名氏')) #out:xiaohanma

#3.3 删除元素：del
del student['name']
print(student.get('name', '无名氏')) #out:无名氏

#删除元素2：
print(student.pop('name')) 

dict


'''
4. 更新值（合并）
dict.update(dict2):dict1当中没有的加到dict里面，有的更新dict1原本的东西
'''
dict1 = {'A':100, 'B':200, 'C':300}
dict2 = {'D':400, 'E':500, 'A':600}

dict1.update(dict2)

print(dict1) #out:{'A': 600, 'B': 200, 'C': 300, 'D': 400, 'E': 500}

#删除，键必须存在，如果不存在会产生KeyError
#dict1.pop('k')
#print(dict1) #out:KeyError: 'k'

#setdefault:更新键值对，或者在字典中存入新的键值对
#如果已经有键，返回它原本的值；如果没有键，存入新的键值对，且新的值默认是none
dict1.setdefault('C',800)
dict1.setdefault('K',10000)
print(dict1)

'''
字典的应用
输入一段话，统计每个英文字母出现的字数
'''
import string

results = {letter : 0 for letter in string.ascii_lowercase}
#print(results)

sentence = input('请输入一段话').lower()
for al in sentence:
    if al in results:
        results[al] += 1
#print(results) 

for key, value in results.items():
    print(f'{key}:出现过{value}次')

'''
字典中保存股票的信息，完成下面的操作
1. 找出股票价格大于100元的股票并创建一个新的字典
2. 找出价格最高和最低的股票对应的股票代码
3. 按照股票价格从高到低给股票代码排序

'''
stocks = {
    'AAPL': 191.88,
    'GOOG': 1186.96,
    'IBM': 149.24,
    'ORGL': 48.44,
    'ACN': 166.89,
    'FB': 208.09,
    'SYMC':21.29,
    }

stocks1 = {}
for key in stocks:
    if stocks[key] > 100:
        stocks1[key] = stocks[key] 
#这里代表了stocks的键值对都可以直接赋给stocks1
        
print(stocks1)

#生成式语法：遍历键值对，只要值符合条件，就加入到新的字典中
stocks1 = {key: value for key,value in stocks.items() if value > 100}
print(stocks1)

#py的zip函数：zip() 函数用于将可迭代的对象作为参数，将对象中对应的元素打包成一个个元组，然后返回由这些元组组成的列表。
#例子：
a = [1, 2, 3]
b = [4, 5, 6]
zipped = zip(a, b)
print(list(zipped))

#zip用在字典中：用dict把zip的结果变成字典，在前面的就是key，后面的就是value
dict1 = dict(zip('ABCED',[1, 2, 3, 4, 5]))
dict2 = dict(A = 1, B = 2, C = 3, D = 4, E = 5)
print(dict1) #{'A': 1, 'B': 2, 'C': 3, 'E': 4, 'D': 5}
print(dict2) #{'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5}

#怎么把字典的key变成value，value变成key？
dict1 = {'A':1, 'B':2, 'C':3, 'D':4}
dict2 = dict(zip(dict1.values(), dict1.keys()))
print(dict2)

#再回到原题目：解题思路为：

stocks = {
    'AAPL': 191.88,
    'GOOG': 1186.96,
    'IBM': 149.24,
    'ORGL': 48.44,
    'ACN': 166.89,
    'FB': 208.09,
    'SYMC':21.29,
    }

#直接搜max，搜的是key首字母在二进制上的max，字母表的顺序是A最小，Z最大
print(max(stocks))
print(max(zip(stocks.values(), stocks.keys())))
#out:(1186.96, 'GOOG')
#最终想输出的是goog，而不是key，所以索引zip元组的第2个值
print(max(zip(stocks.values(), stocks.keys()))[1])
print(min(zip(stocks.values(), stocks.keys()))[1])

'''
#py max的使用是非常丰富的，例如max(dict, key=...)，key可以自己去定义
words = ['apple', 'zoo', 'watermelon', 'zealon', 'internationalization', 'pear']
print(max(words, key=len))
#out:internationalization

words.sort(key=len)
print(words)
#out:['zoo', 'pear', 'apple', 'zealon', 'watermelon', 'internationalization']
'''

#找出stocks中最大的值，通过stocks.get取值
max(stocks, key = stocks.get)
#out:'GOOG'


'''
JSON格式的字符串

操作系统：Windows、iOS、Android、macOS、Linus、Unix
程序语言：Python、Java、PHP、GO、C++

1. 两个异构的系统之间交换数据最好是交换纯文本（可以屏蔽系统和编程语言的差异）
2. 纯文本应该是结构化或半结构化的纯文本（有一定的格式的意思） (数据格式)
    ~ XML ---> eXtensivle Markup Language --->可拓展标记语言
    ~ JSON ---> JavaScript Object Notation ---> 大多数网站和数据接口服务使用的数据格式
    ~ YAML ---> Yet Another Markup Language

3. 如何将JSON格式转成Python程序中的字典？
    使用 json 模块 ---> loads 函数
    
    import json

    dict = json.loads(data)
    
4. URL: Universal Resource Locator ---> 统一资源定位符

'''
import json
data = """{
  "code": 200,
  "msg": "success",
  "newslist": [
    {
      "id": "d5f8d4298e341732a880053e3ccf594e",
      "ctime": "2022-12-24 00:00",
      "title": "警惕老人沉默性缺氧！家有老人面对新冠要知道的事",
      "description": "",
      "source": "中华国内",
     "picUrl": "https://img1.utuku.imgcdc.com/300x200/news/20221224/a77c641b-fb28-498e-b40e-a68382620518.png",
      "url": "https://news.china.com/domestic/945/20221224/44163714.html"
    },
    {
      "id": "804e8b6c97283104505cc07504c60887",
      "ctime": "2022-12-24 00:00",
      "title": "全球首架C919于26日开启100小时验证飞行之旅",
      "description": "",
      "source": "中华国内",
      "picUrl": "https://img0.utuku.imgcdc.com/300x200/news/20221224/11018b18-8436-49d2-89f1-2697baaaa544.png",
      "url": "https://news.china.com/domestic/945/20221224/44163723.html"
    },
    {
      "id": "1f9ed13367d7741ee678bc2965874b23",
      "ctime": "2022-12-23 00:00",
      "title": "海南酒店企业提供“抗阳”服务，名单来了",
      "description": "",
      "source": "中华国内",
      "picUrl": "https://img0.utuku.imgcdc.com/300x200/news/20221223/bdb42b29-1f81-4d9f-9a67-76b940397490.png",
      "url": "https://news.china.com/domestic/945/20221223/44162334.html"
    },
    {
      "id": "c5266a759890af934e37cb93e5590add",
      "ctime": "2022-12-23 00:00",
      "title": "俄方未就普京与拜登会谈安排与美方接触",
      "description": "",
      "source": "中华国内",
      "picUrl": "https://img2.utuku.imgcdc.com/300x200/news/20221223/9e11aff0-fec0-46c8-b94d-f11549751466.png",
      "url": "https://news.china.com/domestic/945/20221223/44162261.html"
    },
    {
      "id": "c7c44a1e2309a17d4c563584aa97db3c",
      "ctime": "2022-12-23 00:00",
      "title": "商务部：将适时推动优化对入境人员的服务保障措施",
      "description": "",
      "source": "中华国内",
      "picUrl": "https://img0.utuku.imgcdc.com/300x200/news/20221223/29ccf650-55fa-4daa-8c44-bb5ad6c31f0c.png",
      "url": "https://news.china.com/domestic/945/20221223/44161996.html"
    },
    {
      "id": "05139ced7050115714aeed1c7fb9d8c1",
      "ctime": "2022-12-23 00:00",
      "title": "北京公积金自助机年底实现全覆盖",
      "description": "",
      "source": "中华国内",
      "picUrl": "https://img3.utuku.imgcdc.com/300x200/news/20221223/52e7c7a6-a59f-4ec0-8769-a4f133ef0133.png",
      "url": "https://news.china.com/domestic/945/20221223/44162033.html"
    },
    {
      "id": "fdbcf806910ea7ef773e610fc5964841",
      "ctime": "2022-12-23 00:00",
      "title": "外交部：美方干涉中国内政，必将受到中方坚决反制",
      "description": "",
      "source": "中华国内",
      "picUrl": "https://img3.utuku.imgcdc.com/300x200/news/20221223/b6754e66-ac52-44fe-9e07-79ad2e67b515.png",
      "url": "https://news.china.com/domestic/945/20221223/44162042.html"
    },
    {
      "id": "21113bb21a4bbf1fd063d89385def3c6",
      "ctime": "2022-12-23 00:00",
      "title": "国家药监局已批准46个新冠病毒抗原检测试剂",
      "description": "",
      "source": "中华国内",
      "picUrl": "https://img1.utuku.imgcdc.com/300x200/news/20221223/91163e7a-7d12-4e51-b4a6-738dd648c83a.png",
      "url": "https://news.china.com/domestic/945/20221223/44162136.html"
    },
    {
      "id": "f41069adffdb2d87d64f2f4a5fec870a",
      "ctime": "2022-12-23 00:00",
      "title": "2023年铁路春运火车票12月24日开售",
      "description": "",
      "source": "中华国内",
      "picUrl": "https://img3.utuku.imgcdc.com/300x200/news/20221223/647ea907-e2f8-422a-9b9c-e26e9cb4e2b8.jpg",
      "url": "https://news.china.com/domestic/945/20221223/44160040.html"
    },
    {
      "id": "aff15672b1b20cbc4ac11822007df591",
      "ctime": "2022-12-23 00:00",
      "title": "旅日大熊猫“香香”计划于2023年2月21日回国",
      "description": "",
      "source": "中华国内",
      "picUrl": "https://img3.utuku.imgcdc.com/300x200/news/20221223/e3acc50a-0057-40eb-a76a-9ac80190e11f.png",
      "url": "https://news.china.com/domestic/945/20221223/44160281.html"
    }
  ]
  }
}"""

#loads函数可以将JSON格式的函数转成python中的字典

dict = json.loads(data)
news_list = dict['newslist']
for news in news_list:
    print(news)

'''
联网获取JSON格式的数据并解析出需要的内容
python Interpreter

修改下载三方库的下载来源为国内的镜像网站 ---> pip config set global.index-url http://pypi.doubanio.com/simple
三方库 ---> requests ---> pip install requests

协议 ---> 通信双方需要遵守的会话的规则。
HTTP / HTTPS ---> 通过URL访问网络资源的协议 ---> Hyper-Text Transfer Protocol(超文本传输协议)

请求(request) - 响应(response)

需要有一个虚拟环境？

'''

import requests
#第一种写法 key:参数名，等号后面为参数值
requests.get('http....?key=xxxxxx')


#第二种写法，params为参数，是一个字典，num表示要取20条数据
requests.get(
    url='http...',
    params={'key': 'xxxx', 'num': 20} 
)

#将服务器给我返回的字符串储存起来
resp = requests.get(
    url='http...',
    params={'key': 'xxxx', 'num': 20} 
)

print(resp.text) #生成JSON格式的文本
json.loads(resp.text)
news_dict = json.loads(resp.text)

#好的，实际使用一下
import json

import requests

resp = requests.get(
    url='https://apis.tianapi.com/guonei/index',
    params={'key':'de14c9c28853c32fa5cbcb3f1738cfa3','num':10}
    )
news_dict = json.loads(resp.text)
result = dict(news_dict['result'])
news_list = result['newslist']
#print(news_list)
for news in news_list:
    print(news['title'])
    print(news['url'])

'''
CRAPS赌博游戏：色子游戏
玩家摇两颗色子，如果第一次要出了7点或11点，玩家胜；如果摇出了2点、3点、12点，庄家胜；
如果摇出了其他的点数，游戏继续，玩家重新摇色子；如果玩家摇出了第一次摇的点数，玩家胜；
如果玩家摇出了7点，庄家胜；如果玩家摇出了其他点数，游戏继续，玩家重新摇色子，直到分出胜负。

游戏开始之前，玩家有1000元的初始资金，玩家可以下注，赢了获得下注的金额，输了就扣除下注的金额。
游戏结束的条件是玩家把钱输光。
'''

import random

money = 1000
while money > 0: #玩家的初始资金是1000，还没输光前都要一直循环
    
    bet_money = int(input('下注多少钱'))
    
    result1 = random.randrange(1, 7) + random.randrange(1, 7)
    print(f'摇出了{result1}点')
    
    if result1 in (7, 11):
        print('玩家胜！')
        money += bet_money
        
    elif result1 in (2, 3, 12):
        print('庄家胜！')
        money -= bet_money
        
    else:
        while True: #我不知道循环次数，但是不知道条件，所以在适当的时候用break
        
            results = random.randrange(1, 7) + random.randrange(1, 7)
            print(f'摇出了{results}点')
            if results == result1 :
                print('玩家胜！')
                money += bet_money
                break
            
            elif results == 7:
                print('庄家胜！')
                money -= bet_money
                break
            else:
                pass
print('玩家破产，游戏结束')


'''
练习：双色球随机选号（实现机选N注）

红色球01-33，选择不重复的6个球，按从小到大排列
蓝色球01-16，选择一个球，跟在红色球的后面

解题思路：
①用生成式语法创建两个随机的容器，每一个容器写上蓝色还是红色，
②红色的处理：每选择一个删掉一个，排列
③蓝色的处理：新建一个新的容器，选第一个加在红色后面
'''
import random

n = int(input('机选几注：'))
for _ in range(n):
    
    red_balls = [i for i in range(1, 34)]
    blue_balls = [i for i in range(1, 17)]
    selected_balls = random.sample(red_balls, 6)
    #sample：返回从总体序列或集合中选择的唯一元素的k长度列表。 用于无重复的随机抽样。
    
    selected_balls.sort()
    #sort：将列表中的元素进行从小到大的排列
    
    selected_balls += random.choices(blue_balls, k=1)
    #selected_balls.extend(random.choices(blue_balls, k=1))
    #choice：从非空序列seq返回一个随机元素。 如果 seq 为空，则引发 IndexError。
    for ball in selected_balls:    
        print(f'{ball:0>2d}', end=' ')


'''
输入一个英文的句子，统计每个单词出现的次数
'''
























