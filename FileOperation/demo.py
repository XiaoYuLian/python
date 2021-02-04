# f=open("aa.txt","w")
# f.write("Hellow World!")
# f.close
f=open("aa.txt","r")
content=f.read(5)
content=f.read(6)
f.close
print(content)