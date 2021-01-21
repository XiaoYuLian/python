#ctrl+shift+F10
"""
    固定成本 FC=180 百万,平均可变成本 AVC=（1+TQ/1500+150/TQ）百万，国家定额利润IG=5%
    计划年运输量 TQ=500 百万吨公里，预期总利润 interest= 200百万，国家定额利润 tax= 5.6%
求 
  1 外加法和内加法的企业定价
  2 计算企业年运量为3……9时的平均成本和边际成本
  3 如果企业定价为2.5万/百万吨公里要达到预期利润水平需要的年运量是多少
"""
"""
# 平均成本计价法
Pw=ATC*(1+CJ)/(1-tax)
Pn=ATC/(1-SJ-tax)
"""
FC=180.0
TQ=500.0
interest=200.0                 
tax=0.056

AFC=FC/TQ                       #平均固定成本
AVC=(1+TQ/1500+150/TQ)          #平均可变成本
ATC=AFC+AVC                     #平均总成本
DJ=interest/TQ                  #单位运量利润率
CJ=interest/(ATC*TQ)            #成本利润率
SJ=interest/(interest+ATC*TQ)   #利润率
#题目一
Pw=ATC*(1+CJ)/(1-tax)
Pn=ATC/(1-SJ-tax)
K=(1+CJ)/(1-tax)
print(Pw,Pn,K,ATC,CJ)

#题目二
TQ=300.0
while TQ<=900 :
    AFC=FC/TQ                       #平均固定成本
    AVC=(1+TQ/1500+150/TQ)          #平均可变成本
    ATC=AFC+AVC                     #平均总成本
    DJ=interest/TQ                  #单位运量利润率
    CJ=interest/(ATC*TQ)            #成本利润率
    SJ=interest/(interest+ATC*TQ)   #利润率
    VC=AVC*TQ                       #总可变成本

    TQI=TQ+1
    AFCI=FC/TQI                       #平均固定成本
    AVCI=(1+TQI/1500+150/TQI)          #平均可变成本
    ATCI=AFCI+AVCI                     #平均总成本
    DJI=interest/TQI                  #单位运量利润率
    CJI=interest/(ATCI*TQI)            #成本利润率
    SJI=interest/(interest+ATCI*TQI)   #利润率
    VCI=AVCI*TQI                       #总可变成本

    MC=VCI-VC
    print("当TQ=%d时，ATC=%d，MC=%d"%(TQ,ATC,MC))
    TQ=TQ+100


#第三题
import sympy                        #引入方程变量
TQ=sympy.symbols("TQ")              #定义未知数（自变量）TQ
AVC=(1+TQ/1500+150/TQ)              #AVC
AFC=180/TQ
ATC=AVC+AFC
a= sympy.solve([ATC*(1+0.05)/(1-0.056)-2.5],[TQ])   #解方程命令，（[Fx=0],[未知量]）
print(a)
