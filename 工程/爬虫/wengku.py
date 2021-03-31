#-*- coding = utf-8 -*- 
from bs4 import BeautifulSoup           #解析网页，获取数据
import re                               #正则表达式，进行文字匹配
import urllib.request,urllib.error      #制定url，获取网页数据
import pandas.io.excel._xlwt            #进行excel操作
import sqlite3
import xlwt


def main():
    baseurl = "https://wenku.baidu.com/view/58ec0d72a417866fb84a8ecc.html"
    #1、爬取网页
    datalist = GetData(baseurl)
    #3、保存数据
    savepath=".\\豆瓣电影Top250.xls"                      #.\\表示文件目录；./表示当前文件夹
    

#制定用于获取对应消息的正则表达式
findUsername = re.compile(r'class="name ">(.*)</a>')        #获取主评论人的站好名称                
findComment = re.compile(r'<p class="text">(.*) </p> ')     #获取主评论
findTime = re.compile(r'<span class="time">(.*)</span>')    #获取评论时间
findLikes = re.compile(r'<span class="like"><i></i><span>(.*)</span>')    #获取点赞数


def GetData (baseurl):
    #获取数据
    html = askURL(baseurl)
    print(html)
    #解析数据
    soup = BeautifulSoup(html,"html.parser")
    # print(soup.p)
    Datalist=[]
    for item in soup.find_all('p'):
        # print(item)
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


#得到指定的一个网页的内容
def askURL(url):
    headers={                                           ##模拟浏览器头部信息
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.96 Safari/537.36 Edg/88.0.705.56"
        }                                               #告知服务器我们是什么样的机器、浏览器（本质上是告知我门可以接受什么严格内容）
    reqeust=urllib.request.Request(url=url,headers=headers)
    html=""                                             #定义存放数据的变量
    try:
        response=urllib.request.urlopen(reqeust)
        html=response.read().decode("utf-8")
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