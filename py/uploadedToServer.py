import subprocess
import time


def doCommand(command):
    try:
        process = subprocess.Popen(command, stdout=subprocess.PIPE, shell=True)
        output, error = process.communicate(timeout=60*30)
        output = output.decode("utf-8")
        time.sleep(10)
        process.terminate()
        process.wait()
        return output
    except Exception as e:
        process.kill()
        f = open("D:/资源/java/forNowCoder/py/uploadedToServer.log", "a+")
        f.write(str(e)+" "+str(e.__traceback__.tb_lineno))
        f.write("\n")
        f.close()
        return 0


def getLocalFiles():
    command = 'e: && cd E:/shareWithPhone && dir'
    tmp = doCommand(command)
    if (tmp != 0):
        tmp = tmp.split("\r\n")
        tmp = tmp[6:-3]
        files = []
        for i in tmp:
            files.append(i[36:])
        return sorted(list(files))
    else:
        return []


def getServerFiles():
    command = 'ssh -p 15328 root@165.3.2.57 "ls /share" '
    files = doCommand(command)
    if (files != 0):
        files = files.split("\n")
        files = files[:-1]
        return sorted(list(files))
    else:
        return []


getServerFiles()
while (True):
    f = open("D:/资源/java/forNowCoder/py/uploadedToServer.log", "a+")
    f.write(str(time.strftime('%D %H:%M:%S', time.localtime())))
    f.write("\n")

    localFiles = getLocalFiles()
    f.write(str(localFiles))
    f.write("\n")

    serverFiles = getServerFiles()
    f.write(str(serverFiles))
    f.write("\n")

    strLocalFiles = "".join(localFiles)
    strServerFiles = "".join(serverFiles)

    if (strLocalFiles != strServerFiles):
        needRm = []
        needScp = []
        rmCmd = 'ssh -p 15328 root@165.3.2.57 "rm -rf '
        scpCmd = "scp -P 15328 -r "

        for i in serverFiles:
            if i not in localFiles:
                needRm.append("/share/"+i)
        for i in localFiles:
            if i not in serverFiles:
                needScp.append("E:/shareWithPhone/"+i)
        for i in needRm:
            rmCmd = rmCmd+" '"+i+"' "
        rmCmd = rmCmd+'"'
        for i in needScp:
            scpCmd = scpCmd+' "'+i+'" '
        scpCmd = scpCmd+" root@165.3.2.57:/share"

        if len(needRm) != 0:
            doCommand(rmCmd)
            f.write(rmCmd)
            f.write("\n")

        if len(needScp) != 0:
            doCommand(scpCmd)
            f.write(scpCmd)
            f.write("\n")

    f.write("--------\n")
    f.close()
    time.sleep(60*10)


# mkdir /data/data/com.termux/files/home/storage/downloads/share
# scp -P 15328 -r  root@165.3.2.57:/share/* /data/data/com.termux/files/home/storage/downloads/share
