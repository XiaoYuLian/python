"""
"""
a=[0,10,2,8,22,16,4,10,6,14,20]
b=[0,0,0,0,0,0,0,0,0,0,0,]
k=0                             #循环控制变量
while k==0:                      
    
    for i in range(1,10):        #右侧的人可以从左侧获得的糖果数,记为b
        b[i+1]=a[i]/2
    b[1]=a[10]/2
    
    for i in range (1,11):      #每个人分出一半糖果后剩余的糖果数量
        a[i]=a[i]/2

    for i in range (1,11):      #接受糖果后的数量
        a[i]=a[i]+b[i]

    for i in range (1,11):      #奇数补足
        if(a[i]%2==1):
            a[i]=a[i]+1
            
    a[0]+=1                     #计数位统计次数

    k=1                         #循环控制变量回复跳出位
    for i in range (1,10):      #判断糖果数是否相等的，若有不相等循环控制变量置为0
        if a[i]!=a[i+1]:
            k=0
print(a)
    