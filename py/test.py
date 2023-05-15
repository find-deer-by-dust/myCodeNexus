from  ChatGPT import *
chat=ChatGPT()
import requests
import zmail
import time
url = "https://v2.alapi.cn/api/zaobao"
server = zmail.server('chatgptemailbot@163.com', 'JHUVKNEFDASRQBZF')
payload = "token=7XzYphnEf5YENgaq"
headers = {'Content-Type': "application/x-www-form-urlencoded"}


response = requests.request("POST", url, data=payload, headers=headers)
tmp = response.json()
content_text =""
for i in tmp['data']['news']:
    content_text = content_text+i[i.find("、")+1:]+'\n\n'

print(content_text)
# content_text=content_text+"\n"+tmp['data']['date']

# print(chat.reply('我是中国公民,这是今天的新闻,我需要你整合这些内容并给出一段新闻评论'+content_text))
subject="每日60秒早报"
user="1915141975@qq.com"
server.send_mail(user, {'subject': subject, 'content_text': content_text})