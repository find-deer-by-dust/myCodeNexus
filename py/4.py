
import pandas as pd
import random
import math

def getDistance(a, b):
    length = len(a)
    tmp = 0
    for i in range(length):
        tmp = tmp+((a[i]-b[i])**2)
    tmp = tmp**(1/length)
    return tmp


def getMean(a):
    length = len(a)
    tmp = []
    for i in range(length):
        tmp.append(data[a[i]])
    mean = []
    for j in range(len(data[0])):
        sum = 0
        for i in range(length):
            sum = sum+tmp[i][j]
        mean.append(sum)

    for i in range(len(mean)):
        mean[i] = mean[i]/length
    return mean


k = 3
pd.set_option('display.notebook_repr_html', False)

data = pd.read_excel(io="D:\资源\学习\课内学习资料\大三下\数据挖掘\实验\实验4 聚类数据.xls")

data = data.values.tolist()
# print(data)

for i in range(len(data[0])):
    maxIndex = data[0][i]
    for j in range(len(data)):
        if data[j][i] > maxIndex:
            maxIndex = data[j][i]
    tmp = len(str(int(maxIndex)))
    for j in range(len(data)):
        data[j][i] = data[j][i]/(10**tmp)

print("数据预处理结果:")
for i in data:
    print(i)

tmp = list(range(len(data)))

random.shuffle(tmp)
result = []
used = []
for i in range(k):
    tmp1 = []
    tmp1.append(tmp[i])
    used.append(tmp[i])
    result.append(tmp1)
# print(used)
# print(result)

for i in range(len(data)):
    if i not in used:
        used.append(i)
        minIndex = 0
        for j in range(k):
            mean = getMean(result[j])
            if (mean < getMean(result[minIndex])):
                minIndex = j
        result[minIndex].append(i)
    
print("k均值聚类结果:")
print(result)


result=[]
for i in range(len(data)):
    tmp=[]
    tmp.append(i)
    result.append(tmp)


while len(result)!=k:
    # print(result)
    means=[]
    for i in result:
        means.append(getMean(i))
    minIndex=[0,1]
    for i in range(len(result)):
        for j in range(len(result)):
            if(i!=j):
                tmp=getDistance(means[i],means[j])
                if(tmp<getDistance(means[minIndex[0]],means[minIndex[1]])):
                    minIndex[0]=i
                    minIndex[1]=j
    # print(minIndex)
    needAdd=result[minIndex[0]]+result[minIndex[1]]
    result.pop(max(minIndex[0],minIndex[1]))
    result.pop(min(minIndex[0],minIndex[1]))
    result.append(needAdd)

print("凝聚式层次聚类结果:")
print(result)
