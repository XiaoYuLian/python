#用牛顿法求三次方程的近似根
def newton(a,b,c,d):
    """
    docstring
    各项的系数根据未知数的次数由高到低分别为abcd，
    根的估计值设为1
    """
    x=1
    x0=x
    f=a*x0*x0*x0+b*x0*x0+c*x0+d
    fd=3*a*x0*x0+2*b*x0+c
    h=f/fd
    x=x0-h
    while abs(x-x0)>=1e-5:
        x0=x
        f=a*x0*x0*x0+b*x0*x0+c*x0+d
        fd=3*a*x0*x0+2*b*x0+c
        h=f/fd
        x=x0-h
    return x

print("请输入方程的系数")
a,b,c,d=map(float,input().split())          ##利用map做映射的多变量同行输入
print("方程度系数为",a,b,c,d)
x=newton(a,b,c,d)
print(x)