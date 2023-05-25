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


doCommand(
    r'copy "D:\资源\java\forNowCoder\py\uploadedToServer.log" "E:\shareWithPhone\" ')
