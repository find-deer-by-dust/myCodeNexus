import whisper
import os


thisPath=os.environ['myCodeNexusPath'].replace('\\','/')+'/py/englishVoiceChatRobot'
outputPath=thisPath+'/wav/output.wav'
inputPath=thisPath+'/wav/input.wav'
tmpPath=thisPath+'/tmp.txt'

model = whisper.load_model("medium.en")
result = model.transcribe(inputPath)
# print(result["text"])
with open(tmpPath, "w+", encoding='utf-8') as f:
    f.write(result["text"])
    f.close()