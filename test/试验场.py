# permonth=[31,28,31,30,31,30,31,31,30,31,30,31]
# n=0
# for a in range(0,6):
#     n=n+permonth[a]
# print(5/2)
# a=[1,2,3]
# b=[4,5,6]
# print(a+b)
# print (a*3)


# a=5/3
# b=5%3
# c=(23/10)%10
# print (a,b,c)


# a=[0,0,0,0,0]
# b=[0,0,0,0,0]
# for i in range (1,5):
#     a[i]=i
# for i in range (1,5):
#     b[i]=2*i
# print (a,b)

# for j in range (4,21):
#     n=j
#     for i in range (2,int(n**0.5)+1):
#         if n%i==0:
#             print ("%d不是质数" %n)
#             break
#     else:
#         print("%d是质数" %n)

i=0 
for j in range (1,21):
    k=int(input("第%d选项是"%j))
    i=i+k
print (i)