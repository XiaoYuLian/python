y=[245,250,256,280,274,255,263,270,273,284,289,286,295,301,312]

# 一次移动平均法 N=5
N=5
sum=0
for i in range(0,5):
    sum=sum+y[i+10]
M1=sum/N
print(M1)
