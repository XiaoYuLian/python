"""
在国际象棋8X8过64个各自的棋盘上放麦粒，第一个各自放一个，第二个各自放两个，第三个格子放三个，总共需要多少麦子？
"""
print("kaishi")
for i in range (1,65):
    m=0                         #累计变量
    k=1                         #内循环控制变量
    n=1                      
    while (k<i):
        n=n*2
    m=m+n
print(m)
print ("jieshu")