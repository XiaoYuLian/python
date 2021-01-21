"""
假设自1990年1月1日开始三天打鱼两天筛网，计算指定日期是该大于呢还是筛网呢
"""

def runYear(year):
    """
    判断是否是闰年
    """
    i=0
    if(year%400==0):
        i=i+1
    elif(year%4==0 and year%100!=0):
        i=i+1
    return i

def totalDay(year,mon,day):
    """
    计算距1990年1月1日一共有多少天
    """
    permonth=[0,31,28,31,30,31,30,31,31,30,31,30,31]
    nian=(year-1990)*365
    yue =0
    for a in range(1990,year):
        nian=nian+runYear(a)
    for b in range(0,mon,1):
        print ("月换算：",yue)
        yue=yue+permonth[b]
    print("年换算：",nian)
    
    n=nian+yue+day
    k=runYear(year)
    if(k==1 and mon>2):
        n=n+1
    return n

print("请输入年月日")
year,mon,day=map(int ,input().split())
n=totalDay(year,mon,day)
print("距起始日期一共%d天"%n)
if(n%5<4):
    print("今日打鱼")
else:
    print("今日晒网")