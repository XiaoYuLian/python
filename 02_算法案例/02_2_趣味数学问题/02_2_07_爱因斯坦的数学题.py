"""
一条长台阶，
每步跨2阶则余1，每步3阶则余2，每步5阶则余4，每步6阶则余5，每步7阶则正好。
问：在1到n内，有多少个数能满足？
"""
n=int(input("请输入范围上限："))
m=0                                                     #计数变量初始化
for i in range (8,n+1):
    a=i%2
    b=i%3
    c=i%5
    d=i%6
    e=i%7
    if (a==1 and b==2 and c==4 and d==5 and e==0):
        m+=1
        print(i)
print (m)