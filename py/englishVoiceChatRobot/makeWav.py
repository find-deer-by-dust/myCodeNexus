import os
os.environ["CUDA_VISIBLE_DEVICES"] = "0"
os.environ["SUNO_USE_SMALL_MODELS"] = "True"


from pydub import AudioSegment
from bark import SAMPLE_RATE, generate_audio, preload_models
from scipy.io.wavfile import write as write_wav


thisPath=os.environ['myCodeNexusPath'].replace('\\','/')+'/py/englishVoiceChatRobot'
outputPath=thisPath+'/wav/output.wav'
inputPath=thisPath+'/wav/input.wav'
tmpPath=thisPath+'/tmp.txt'

# download and load all models
# preload_models()

# generate audio from text

with open(tmpPath, "r+", encoding='utf-8') as f:
    text_prompt=f.read()
    f.close()

# audio_array = generate_audio(text_prompt)

# # save audio to disk
# write_wav(outputPath, SAMPLE_RATE, audio_array)

textsTmp=text_prompt.split('. ')

i=1
texts=[]
texts.append(textsTmp[0]+'. ')
while i < len(textsTmp):
    tmp=texts[len(texts)-1]+textsTmp[i]+'. '
    if len(tmp)<200:
        texts[len(texts)-1]=tmp
    else:
        texts.append(textsTmp[i]+'. ')
    i=i+1

num=len(texts)
print('一共 '+str(num)+' 句')
for i in range(num):
    print('正在生成第 '+str(i)+' 句')
    # print(texts[i])
    audio_array = generate_audio(texts[i],history_prompt="v2/en_speaker_9")
    write_wav(thisPath+'/wav/'+str(i), SAMPLE_RATE, audio_array)
    

output= AudioSegment.from_wav(thisPath+'/wav/0')
for i in range(num-1):
    sound = AudioSegment.from_wav(thisPath+'/wav/'+str(i+1))
    output=output+sound
    print('正在处理第 '+str(i+1)+' 句的合成')

output.export(outputPath, format="wav")  # 保存文件