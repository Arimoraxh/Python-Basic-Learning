# -*- coding: utf-8 -*-
"""
Created on Mon Feb 13 19:05:27 2023

@author: Mora

9.3 用SMTP发送邮件
协议：通信双方需要遵守的规范和标准
SMTP：simple mail transfer protocol，简单邮件传输协议
我们注册的邮箱一般都提供了SMTP服务，我们利用这个服务就可以用Python程序实现邮件发送。

"""

import smtplib
from email.mime.multipart import MIMEMultipart
from email.header import Header
from email.mime.text import MIMEText

email = MIMEMultipart()

sender = 'moraxiaohan@qq.com'
receivers = ['944820906@qq.com', '547058465@qq.com']


#修改标题
email['From'] = Header('小涵', 'utf-8')
email['To'] = Header('测试', 'utf-8')
email['Subject'] = Header('python邮件发送测试', 'utf-8')

#添加正文
content = """
    莫听穿林打叶声，何妨吟啸且徐行。
    竹杖芒鞋轻胜马，谁怕？一蓑烟雨任平生。
　　
    料峭春风吹酒醒，微冷，山头斜照却相迎。
    回首向来萧瑟处，归去，也无风雨也无晴。"""

#三个参数：第一个为文本内容，第二个 plain 设置文本格式，第三个 utf-8 设置编码
email.attach(MIMEText(content, 'plain', 'utf-8'))

#构造附件1
with open('D:/富途证券/表格/SEO数据看板2.xlsx', 'rb') as file:
    attachment1 = MIMEText(file.read(), 'base64', 'utf-8')
    attachment1['content-type'] = 'application/octet-stream'
    attachment1['content-disposition'] = 'attachment; filename="attachment1.xlsx"'

email.attach(attachment1)

#构造附件2
with open('D:/富途证券/表格/demo.docx', 'rb') as file:
    attachment2 = MIMEText(file.read(), 'base64', 'utf-8')
    attachment2['content-type'] = 'application/octet-stream'
    attachment2['content-disposition'] = 'attachment; filename="attachment2.docx"'

email.attach(attachment2)


#创造SMTP_SSL对象并连接邮件服务器
smtp_obj = smtplib.SMTP_SSL('smtp.qq.com', 465)
#通过用户名和授权码登录
smtp_obj.login('moraxiaohan@qq.com', 'csygcrzkrxqybcje')
#发送邮件
smtp_obj.sendmail(sender, receivers, email.as_string())

print('邮件发送成功')





















