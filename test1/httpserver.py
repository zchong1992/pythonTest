#coding:utf-8
from socket import *
import os

host = ''   #对应本机所有ip地址
port = 8899 #TCP socket端口
address = (host, port)
serverSocket = socket(AF_INET, SOCK_STREAM) #创建TCP socket
serverSocket.bind(address)  #绑定地址
serverSocket.listen(1)  #开始监听

while True:
    try:
        connectionSocket, clientAddr = serverSocket.accept()    #获取「连接套接字」
        message = connectionSocket.recv(1024)   #获得http报文
        print message
        filename = message.split()[1]   #获得URI，去掉首部'/'就是文件名
        #for a in filename:
        print "read file name :",filename[1:]
        f = open(filename[1:])

        outputdata = f.readlines()  #逐行读出文件内容并存到list中
        connectionSocket.send('HTTP/1.1 200 OK\r\n\r\n')    #发response行

 #       for line in range(0, len(outputdata)):
#            print outputdata[line]
        for i in range(0, len(outputdata)):
            connectionSocket.send(outputdata[i])   #把文件各行数据塞到response中
        connectionSocket.close()    #关闭数据连接
    except IOError:
        connectionSocket.send("404 not found")  #文件不存在时异常处理
        connectionSocket.close()
serverSocket.close()