import requests
import zmail
import time
url = "https://v2.alapi.cn/api/zaobao"

payload = "token=7XzYphnEf5YENgaq"
headers = {'Content-Type': "application/x-www-form-urlencoded"}
server = zmail.server('chatgptemailbot@163.com', 'JHUVKNEFDASRQBZF')
while(True):
    
    print(time.strftime('%H:%M', time.localtime()))
    if("07:00"==time.strftime('%M', time.localtime())):
        response = requests.request("POST", url, data=payload, headers=headers)
        tmp = response.json()
        content_text =""
        for i in tmp['data']['news']:
            content_text = content_text+i+'\n'
        content_text=content_text+"\n"+tmp['data']['date']
        subject="每日60秒早报"
        user="1915141975@qq.com"
        server.send_mail(user, {'subject': subject, 'content_text': content_text})
        time.sleep(120)
    time.sleep(30)
