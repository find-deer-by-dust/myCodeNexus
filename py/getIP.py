import os
a = os.popen("ipconfig")

b = a.read().splitlines()

tmp = b[51].find(":")
ip = b[51][tmp+2:]

f = open("D:/vm/share/ip.txt", "w")
f.write(ip)
f.close()
