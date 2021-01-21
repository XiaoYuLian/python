import sympy                        #引入方程变量
i=1
while i==1:
    x = sympy.symbols("x")              # 申明未知数"x"
    a=int(input('请输入初期投资额'))
    b=int(input('请输入年收益'))
    p= ((1+x)**15-1)/(((1+x)**15)*x)
    irr=sympy.solve([b*((1+x)**15-1)/(((1+x)**15)*x)-a],[x])
    print (irr)