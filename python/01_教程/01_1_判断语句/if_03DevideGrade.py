# coding=UTF-8
score=int(input("请输入成绩"))
if(score<60):
    print("D")
else:
    if(score<75):
        print("C")
    else:
        if(score<90):
            print ("B")
        else:
            print ("A")