# coding=UTF-8
#if顶格写之后空一格+家要判断的条件+    ：第二行用tab键或四个空格起始
#tab与空格不能混用，两者只能用其一。
i=1
while i==1:
    #例一：判断年龄
    age=(int(input("你的年龄是")))
    if age>=18:
        print("你已经成年")
        print("you are not along")
        print("you are great")
    else :
        print("you are still young")
        print("tomorrow is other day")
    #if语句的范围：自if始每一行缩进的语句都包括在内。


    #if语句的进阶——elif
    #elif=else if
    #例二
    a=int(input("输入你的成绩"))
    if a>=90:
        print("A")
    elif a>=80:
        print("B")
    else:
        print("C")
    i=int(input())
    


