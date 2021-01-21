# coding=UTF-8
score=int(input("输入成绩"))
if (0<=score<=100):
    if (score>=85):
        print ("A")
    elif(score>=75):
        print("B")
    elif (score>+60):
        print("C")
    else:
        print("D")
else :
    print ("输入错误")