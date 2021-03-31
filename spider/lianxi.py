#-*- coding = utf-8 -*- 
from bs4 import BeautifulSoup           #解析网页，获取数据
import re                               #正则表达式，进行文字匹配
import urllib.request,urllib.error      #制定url，获取网页数据
import pandas.io.excel._xlwt            #进行excel操作
import sqlite3
import xlwt



def main():
    baseurl = "https://movie.douban.com/top250?start="
    #1、爬取网页
    datalist = GetData(baseurl)
    #3、保存数据
    savepath=".\\豆瓣电影Top250.xls"                      #.\\表示文件目录；./表示当前文件夹
    SaveData(datalist,savepath)
    # askURL("https://movie.douban.com/top250?start=&filter=")      #会在下方的终端中显示一遍获取到的内容用于检测
    
#制定用于获取对应消息的正则表达式
findlink = re.compile(r'<a href="(.*?)">')              #获取影片详情页链接
findImgsrc = re.compile(r'<img.*?src="(.*?)"',re.S)     #图片
findTitle = re.compile(r'<span class="title">(.*)</span>') #标题
findRating = re.compile(r'<span class="rating_num" property="v:average">(.*)</span>') #评分
findJudge = re.compile(r'<span>(\d*)人评价</span>')     #评价人数
findInq = re.compile(r'<span class="inq">(.*)</span>')  #评语
# findBd = re.compile(r'<p class>(.*?)</p>,re.S')      #影片详情


#爬取网页
def GetData(baseurl):
    datalist=[]
    for i in range (0,10):
        url=baseurl + str(i*25)                         #基础url+每页的起始序号
        # askURL(url)
        html = askURL(url)
        #2、逐一解析数据
        soup = BeautifulSoup(html,"html.parser")        #把获取到的信息(hrml)使用"html.parser"解析器打开，定义为一个新的变量 soup
        for item in soup.find_all('div',class_="item"): #找到所有div，并且包含class为item的属性。class后加下划线，与系统关键字区分。
            # print(item)
            data=[]                                     #保存一部电影的信息
            item=str(item)

            link = re.findall(findlink,item)[0]
            data.append(link)
            Imgsrc = re.findall(findImgsrc,item)[0]
            data.append(Imgsrc)
            Titles = re.findall(findTitle,item)
            if (len(Titles)==2):
                CTitle=Titles[0]
                data.append(CTitle)
                OTitle=Titles[1].replace("/","")        #replace 将名字中的斜杠换成空
                data.append(OTitle)
            else:
                data.append(Titles[0])
                data.append(' ')                        #留空，保证excel中数据结构整齐
            Rating = re.findall(findRating,item)[0]
            data.append(Rating)
            Judge = re.findall(findJudge,item)[0]
            data.append(Judge)
            Inq = re.findall(findInq,item)
            if (len(Inq)!=0):
                Inq=Inq[0].replace("。","")
                data.append(Inq)
            else:
                data.append(" ")
                
            # Bd = re.findall(findBd,item)[0]
            # Bd = re.sub('<br(\s+)?>(\s+)?'," ",str(Bd)) #去掉其中的<br/>
            # Bd = re.sub('/'," ",Bd)                     #替换/-->空格
            # data.append(Bd.strip)                       #去掉前后空格
            datalist.append(data)                       #吧处理好的信息放入datalist 

    # print(datalist)
    return datalist

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


#保存数据
def SaveData(datalist,savepath):
    print ("saving")
    workbook = xlwt.Workbook(encoding="utf-8")                                      #创建workbook对象
    worksheet = workbook.add_sheet('豆瓣top',cell_overwrite_ok=True)                #创建工作表
    clo = ("电影详情","图片","中文名","外文名","评分","评价数","概况")
    for i in range(0,7):                                                            #表头
        worksheet.write(0,i,clo[i])
    for i in range (0,250):
        print("正在处理第%d条信息" %(i+1))
        data=datalist[i]
        for j in range (0,7):
            worksheet.write(i+1,j,data[j])  
    workbook.save('豆瓣电影Top250.xls')                                        #第一行是表头，佛而已微试是i+1，j


if __name__ == "__main__":
    main()
    print("爬取完毕")