from bs4 import BeautifulSoup
import feedparser
from ChatGPT import *

url='https://36kr.com/feed-newsflash'
chat=ChatGPT()
rss = feedparser.parse(url)

text=''
for i in rss['entries']:
        soup = BeautifulSoup(i['summary'],'html.parser')
        textCopy=text
        text=text+i['title']+'\n'+soup.get_text()+'\n\n'
        if(len(text)>3000):
                text=textCopy
                break

print(text)
botSay=chat.reply('这是今天的最新快讯,说说你的看法,你的看法需要有政策性，针对性和准确性；在有限的篇幅中，主要靠独特的见解吸引读者；立意新颖，论述精当，文采斐然；主要面向广大群众\n'+text)
print(botSay)