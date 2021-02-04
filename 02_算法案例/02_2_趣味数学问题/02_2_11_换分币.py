"""
将5元，换为1元，5角或1角的硬币，有几种换法。
"""
n=0
for i in range (0,6):
    for j in range (0,11):
        c=50-i*10-5*j
        if c>=0 :
            n+=1
            print(n,i,j,c,end ="    ")
print ("总共可能的情况有%d种" %n)
