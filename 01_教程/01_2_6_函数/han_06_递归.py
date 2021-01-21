# coding=UTF-8
#递归函数：函数在自己内部调用自己，产生循环但是有跳出条件。
#定义函数
def rec(num):
    if num==1 or num==2:
        return 1
    return (rec (num-1)+rec(num-2))

#主程序
for i in range (1,11):
    print(rec(i))


#匿名函数：如果函数只调用一次则可以使用匿名函数
is1=[1,2,3,4,5]
is2=list (map(lambda x: x**2,is1))                  #map的作用是去除is1中的值做映射；lambda表明是匿名函数   ：左侧是参数，右侧是返回值
print is2

is3=[1,2,3]
is4=[4,5,6]
is5=list(map(lambda x,y:x+y,is3,is4))
print is5