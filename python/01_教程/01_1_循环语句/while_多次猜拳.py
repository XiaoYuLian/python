# coding=UTF-8
#ctrl+shift+F10
#使用循环结构进行多次的猜拳比赛
#载入随机数工具包
import random
#控制猜拳局数
i=int(input("请输入局数 ：" ))
j=1
#统计最终结果
win=0
lose=0
while j<=i :
    #电脑出拳
    computer=random.randint(1,3)
    #玩家出拳
    player=int(input("请输入您的选择  1-拳 -- 2-剪刀 -- 3-布    :"))
    #显示双方的选择
    print("你要出的是：%d - 电脑出的是：%d " %(player,computer))
    print("",computer)
    #输出比赛结果
    if ((player==1 and computer==2)
        or (player==2 and computer==3)
        or (player==3 and computer==1)) :
        print("真厉害，你赢了。")
        win+=1
    elif ((computer==1 and player==2)
        or (computer==2 and player==3)
        or (computer==3 and player==1)) :
        print("真可惜，你输了")
        lose+=1
    else :
        print("真是心有灵犀，是平局")
    j+=1
if (win>lose) :
    print("你取得了最终的胜利")
elif (win<lose) :
    print("可惜总体上还是我更胜一筹")
else :
    print("是平局呢，下次再来挑战吧。")