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

        if(len(text)>10000):
                text=textCopy
                break

# print(text)
botSay=chat.reply('这是今天的新闻,说说你的看法,你的看法需要有政策性，针对性和准确性；在有限的篇幅中，主要靠独特的见解吸引读者；立意新颖，论述精当，文采斐然；主要面向广大群众\n'+text)
print(botSay)