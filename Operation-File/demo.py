# f=open("aa.txt","w")
# f.write("Hellow World!")
# f.close
f=open("aa.txt","r")#文件名必须不齐后缀
content=f.read(6)#使用open读取恩文件时，连续读取两次会累加读取起始点。
print(content)
content=f.read(6)
f.close
print(content)

f= open("aa.txt")
cont=f.read(6)#当重新打开文件时，七十点重新开始计算
f.close
print(cont)

# print (i)
# g=open("bb.txt","a")
# g.write("今天心情很不好"'\t'"我只想说三句话"'\n'"包括上一句在内"'\n'"我说完了")
# g.close