# coding=UTF-8

infos={
    'sid':1,
    'sname':'小明',
    'shobby':['篮球','游泳','外语'],
    'sbir' : 416,                           #以数字0开头可能会引起计算机识别时更改进制
}

#字典的删除
v=infos.pop('sid')                          #这个操作会对原本的infos内容也进行修改
# print(v)
# print(infos)
w=infos
del w ['shobby']
#print (w)
#想完全清空可以直接使用infos.clean()

#字典的判断
print('sid' in infos)
print('sid' not in infos)
print(1 in infos.values())                  #在该语句中value后的括号中不能选择范围
print(416 in infos.values())

#字典的遍历
for key in infos:
    print(key)
    print(key+':'+str(infos[key]))           #在一个print语句中输出多个值，需要用+链接各个值