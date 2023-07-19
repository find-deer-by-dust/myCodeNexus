from bs4 import BeautifulSoup
import feedparser
from ChatGPT import *

url='https://36kr.com/feed-newsflash'
chat=ChatGPT()
rss = feedparser.parse(url)
text=''

for i in rss['entries']:
        textCopy=text
        text+=i['title']+'\n'

        if '<' in i['summary']:
                soup = BeautifulSoup(i['summary'],'html.parser')        
                text+=soup.get_text()
        else:
                text+=i['summary']
        text+='\n\n'

        if(len(text)>3000):
                text=textCopy
                break

print(text)
botSay=chat.reply('这是今天的新闻,你是一个专业的新闻人,你将所有新闻整合为更短的文章同时不丢失准确性和完整性\n'+text)
print(botSay)