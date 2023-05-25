
# 最大连续登录天数

# 现有用户登录数据表login data,字段为user id+login dt,求每个用户的最大连续登录天数

# user_id login_dt
# 1001 2021-03-01
# 1001 2021-03-10
# 1001 2021-03-11
# 1001 2021-03-12
# 1002 2021-03-01
# 1002 2021-03-02
# 1002 2021-03-05
# 1003 2021-03-01
import time
import datetime
list=[
    [1001, "2021-03-01"],
    [1001, "2021-03-10"],
    [1001, "2021-03-11"],
    [1001, "2021-03-12"],
    [1002 ,"2021-03-01"],
    [1002, "2021-03-02"],
    [1002, "2021-03-05"],
    [1003 ,"2021-03-01"],
]

users=set()
for i in list:
    users.add(i[0])
for user in users:
    print(user)
    datas=[]
    for j in list:
        if j[0]==user:
            datas.append(j[1])
    datas=sorted(datas)
    tmp=1
    maxNum=1
    for i in range(len(datas)):
        if i+1<len(datas):
            d1 = datetime.datetime.strptime(datas[i], '%Y-%m-%d')
            d2=datetime.datetime.strptime(datas[i+1], '%Y-%m-%d')
            # print(d2-d1)
            # print(str(d2-d1)[0]=="1")
            if str(d2-d1)[0]=="1":
                tmp=tmp+1
                maxNum=max(tmp,maxNum)
            else :
                maxNum=max(tmp,maxNum)
                tmp=1
            maxNum=max(tmp,maxNum)
            # print("tmp:"+str(tmp))
    print(maxNum)