import selenium
from selenium import webdriver

options = webdriver.ChromeOptions()
broweser = webdriver.Chrome(options=options)

broweser.get("https://www.baidu.com/")