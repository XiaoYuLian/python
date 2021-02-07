from bs4 import BeautifulSoup


file = open ('/mnt/d/tools/code/objects/python/test/baidu.html',"rb")       #rb-->read bytes,二进制读取
html=file.read()
bs= BeautifulSoup(html,"html.parser")

"""
1、tag:找到并获取第一个对应的标签和里面的内容
"""
# print(bs.title)
# print(bs.a)
# print(bs.head )
# print(type(bs.head))


"""
2、string:标签里的内容
"""
# print(bs.title.string)
# print(type(bs.title.string))


"""
3、beautifulsoup:整个文档
"""
# print(bs.a.attrs)
# print(type(bs))


"""
4、comment:特殊的string不包括注释符号（但包含注释内容）
"""
# print(bs.a.string)
# print(type(bs.a.string))


#-----------------------------------------------------------------------------
#文档的遍历



#文档的搜索
#(1)、find_all
t_list = bs.find_all("a")
print(t_list)