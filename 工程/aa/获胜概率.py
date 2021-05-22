"""

"""
def Jiechen (k):
    mul=1
    for i in range(1,k+1):
        mul=mul*i
    return (mul)

def Combinatoral (n,i):
    '''设计组合数'''
    nI=Jiechen(n)
    iI=Jiechen(i)
    Canshu=Jiechen(n-i)
    # print(nI,iI,Canshu)
    result=nI/(iI*Canshu)
    return result



def main ():
    GWin=int(input("输入比赛获胜所需分数="))
    TWin=float(input("出入单局获胜概率="))
    FinalWin=Calc(GWin,TWin)
    print(FinalWin)

def Calc (Gwin,Twin):
    sum=0
    for i in range (Gwin,Gwin*2):
        mid = Combinatoral(i-1,Gwin-1)*(Twin**(Gwin-1))*((1-Twin)**((i-1)-(Gwin-1)))*(Twin)
        sum=sum+mid
    return sum


if __name__ ==  "__main__":
    main()