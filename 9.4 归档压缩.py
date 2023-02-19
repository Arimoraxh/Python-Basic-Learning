# -*- coding: utf-8 -*-
"""
Created on Tue Feb 14 22:15:28 2023

@author: Mora

任务：从网站上下载美女图片，归档压缩后发送到指定邮箱中

MIME - Multi-purpose Internet Mail Extension - 多用途Internet拓展
MIMEMultipart：多个部分

"""
import os
import requests
import shutil
from sendemail import send_email

#定义一个下载图片的函数，下载到的路径为path，下载的网页为url
def download_picture(path, url):

    #原url为https:\/\/p0.ssl.qhimgs1.com\/t01e86ce6da26b00d3e.jpg，截取/后面的字符
    filename = url[url.rfind('/') + 1:]
    response = requests.get(url)

    #构造文件，文件名称为url名
    with open(f'{path}{filename}', 'wb') as file:
        file.write(response.content)


def main():
    
    #如果不存在路径，在系统目录中创建一个
    if not os.path.exists('D:/富途证券/表格/美女图片'):
        os.makedirs('D:/富途证券/表格/美女图片')
        
    #通过网站的接口获取JSON数据，遍历下载url并储存
    resp = requests.get('https://image.so.com/zjl?sn=0&ch=beauty&sn=30')
    beauty_list = resp.json()['list']
    for beauty in beauty_list:
        picture_url = beauty['qhimg_url']
        download_picture('D:/富途证券/表格/美女图片/', picture_url)
    
    #进行文件压缩归档，参数为(basename, format, root_dir, base_dir)
    #其中，root_dir是指输出文件的基本目录，base_dir是指想要打包的文件
    shutil.make_archive('beauties', 'zip', 'D:/富途证券/表格/美女图片' )
    send_email(
        from_user='944820906@qq.com',
        to_users=['moraxiaohan@outlook.com','547058465@qq.com']
        subject='福利资源分享',
        content='下载的内容在附件中，请查收！',
        filenames=['beauties.zip']
        )
if __name__ == '__main__':
    main()
    


'''
补充知识：使用shutil模块（封装了高级的文件操作函数）
例如：

1. 获取命令的路径：
print(shutil.which('pl'))
[Out]: D:\Anaconda\python.EXE

2. 移动文件
shutil.move('resource/sales_data.csv', 'sale.csv')

'''















