#-*- coding = utf-8 -*- 
import bs4                              #解析网页，获取数据
import re                               #正则表达式，进行文字匹配
import urllib.request,urllib.error      #制定url，获取网页数据
import pandas.io.excel._xlwt            #进行excel操作
import sqlite3