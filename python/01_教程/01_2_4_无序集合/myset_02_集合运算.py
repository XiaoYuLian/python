# coding=UTF-8
myset1 = {1,2,3}
myset2 = {3,4,5}
#集合的并
bing1=myset1 | myset2
print(bing1)
bing2=myset1.union(myset2)                      #这两种方式都不影响myset的原值
print(bing2)

#集合的交
jiao1=myset1 & myset2
jiao2=myset1.intersection(myset2)
print(jiao1)

#集合的差
cha1 = myset1 - myset2
print(cha1)
cha2 = myset2.difference(myset1)                #集合的差运算有先后顺序的区别
print(cha2)