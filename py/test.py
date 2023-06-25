from selenium import webdriver
 

b = webdriver.Chrome()
url = "https://www.baidu.com/"
b.get(url)
 

# 关闭当前标签页（第一页）
# b.close()