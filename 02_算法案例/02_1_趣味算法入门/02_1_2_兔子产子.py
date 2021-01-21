"""
有一对兔子出生后三个月成熟成熟后的兔子每产一个对小兔子
假设所有兔子都不死
30个月后有多少个兔子?
"""

a,b,c=1,1,0
i=int(input())
j=2
while j<=i :
    c=a+b
    a=b
    b=c
    j=j+1
    print (a,end='\t')   #end控制print的结尾
print("")