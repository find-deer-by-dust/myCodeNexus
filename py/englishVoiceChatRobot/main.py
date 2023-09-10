
from ChatGPT import ChatGPTtoFile
import os
from playsound import playsound
from ChatGPT import ChatGPT
import sounddevice as sd
from scipy.io.wavfile import write


thisPath=os.environ['myCodeNexusPath'].replace('\\','/')+'/py/englishVoiceChatRobot'
outputPath=thisPath+'/wav/output.wav'
inputPath=thisPath+'/wav/input.wav'
tmpPath=thisPath+'/tmp.txt'

fs = 44100  # Sample rate
seconds = 10  # Duration of recording

def getText():
    os.system("python "+thisPath+'/makeText.py')
    with open(tmpPath, "r+", encoding='utf-8') as f:
        re=f.read()
        f.close()
    return re

def makeWav():
    os.system("python "+thisPath+'/makeWav.py')

for i in [outputPath,inputPath,tmpPath]:
    with open(i, "a+") as f:
        f.close()

while True:
    seconds=int(input('多少秒捏?\n'))
    print('开始了')
    myRecording = sd.rec(int(seconds * fs), samplerate=fs, channels=2)
    sd.wait()  # Wait until recording is finished
    write(inputPath, fs, myRecording) 
    print('录完了') # Save as WAV file 

    text=getText()
    print(text)

    GPT=ChatGPTtoFile(fn='lcy',messages={"role": "system", "content": '你始终使用英语,你作为用户的英语学习伙伴,你需要陪用户进行日常聊天交流.只有当用户句子有语法或者表达错误时,你才需要指出用户的错误,无需在意用户的符号错误'})

    say=GPT.reply(text)
    with open(tmpPath, "w+", encoding='utf-8') as f:
        f.write(say)
        f.close()

    makeWav()
    
    playsound(outputPath)
    print(say)



