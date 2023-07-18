
import requests
import json
import xmltodict
import nltk
from bs4 import BeautifulSoup
import feedparser
import urllib.request


url='https://36kr.com/feed-newsflash'

rss = feedparser.parse(url)
for i in rss['entries']:
        # print(i['title'])
        # print(i['summary'])
        # print('--')

        text=i['title']
        soup = BeautifulSoup(i['summary'],'html.parser')
        print(text)
        print(soup.get_text())
        print('---')




# j=xml_to_json(str)
# for i in j['rss']['channel']['item']:
#         text=i['title']
#         soup = BeautifulSoup(i['description'],'html.parser')
#         print(text)
#         print(soup.get_text())
#         print('---')