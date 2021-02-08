# coding=UTF-8

infos={
    'sid':1,
    'sname':'小明',
    'shobby':['篮球','游泳','外语'],
    'sbir' : 416,                           #以数字0开头可能会引起计算机识别时更改进制
}

#拷贝字典
infos2 = infos.copy()
#print(infos2)

#利用现成的列表创建字典
ke='abcd'
infosk= dict.fromkeys(ke)
print(infosk)
lis=['1','2','3','4']
infosl= dict.fromkeys(ke,lis)               #该语句只能把逗号后的全部内容逐个赋值给前面的键
print(infosl)

#字典的补充
infos.update(infos2)                        #把infos2添加到infos的末尾
