#coding: utf-8
from socket import * #从onetnet上get数据要用的包
import time #延迟函数用到的包
import re
device_id = "45328136"  # 连接在onenet上的备Id
api_key = "CgAFQ3JAMsCHomt50lsH6=UcedQ="  # onetnet中对于不同的产品有不同的API_key
HOST = 'api.heclouds.com'  # onenet服务器的地址
PORT = 80  # 80端口，该端口是访问网站必须的端口，访问网站就是访问端口
BUFSIZ = 1024  # 每次从onenet服务器中读取的数据量
ADDR = (HOST, PORT)
#获取训练数据与验证数据
def get_inputdata():
    while True:
        data = ""
        data += ("GET /devices/" + device_id + "/datapoints HTTP/1.1\r\napi-key:" + api_key + "\r\nHost: " + HOST + "\r\n\r\n")
        Tcpclisocket = socket(AF_INET, SOCK_STREAM)
        Tcpclisocket.connect(ADDR)
        Tcpclisocket.send(data.encode())
        data1 = Tcpclisocket.recv(BUFSIZ).decode()
        heart_rate_obj = re.compile(r'.*?{"errno".*"value":(.*?)}].*?3303_0_5700.*?', re.S)
        heart_rate = re.search(heart_rate_obj, data1)
        print(heart_rate.groups()[0])
        lon_lat_obj = re.compile(r'.*?{"errno".*"value":"(.*?)"}].*?3336_0_5514.*?"value":"(.*?)"}].*?3336_0_5515.*?', re.S)
        lon_lat = re.search(lon_lat_obj, data1)
        print(lon_lat.groups())
        print(data1)
        time.sleep(2)
get_inputdata()
#print(input_data)
#print(len(input_data))
#print(output_data)
#print(len(output_data))