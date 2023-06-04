import itertools as its
import datetime

# 记录程序运行时间
start = datetime.datetime.now()
words = '0123456789qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'  # 大小写字母 + 数字 组合
# words = '0123456789' # 纯数字
# 生成密码的位数
r = its.product(words, repeat=8)  # 即生成8位密码，正常情况下热点密码位数为8
dic = open(r"D:\资源\java\forNowCoder\py\AlphabetPass.txt", 'a')  # alphabetPass.txt 是密码本名称
for i in r:
    dic.write(''.join(i))
    dic.write(''.join('\n'))
    print(i)

dic.close()
print('密码本生成好了')
end = datetime.datetime.now()
print("生成密码本一共用了多长时间：{}".format(end - start))
