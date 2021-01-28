"""
税金的阶梯计算
"""
TaxTable=[
    (0,500,0.05),
    (500,2000,0.1),
    (2000,5000,0.15),
    (5000,20000,0.2),
    (20000,40000,0.25),
    (40000,60000,0.3),
    (60000,80000,0.35),
    (80000,100000,0.4),
    (80000,1e10,0.45)]
print("cc")

def CaculateTax(x):
    """
    税金的阶梯计算
    """
    print("bb")
    i=0
    tax=0
    while (x>TaxTable[i][0]):
        if(x<TaxTable[i][1]):
            tax+=(x-TaxTable[i][0])*TaxTable[i][2]
            break
        else:
            tax+=(TaxTable[i][1]-TaxTable[i][0])*TaxTable[i][2]
        i+=1
    return(tax)


if __name__=="__main__":

    print("aa")
    x=int(input("请输入金额"))
    tax=CaculateTax(x)
    print ("应缴的税金为%d" %tax)