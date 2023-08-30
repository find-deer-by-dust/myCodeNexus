import os
os.environ["CUDA_VISIBLE_DEVICES"] = "0"
os.environ["SUNO_USE_SMALL_MODELS"] = "True"

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

audio_array = generate_audio(text_prompt)

# save audio to disk
write_wav(outputPath, SAMPLE_RATE, audio_array)

