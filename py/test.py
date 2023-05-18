import nltk
from nltk import *
from nltk.corpus import PlaintextCorpusReader
from collections import Counter
import matplotlib as mpl
import matplotlib.pyplot as plt
import re
import jieba
from matplotlib.font_manager import FontManager
import subprocess

with open(r'D:\资源\java\forNowCoder\py\data\金庸-神雕侠侣.txt', 'r') as f:
    str = f.read()

print(str.count("小龙女"))
print(str.count('杨过'))
print(str.count('雕'))
print(str.count('侠'))

print(str[5394:6008])

fdist = FreqDist(str)
print(fdist.most_common(30))


W = Counter(str)
# 查询词频在0~100的词量
print(len([w for w in W.values() if w < 100]))
# 查询词频在100~1000的词量
print(len([w for w in W.values() if w > 100 and w < 1000]))
# 查询词频在1000~5000的词量
print(len([w for w in W.values() if w > 1000 and w < 5000]))
# 查询词频在5000以上的词量
print(len([w for w in W.values() if w > 5000]))



cleaned_data = ''.join(re.findall('[\u4e00-\u9fa5]', str)) 
wordlist = jieba.lcut(cleaned_data) 
text = nltk.Text(wordlist) 
text.concordance(word='杨过', width=60, lines=6)
print()
text.similar(word='李莫愁', num=10)


mpl.rc("font",family='DengXian')
mpl.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['font.sans-serif'] = ['SimHei']
words=['小龙女', '杨过', '郭靖', '黄蓉']
nltk.draw.dispersion.dispersion_plot(text, words, title='词汇离散图')