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
#字符串过滤：会查找与 字符串完全匹配的内容 
#与正则表达式、函数配合，可以找出所有符合条件的内容

# t_list = bs.find_all("a")

#   1.1正则表达式搜索：使用search（）方法来匹配内容
# import re
# t_list = bs.find_all(re.compile("a"))             #所有含有'a'的标签里的内容


#   1.2方法 ： 传入一个函数（方法），根据函数的要求来搜索
# def name_is_exists(tag):                          #传入一个标签
#     return tag.has_attr("name")                   #返回标签里name的属性（attr）
# t_list = bs.find_all(name_is_exists)              #有name标签的可以被搜出来


##########################################################################################
#（2）kwargs        参数

# t_list = bs.find_all(id="head")                   #找出id= head 的标签的内容
# t_list = bs.find_all(href="http://news.baidu.com")
# t_list = bs.find_all(class_= True)                #class加了下划线应该是为了与python保留的关键字区分开，true应该是指非空；
                                                    # 有趣的是，如果母级标签和子标签都负荷条件，那么他会完整的输出母标签，再独立输出子标签


###########################################################################################
#(3).text参数

# t_list = bs.find_all(text="hao123")               #查找相应的文本
# t_list = bs.find_all(text=["hao123","地图","贴吧"]) #查找时，可以直接把所有的目标组成列表
# import re
# t_list = bs.find_all(text= re.compile("\d"))      #结合了正则表达式(-->re.compile),"\d"-->所有数字，注意斜杠的方向不要打错斜杠


###########################################################################################
#(4).limit参数

#t_list = bs.find_all("a",limit=3)                  #在搜索a的基础上，加上了限制-->  只要3条


###########################################################################################
#(5).css选择器

# t_list = bs.select("title")                       #select 后面直接指定标签
t_list = bs.select(".mnav")                       #select 后面直接指定特定类，css中通过class=,调用相应类来控制颜色字体等样式，.mnav应该是其中一种
# t_list = bs.select("#u1")                         #select 后面直接指定id（不清楚井号的意义，不过u1确实是网站中某个id的值
# t_list = bs.select("a[class='bri']")              #select 后面直接指定某个标签（这里是a）的属性（例中用的class） 注意引号，这里要用两次引号，用单双引号区别开
# t_list = bs.select("title")
# t_list = bs.select("head>title")                  #按结构查找 "head>title"---->表示head里面的title
# t_list = bs.select(".mnav~.bri")                  #按结构查找 ".mnav ~ bri"---->表示与.mnavt平级的.bri

# print(t_list)

for item in t_list:                                 #遍历输出列表-->是输出的结果分行
    print(item)

# print(t_list[0])                                  #由于结果是列表，我们可以用t_list[0]来选择输出第一个内容
# print(t_list[0].get_text())                       #对于单个列表元素，我们可以用。get_list()来得到其中的文本
# for i in range (0,len(t_list)):                   #据此设计循环，遍历列表中的每一个元素，获取其文本
#     print(t_list[i].get_text())                   #html中的注释内容无法被识别为文本会被略过  例如：<!--新闻1-->就不会被认出来。
