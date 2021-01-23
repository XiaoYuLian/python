"""
冒泡法排序
"""

def bubblesort(a):
    """
    将出入的数据进行排序
    """
    n=len(a)
    i=0
    for i in range(0,n-1):
        j=0
        for j in range(0,n-1):
            if(a[j]>a[j+1]):        #从小到大排序
                t=a[j+1]
                a[j+1]=a[j]
                a[j]=t
    print(a)

if __name__=="__main__":
    print("请输入数据")
    x=input()
    a=x.split(" ")
    n=len(a)
    for i in range (0 ,n):
        a[i]=int(a[i])
    bubblesort(a)