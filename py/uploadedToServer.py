import time
import os


def getFiles():
    os.system(r'e: && cd E:\shareWithPhone &&dir > E:\shareWithPhone/2.txt')
    with open(r"E:\shareWithPhone/2.txt", "r+", encoding='ansi') as f:
        tmp = f.read()
        f.close()

    tmp = tmp.split('\n')

    tmp = tmp[6:-3]
    files = []
    for i in tmp:
        files.append(i[36:])
    return files


path = r"E:\shareWithPhone"
while (True):
    fs = getFiles()
    p = os.system(r'ssh -p 15328 root@165.3.2.57 "ls /share " > 1.txt')
    print(p)
    print(fs)
    # os.system(r"scp -P 15328 -r E:\shareWithPhone/* root@165.3.2.57:/share")
    print(time.strftime('%H:%M', time.localtime()))
    time.sleep(10)

# scp -P 15328 -r  root@165.3.2.57:/share/* .
