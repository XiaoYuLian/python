# coding=UTF-8
#字典的定义：使用大括号、每一组键和值用冒号链接、组与组之间用逗号隔开
student={'sid' : 110,'sname':'小明','ssax':'男','sscore':89}
#字典的新增与修改
infos={
    'sid':1,
    'sname':'小明',
    'shobby':['篮球','游泳','外语']
}
infos['saddress']='河南郑州'
infos['sid']=110

#字典的查询
print(infos['saddress'])        #直接查询
print(infos.get('sid'))         #使用get查询，若不存在相应的值则返回None
print(infos.get('syears'))

#字典的计数
print(len(infos))

#输出字典的全部内容
ret= str(infos)
print (ret)

#输出字典里的全部键
keys = infos.keys()             #infos.keys可以返回所有的键，
print(keys)                                 
for i in keys:                  #用foe循环将其逐个输出
    print(i)                    