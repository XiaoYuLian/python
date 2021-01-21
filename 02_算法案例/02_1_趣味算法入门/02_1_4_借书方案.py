"""
五本书借给三个人有几种借法
"""
i=0
for a in range(1,6):
    for b in range(1,6):
        for c in range(1,6):
            if(a!=b and a!=c and b!=c ):
                print("A:%d B:%d C:%d" %(a,b,c),end="   ")
                i=i+1
print("共有组合%d种" %i)

##for循环范围有头无尾，默认步长为1