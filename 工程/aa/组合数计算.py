
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
    print(nI,iI,Canshu)
    result=nI/(iI*Canshu)
    return result

def main () :
    n=int(input ("出入排列组合数n="))
    i=int(input ("出入排列组合数i="))
    result=Combinatoral(n,i)
    print (result)

if __name__ ==  "__main__":
    main()