# coding=UTF-8
#统计学变量
#装载随机数工作包
import random
win=0
lose=0
x=1
#准备循环
while x<=30000:
    #电脑随机生成正确的选项
    aim=random.randint(1,3)
    #由玩家猜一个选项
    player=random.randint(1,3)
    #排除玩家选项外的一个错误答案
    i=1
    while i<=3:
        if(i==aim or i==player) :
            i += 1
            continue
        else :
            #print("现在排除错误选项%d" %i)
            break
    #询问玩家是否要更换选项
    q=1
    if (q==1) :
        j=1
        while j<=3 :
            if (j==player or j==i) :
                j+=1
                continue
            else :
                player=j
                break
    #输出游戏结果
    if (player==aim):
        win+=1
        #print("你猜对了")
    else :
        lose+=1
        #print("真可惜，你猜错了")
    x+=1
#输出多次实验的最终结果
print("总计:实验的总次数是%d猜对的次数是%d,猜错的次数是%d"%(x-1,win,lose))

