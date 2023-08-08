import keyboard
import time

text_list = ['print()', 'name', 'Hello, World!']
typing_speed = 0.1  # 输入代码的速度（以秒为单位）
current_index = 0

def input_text(text):
    for char in text:
        keyboard.write(char)
        time.sleep(typing_speed)

def on_shift_press(event):
    global current_index
    if event.name == 'shift':
        if current_index < len(text_list):
            input_text(text_list[current_index])
            current_index += 1

keyboard.on_press(on_shift_press)
keyboard.wait('esc')