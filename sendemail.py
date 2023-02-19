# -*- coding: utf-8 -*-
"""
Created on Sun Feb 19 17:16:32 2023

@author: Mora

将发邮件封装成函数，并在 "9.4 归档压缩.py" 中调用
"""

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from urllib.parse import quote
import requests

HOST = 'smtp.qq.com'
PORT = 465
USER = '944820906@qq.com'
PASS = ''


def send_email(from_user, to_users, subject='', content='', filenames=[]):
    """发送邮件"""

    #从from_user发送到to_users，确定邮件主题
    email = MIMEMultipart()
    email['From'] = from_user
    email['To'] = ';'.join(to_users)
    email['Subject'] = subject

    #添加正文；MIMEText三个参数为(文本内容，文本格式，编码格式)
    message = MIMEText(content, 'plain', 'utf-8')
    email.attach(message)

    #构造附件：
    for filename in filenames:
        with open(filename, 'rb') as file:

           #找到给filename起名字的方法
           #如果有'/'就取'/'后面的字符穿，如果没有就取其文件本身
           position = filename.rfind('/')
           display_filename = filename[position + 1:] if position >= 0 else filename
           #display_filename = quote(display_filename)

           attachment = MIMEText(file.read(), 'base64', 'utf-8')
           attachment['content-type'] = 'application/octet-stream'
           attachment['content-disposition'] = f'attachment; filename="{display_filename}"'

    email.attach(attachment)

    #创造SMTP_SSL对象并连接邮件服务器,两个参数分别为(host port)，port=465是常用的端口名
    smtp_obj = smtplib.SMTP_SSL(HOST, PORT)
    #通过用户名和授权码登录
    smtp_obj.login(USER, PASS)
    #发送邮件
    smtp_obj.sendmail(from_user, to_users, email.as_string())

    print('邮件发送成功')
