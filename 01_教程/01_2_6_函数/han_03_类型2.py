# coding=UTF-8
# 函数的4种类型：有参有返回
def f4 (a,b,oper):
    if oper=='+':
        return a+b
    elif oper=='-':
        return a-b
    elif oper=='*':
        return a*b
    elif oper=='/':
        return a/b
i= f4(3,4,"+")
print i