import re
"""
正则表达式-->用一个标准来筛出符合规则的字符串
"""

#re.compile 封装一个正则表达式的对象 
# pat = re.compile("AA")                            #re.compile 封装一个正则表达式的对象
# m = pat.search("CBA")                             #以pat为规则在"CBA"中搜索
# m = pat.search("aACBAA")                          #python中的区间一般左闭右开
# m = pat.search("BAAABB")                          #只搜索第一个满足条件的

#没有模式对象
# m = re.search("asd","ABEasd")                     #re.search("目标内容","搜索范围")
# print(m)

# print(re.findall("aa","ASFaaDSAsgdaFSaa"))        #re.findall("目标内容","搜索范围")
# print(re.findall("[A-Z]","ASFaaDSAsgdaFSaa"))     #单独找出所有的大写字母
# print(re.findall("[A-Z]+","ASFaaDSAsgdaFSaa"))    #加了一个'+'表示前一个字符的多次扩展


#sub-->查找替换
# print(re.sub("a","A","abcABC"))                   #吧'a'替换为'A'，范围是"abcABC"，并将结果输出
"""
建议在正则表达式中，在被比较的字符串前面加上r-->防止转义字符生效
"""