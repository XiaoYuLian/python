import random
# n = int(input("请输入想要的数列长度： "))
n=5
c=[]
d=[]
for i in range (0,n):
    c.append(i)
    d.append(i)
random.shuffle(c)
print (c)
print (d)

