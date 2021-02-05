#-*- coding = utf-8 -*- 
from bs4 import BeautifulSoup           #解析网页，获取数据
import re                               #正则表达式，进行文字匹配
import urllib.request,urllib.error      #制定url，获取网页数据
import pandas.io.excel._xlwt            #进行excel操作
import sqlite3



def main():
    baseurl = "https://movie.douban.com/top250?start=&filter="
    #1、爬取网页
    datalist = GetData(baseurl)
    #3、保存数据
    savepath=".\\豆瓣电影Top250.xls"    #.\\表示文件目录；./表示当前文件夹
    SaveData(savepath)


#爬取网页
def GetData(baseurl):
    datalist=[]
    #2、逐一解析数据
    return datalist


#保存数据
def SaveData(savepath):
    print (save)



if __name__ == "__main__":
    main()