from  ChatGPT import *
import requests
import zmail
import time

chat=ChatGPT()
url = "https://v2.alapi.cn/api/zaobao"
server = zmail.server('chatgptemailbot@163.com', 'JHUVKNEFDASRQBZF')
payload = "token=7XzYphnEf5YENgaq"
headers = {'Content-Type': "application/x-www-form-urlencoded"}
users=["3350325473@qq.com","1915141975@qq.com","2609446429@qq.com"]

yesterday=''
while(True):
    
    print(time.strftime('%H:%M', time.localtime()))
    if("07:00"==time.strftime('%H:%M', time.localtime())): 
        response = requests.request("POST", url, data=payload, headers=headers)
        tmp = response.json()
        content_text =""
        for i in tmp['data']['news']:
            content_text = content_text+i[i.find("、")+1:]+'\n\n'

        botSay=chat.reply('这是今天的新闻,说说你的看法,你的看法需要有政策性，针对性和准确性；在有限的篇幅中，主要靠独特的见解吸引读者；立意新颖，论述精当，文采斐然；主要面向广大群众\n'+content_text)
        
        subject="每日60秒新闻 "+tmp['data']['date']
        if yesterday!=tmp['data']['date']:
            yesterday=tmp['data']['date']
            for user in users:
                print("have sent email to " + user)
                separator='\n------我是分割线------\n'
                server.send_mail(user, {'subject': subject, 'content_text': "ChatGPT的看法:\n"+botSay+separator+"\n原新闻:\n"+content_text})
        else:
            time.sleep(60*10)
            
        time.sleep(120)

    time.sleep(30)
