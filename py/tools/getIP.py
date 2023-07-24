import os
a = os.popen("ipconfig")

b = a.read().splitlines()

for i in range(len(b)):
    if '无线局域网适配器 WLAN:' in b[i]:
        ip = b[i+4][b[i+4].find(":")+2:]
        break

f = open("D:/vm/share/ip.txt", "w")
f.write(ip)
f.close()
