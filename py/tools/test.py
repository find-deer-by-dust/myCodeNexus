
import pyttsx3
from  ChatGPT import ChatGPT
import whisper
import sounddevice as sd
from scipy.io.wavfile import write

import keyboard

fs = 44100  # Sample rate
seconds = 20  # Duration of recording

print('开始了')

myrecording = sd.rec(int(seconds * fs), samplerate=fs, channels=2)
sd.wait()  # Wait until recording is finished
write('D:/资源/java/myCodeNexus/py/englishVoiceChatRobot/output.wav', fs, myrecording) 


print('录完了')
 # Save as WAV file 


pp = pyttsx3.init()
c=ChatGPT()
pp.setProperty('gender','female')
pp.setProperty('rate', 150)
model = whisper.load_model("medium")

result = model.transcribe('D:/资源/java/myCodeNexus/py/englishVoiceChatRobot/output.wav')
print(result["text"])

say=c.reply(result["text"])
print(say)
pp.say(say)
pp.runAndWait()
pp.stop()