import urllib.request

"""
#获取一个get请求
"""
# response = urllib.request.urlopen("http://www.baidu.com")       #注意http与https有区别
# # print(response)     #输出一个类-->object
# print(response.read().decode('utf-8'))  # .read-->对类进行读取； .decode-->对内容进行解码，默认为utf-8，解码后可以看出HTML结构


"""
http://httpbin.org/  测试用网站
获得一个post请求， post请求可以提交一个表单包含可加密的用户名和密码
"""
# import urllib.parse             #用于封装提交的表单
# #bytes 转换为2进制，encode对内容进行封装(封装内容用{}字典格式)，最后在补上编码格式
# data = bytes(urllib.parse.urlencode({"hello":"world"}),encoding="utf-8")    #hello world 的位置可以用于填写cookie
# respon = urllib.request.urlopen("http://httpbin.org/post",data=data)
# print(respon.read().decode("utf-8"))


"""
获得一个get请求
"""
# try:
#     response1=urllib.request.urlopen("http://httpbin.org/get",timeout=0.2)    #timeout-->相应等待时间，若超时则会报错。用try...catch
#     print(response1.read().decode("utf-8"))
# except urllib.error.URLError as e :
#     print("Time Out")

# response =urllib.request.urlopen("https://movie.douban.com/top250?start=&filter=")      #错误418 ”我是一个茶壶”即被发现是一个爬虫
# print(response.status)

# response =urllib.request.urlopen("http://www.baidu.com")
# print(response.status)
# print(response.getheaders())        #打印头文件
# print(response.getheader("server")) #想要其中一个信息注意去掉s，在括号里用引号引住键

"""
伪装成浏览器
"""
url = "https://music.163.com"
headers={"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.96 Safari/537.36 Edg/88.0.705.56"}
req = urllib.request.Request(url=url,headers=headers)     #封装一个请求
respones = urllib.request.urlopen(req)
print(respones.read().decode("utf-8"))
