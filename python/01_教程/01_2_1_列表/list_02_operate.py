# coding=UTF-8
# 对列表内容能进行操作
#原列表
Is=['aa',"bb","cc"]
print(Is)
# 列表新增/后续
Is.append("dd")
print(Is)
# 添加/插入
# 在1位插入“one”
Is.insert(1,"one")
print(Is)
#列表扩展
Is1=[110,119,120]
Is2=[1,2,3]
print(Is1)
print(Is2)
Is1.extend(Is2)             #在列表1的后面扩展列表2的全部内容
print(Is1)
#对列表中的那个元素进行修改
Is3=[0,1,2,3,4,5]
print(Is3)
Is3 [1] =10
print(Is3)
#列表的脚本操作
a=[1,2,3]
b=[4,5,6]
print(a+b)
print (a*3)