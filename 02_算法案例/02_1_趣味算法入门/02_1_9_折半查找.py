"""

"""
def find(a,target):
    """
    折半查找法-->在有序数列a中，查找target是否存在若存在则求出位置。
    """
    n=len(a)
    lab=-1
    
    l=0
    low=a[l]
    m=n//2
    mid=int(a[m])
    h=(n-1)
    high=a[h]
    while low<mid:
        if(target<mid):
            h=m
            high=a[h]
            m=(h+l)//2
            mid=a[m]
        elif target>mid:
            l=m
            low=a[l]
            m=(l+h)//2
            mid=a[m]
        else:
            print("目标值的位置在%d" %(m+1))
            lab=1
            break
    if lab ==-1:
        print ("目标数不在数列中")

if __name__=="__main__":
    print("请输入数组")
    x=input()
    a=x.split(" ")
    n=len(a)
    for i in range(0,n):
        a[i]=int(a[i])
    target=int(input("请输入要查找的数值"))
    find(a,target)