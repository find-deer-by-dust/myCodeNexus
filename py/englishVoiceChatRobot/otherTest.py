
import json
messages=[]
messages.append({"role": "system", "content": '你始终使用'})

with open('chatHistory.json', "a+", encoding='utf-8') as f:
    f.close()
with open('chatHistory.json', "r+", encoding='utf-8') as f:
    content = f.read()
    if content!='':
        tmp=json.loads(content)
        for i in tmp:
            messages.append(i)

messages.append({"role": "assistant", "content": 'ea'})
b = json.dumps(messages)
f2 = open('chatHistory.json', 'w')
f2.write(b)
f2.close()
print(messages)
print(len(messages))