def f():
    s=input()
    l=len(s)
    if(eval(s.replace('=','=='))):
        print("Yes")
        return 1
    for j in range(10):
        for ii in range(l+1):
            news=s[0:ii]+str(j)+s[ii:]
            try:    
                if(eval(news.replace('=','=='))):
                    print("Yes")
                    return 1
            except(SyntaxError):
                l=l
    print("No")

t=int(input())
for i in range(t):
    f()


# print(eval('016==1+2*3'))
"""
6
16=1+2*3
7*8*9=54
1+1=1+22
4*6=22+2
15+7=1+2
11+1=1+5

"""