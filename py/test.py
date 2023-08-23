import pyaudio
import wave
import threading
import keyboard

# 设置录音参数
CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100
RECORD_SECONDS = 0  # 初始录制时间为0
OUTPUT_FILENAME = "output.wav"  # 输出文件名

# 创建一个标志用于控制录音线程
recording = threading.Event()
recording.set()  # 设置为True

# 录音线程函数
def record_audio():
    global RECORD_SECONDS
    audio = pyaudio.PyAudio()
    stream = audio.open(
        format=FORMAT,
        channels=CHANNELS,
        rate=RATE,
        input=True,
        frames_per_buffer=CHUNK
    )

    frames = []
    print("开始录音...")
    while recording.is_set():  # 当recording为True时，录音继续
        data = stream.read(CHUNK)
        frames.append(data)
        RECORD_SECONDS += CHUNK / RATE  # 更新录制时间

    stream.stop_stream()
    stream.close()
    audio.terminate()
    print("录音已停止.")

    # 将录制的音频保存到文件
    with wave.open(OUTPUT_FILENAME, "wb") as wf:
        wf.setnchannels(CHANNELS)
        wf.setsampwidth(audio.get_sample_size(FORMAT))
        wf.setframerate(RATE)
        wf.writeframes(b"".join(frames))

# 启动录音线程
recording_thread = threading.Thread(target=record_audio)
recording_thread.start()

# 监测键盘事件，当按下任意键时停止录音
print("按下任意键停止录音...")
keyboard.wait("enter")  # 此处可以更改为任意您想要的按键，"enter"表示回车键
recording.clear()  # 设置recording为False，停止录音

# 等待录音线程结束
recording_thread.join()
