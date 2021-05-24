import random

"""
1、生成初始条件
"""
b=[]
f=[]
c=[]
n = int(input("请输入想要的青蛙数： "))+1

for i in range (1,n):
    b.append (i)
    c.append (i)
    f.append (i)
random.shuffle(f)
if (n%2==0):
    b.append (n)
    c.insert(int(n/2-1),0)
    f.insert(int(n/2-1),0)
elif (n%2==1):
    b.append (n)
    c.insert(int(n/2),0)
    f.insert(int(n/2),0)


"""
2、检测初始条件是否达标
"""
t=1#检验标志位，1表示一致，0表示不一致。
for i in range (0,n):
    if (c[i]==f[i]):
        t=1
    else:
        t=0
        break


"""
3、操作和调整
"""
print("位置编号",b)
print("")
print("青蛙位置",f)
print("对应位置",c)
while t == 0:
    mid=int(input("选择要哪个杆上的青蛙移动: "))
    a=mid-1
    #倒数第一个值
    if (a==n-1):
        if (f[a-1]==0):
            f[a-1]=f[a]
            f[a]=0
        elif(f[a-2]==0):
            f[a-2]=f[a]
            f[a]=0
    #倒数第二个值
    elif (a==n-2):
        if (f[a+1]==0):
            f[a+1]=f[a]
            f[a]=0
        elif(f[a-1]==0):
            f[a-1]=f[a]
            f[a]=0
        elif(f[a-2]==0):
            f[a-2]=f[a]
            f[a]=0
    #第一个值
    elif (a==0):
        if (f[a+1]==0):
            f[a+1]=f[a]
            f[a]=0
        elif(f[a+2]==0):
            f[a+2]=f[a]
            f[a]=0
    #第二个值
    elif (a==1):
        if (f[a+1]==0):
            f[a+1]=f[a]
            f[a]=0
        elif(f[a+2]==0):
            f[a+2]=f[a]
            f[a]=0
        elif(f[a-1]==0):
            f[a-1]=f[a]
            f[a]=0
    #在中间的值
    elif(f[a+1]==0):
        f[a+1]=f[a]
        f[a]=0
    elif(f[a-1]==0):
        f[a-1]=f[a]
        f[a]=0
    elif(f[a+2]==0):
        f[a+2]=f[a]
        f[a]=0
    elif(f[a-2]==0):
        f[a-2]=f[a]
        f[a]=0

    print("位置编号",b)
    print("")
    print("青蛙位置",f)
    print("杆的位置",c)   

    for i in range (0,n):
        if (c[i]==f[i]):
            t=1
        else:
            t=0
            break
print("恭喜通关")
    


     


"""

"""