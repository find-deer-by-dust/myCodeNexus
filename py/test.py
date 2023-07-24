from  ChatGPT import *
import requests
import zmail
import time
import os


chat=ChatGPT()
url = "https://v2.alapi.cn/api/zaobao"
emailKey=os.environ['emailKey']
server = zmail.server('chatgptemailbot@163.com', emailKey)
payload = "token=7XzYphnEf5YENgaq"
headers = {'Content-Type': "application/x-www-form-urlencoded"}
users=["1915141975@qq.com"]
myCodeNexusPath=os.environ['myCodeNexusPath']
# users=["3350325473@qq.com","1915141975@qq.com","2609446429@qq.com"]

while(True):
    with open(myCodeNexusPath+'/py/tools/hadSent.log', "r+", encoding='utf-8') as f:
        days = f.read()
        f.close()
    
    hour=int(time.strftime('%H', time.localtime()))
    today=time.strftime('%Y-%m-%d', time.localtime())
    if(hour > 8 and today not in days): 
        ssh = os.popen("ssh 192.168.0.104").read()

        response = requests.request("POST", url, data=payload, headers=headers)
        tmp = response.json()
        content_text =""
        for i in tmp['data']['news']:
            content_text = content_text+i[i.find("、")+1:]+'\n\n'
        
        try:
            botSay=chat.reply('这是今天的新闻,说说你的看法,你的看法需要有政策性，针对性和准确性；在有限的篇幅中，主要靠独特的见解吸引读者；立意新颖，论述精当，文采斐然；主要面向广大群众\n'+content_text)
            separator='\n------我是分割线------\n'
            content_text="ChatGPT的看法:\n"+botSay+separator+"\n原新闻:\n"+content_text
        except:
            content_text=content_text
        
        if 'Connection timed out'  not in ssh :
            content_text='nokia8正常工作中~\n\n'+content_text
        else:
            content_text='!!!手机没开机!!!\n!!!!\n\n'+content_text
        
        subject="每日60秒新闻 "+tmp['data']['date']

        for user in users:
            print("have sent email to " + user)
            server.send_mail(user, {'subject': subject,'content_text': content_text})
            with open(myCodeNexusPath+'/py/tools/hadSent.log', "a+", encoding='utf-8') as f:
                f.write(time.strftime(today)+'\n')
                f.close()

    else:
        time.sleep(60*60)

    time.sleep(60*30)
