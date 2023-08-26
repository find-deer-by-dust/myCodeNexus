
import pyttsx3
from ChatGPT import ChatGPT
import whisper
import sounddevice as sd
import os
from scipy.io.wavfile import write
import keyboard


fs = 44100  # Sample rate
seconds = 10  # Duration of recording

myCodeNexusPath=os.environ['myCodeNexusPath']
wavPath=myCodeNexusPath+'/py/englishVoiceChatRobot/output.wav'

print('开始了')
myRecording = sd.rec(int(seconds * fs), samplerate=fs, channels=2)
sd.wait()  # Wait until recording is finished
write(wavPath, fs, myRecording) 
print('录完了') # Save as WAV file 

model = whisper.load_model("medium")
result = model.transcribe(wavPath)
print(result["text"])


GPT=ChatGPT()
say=GPT.reply(result["text"])
print(say)


pp = pyttsx3.init()
pp.setProperty('gender','female')
pp.setProperty('rate', 150)
pp.say(say)
pp.runAndWait()
pp.stop()