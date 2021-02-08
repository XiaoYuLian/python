# coding=UTF-8

#无序集合的定义
myset={1,3,5,2,3,2,3,1,1,1,2,3}                         #无序集合和字典很像都使用大括号定义，只是无序集合没有键
print(myset)                                            #在定义时程序会自动滤过重复的元素      

#无序集合的新增
myset.add(100)                                          #新增元素
print(myset)

ad={6,7,7,4,6,8}                                        #合并集合
myset.update(ad)
print(myset)

#无序集合的删除
myset.remove(4)                                         #去除括号中的元素，若不存在则报错
myset.discard(100)                                      #去除括号中的内容，若不存在不会报错
#myset.pop()                                            随机删除无序集合中的元素
#myset.clear()                                          清空集合中的内容

