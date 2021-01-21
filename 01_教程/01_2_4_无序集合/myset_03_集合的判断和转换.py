# coding=UTF-8
myset1={110,114,119}
myset2={110,119}

#判断myset2是不是1的子集
print(myset2.issubset(myset1))
print(myset1.issubset(myset2))

#判断某个元素是不是在某个集合中
i=110
print(i in myset1)                                  #元素可以是以变量存在
print(911 in myset1)                                #元素也可以直接进行判断

#无序集合宇列表、元组之间的转换
#list()                                             #转换为列表
#tuple()                                            #转换为元组
#set()                                              #转换为集合
