#-*- coding = utf-8 -*- 
from bs4 import BeautifulSoup
import re 
import urllib.request,urllib.error
import pandas.io.excel._xlwt
import xlwt
from io import BytesIO
import gzip


def main():
    baseurl = "https://www.bilibili.com/video/BV1db4y1Q71W"
    #1、爬取网页
    datalist = GetData(baseurl)
    #3、保存数据
    savepath=".\\豆瓣电影Top250.xls"                      #.\\表示文件目录；./表示当前文件夹
    #SaveData(datalist,savepath)


#制定用于获取对应消息的正则表达式
findUsername = re.compile(r'class="name ">(.*)</a>')        #获取主评论人的站好名称                
findComment = re.compile(r'<p class="text">(.*) </p> ')     #获取主评论
findTime = re.compile(r'<span class="time">(.*)</span>')    #获取评论时间
findLikes = re.compile(r'<span class="like"><i></i><span>(.*)</span>')    #获取点赞数
##findHate = re.compile(r'<span class="hate">(.*)</span>')

def GetData (baseurl):
    #获取数据
    html = askurl(baseurl)
    #解析数据
    soup = BeautifulSoup(html,"html.parser")
    print(soup)
    Datalist=[]
    for item in soup.find_all('div',class_="con"):
        print(item)
        data = []
        # print("准备处理数据")
        # username = re.findall(findUsername,item)
        # print(username)
        # data.append(username)
        # comment = re.findall(findComment,item)
        # data.append(comment)
        # time = re.findall(findTime,item)
        # data.append(time)
        # likes = re.findall(findLikes,item)
        # data.append(likes)
        # print("处理数据")
        Datalist.append(data)
    return (Datalist)



def askurl(baseurl):
    headers={                                           ##模拟浏览器头部信息
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.96 Safari/537.36 Edg/88.0.705.56"
        }  
    request = urllib.request.Request(url=baseurl,headers=headers)
    html=""
    try:
        response = urllib.request.urlopen(request)
        html = response.read()#根据报错内容，文件经过压缩，需要进行解压操作
        #文件内容解压（二进制？）
        buff = BytesIO(html)
        f = gzip.GzipFile(fileobj=buff)
        html = f.read().decode('utf-8')
        print("获取成功")
        # print(html)
    except urllib.error.URLError as e :
        if hasattr(e,"code"):
            print(e.code)
        if hasattr(e,"reason"):
            print(e.reason)
    return html






if __name__ == "__main__":
    main()
    print("爬取完毕")