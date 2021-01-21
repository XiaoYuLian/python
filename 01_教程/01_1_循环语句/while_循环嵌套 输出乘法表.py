#ctrl+shift+F10
# coding=UTF-8
#利用循环嵌套控制输出，输出乘法表
#控制各行的内容
i=1
while i<= 9:
    j=1
    while j<=i-1 :
        print("%d X %d= %d"%(j,i,i*j))
        j=j+1
    print("%d X %d= %d"%(j,i,i*j))
    i+=1