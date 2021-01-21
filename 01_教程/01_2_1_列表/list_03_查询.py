# coding=UTF-8
# 在列表中各个元素的编码顺序为：从前往后——0，1，2，3，
#                             从后往前——-1，-2，-3，-4
Is=[110,119,120,210,211]
print(Is[2])
print (Is[-2])


#查找指令：显示对应值的位置
print(Is.index(120))            #查找值
print(Is.index(120,0,4))          #查找值，起始位置
print(Is.index(120,2,4))        #查找值，起始位置，终止位置


#计数指令
Is1=[110,120,121,120,120,119]
print(Is1.count(120))
#列表长度
Is2=[110,120,121,210,210,120,119,110,120]
print(len(Is2))
#列表最值
print (min(Is2))
print (max(Is2))
#列表删除
ret1=Is2.pop(2)#按位置删除
ret2=Is2.remove(120)#按内容删除
print(Is2)
print(ret1)


#列表判断:返回TRUE或FALES
print (110 in Is2)
print (300 in Is2)
