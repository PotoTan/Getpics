#coding=utf-8

import os #建立本地目录使用
import time #写了一个1秒延时
import socket

a = 1 #起始章节
b = 1 #起始页面
c = 271 #定义总章节，当大于此章节循环跳出
errorcode = 200 #先定义正常代码
socket.setdefaulttimeout(12) #设置默认超时时间s

#定义下载方法方便调用
def picdownld():
    os.makedirs(folder, exist_ok=True)
    from urllib.request import urlretrieve
    try:
        urlretrieve(IMAGE_URL, picname)  #如果超时将进行两次循环，均失败则程序结束
    except socket.timeout:
        count = 1
        while count < 3:
            try:
                print(str(count) + 'Reloading')
                urlretrieve(IMAGE_URL, picname)
                break
            except socket.timeout:               
                print(str(count) + 'Reload fail')
                count += 1
        if count == 3:
            print('download fail, pls try again')

while b < 100:

    #定义下载地址
    IMAGE_URL_HEAD = "http://img.2animx.com/upload/img/1w/90b/19033/"
    IMAGE_URL_MID = str(a)
    PIC_URL_END = "/"+ str(b) +".jpg"
    IMAGE_URL = IMAGE_URL_HEAD + IMAGE_URL_MID + PIC_URL_END
	
    #定义本地电脑保存目录
    folder = './pics/' + str(a) + '/'
    pictitle = str(b) + '.jpg'
    picname = folder + pictitle
    
    #判断下载地址是否有效
    from urllib import request
    from urllib import error
    req = request.Request(IMAGE_URL)
    try:
        responese = request.urlopen(req)
    except error.HTTPError as e:
        errorcode = e.code
    if errorcode == 404: #如果地址无效跳下一章节，有效就进行下载    
        errorcode = 200 #只会返回错误的情况，所以必须重置返回值
        a = a + 1
        if a > c:
            break
        b = 1
        IMAGE_URL_MID = str(a)
        PIC_URL_END = "/"+ str(b) +".jpg"
        IMAGE_URL = IMAGE_URL_HEAD + IMAGE_URL_MID + PIC_URL_END
        folder = './pics/' + str(a) + '/'
        pictitle = str(b) + '.jpg'
        picname = folder + pictitle  
        req = request.Request(IMAGE_URL)
        try:
            responese = request.urlopen(req)
        except error.HTTPError as e:
            errorcode = e.code
        if errorcode == 404: #如果再次404跳下一章节继续判断
            errorcode = 200 #只会返回错误的情况，所以必须重置返回值
            a = a + 1
            continue
    picdownld() #调用下载方法
    b = b + 1   #图片+1
    print(IMAGE_URL + '下载完成')
    time.sleep(1)
print('All done，一切安好')