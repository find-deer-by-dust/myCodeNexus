# 1.
# （编程）金额大写转换
# 写一个函数，要求能够将大写的人民币金额转化为数字。示例如下：
# 壹仟贰佰叁拾万零柒拾伍 -〉12300075
# 拾亿零陆佰叁拾伍万零叁佰->1006350300
dic1={
    "壹":1,"贰":2,"叁":3,"肆":4,"伍":5,"陆":6,"柒":7,"捌":8,"玖":9,
}
dic2={
    "拾":10,"佰":100,"仟":1000,
}
dic3={
    "万":10000,"亿":10000000,
}
def capitalRmbIntoDigital(s):
    i=0
    tmp=0
    re=""
    while i<len(s):
        if s[i] in dic1 and i+1<len(s) and s[i+1] in dic2:
            tmp=tmp+dic1[s[i]]*dic2[s[i+1]]
            i=i+1
        elif s[i] in dic1:
            tmp=tmp+dic1[s[i]]
        elif s[i] in dic2 :
            tmp=tmp+dic2[s[i]]
        
        elif s[i] in dic3 :
            tmp2=str(tmp)
            tmp=0
            while len(tmp2)!=4:
                tmp2="0"+tmp2
            re=re+tmp2
        if i==len(s)-1:
            tmp2=str(tmp)
            tmp=0
            while len(tmp2)!=4:
                tmp2="0"+tmp2
            re=re+tmp2
        i=i+1
    return int(re)

print(capitalRmbIntoDigital("壹仟贰佰叁拾万零柒拾伍"))
print(capitalRmbIntoDigital("拾亿零陆佰叁拾伍万零叁佰"))


