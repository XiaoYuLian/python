# coding=UTF-8
#sshi用print时：    1、可以省略括号 2、格式化输出需要根据输出类型使用类型符
#   例如：%d——输出整数  %a——输出浮点数  %s——输出字符串
def func(a=3,b=4):                              #在定义函数时可以给参数一个预设值，调用函数时当参数为空则自动填充
    c=100                                       #在函数内定义的变量不会宇外部互相影响
    h=300                                       #在函数内部定义的变量不能再函数值wide地方使用
    print 'a=%d,b=%s,c=%d,h=%d'%(a,b,c,h)
c=500
d=600
func(1)
print c