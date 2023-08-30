
import os
import openai

key = os.environ['ChatGPTkey']
thisPath=os.environ['myCodeNexusPath'].replace('\\','/')+'/py/englishVoiceChatRobot'

class ChatGPT():
    userSay = ''
    assistantContent = ''
    systemContent = ''
    needTokens=False
    messages= ''
    def __init__(self,userSay = '',assistantContent = '',systemContent = ''):
        self.userSay=userSay
        self.assistantContent=assistantContent
        self.systemContent=systemContent
        

    def reply(self, userSay='',needTokens=False,messages= ''):
        self.needTokens=needTokens
        self.messages=messages
        openai.api_key = key
        if self.messages=='':
            self.messages=[
                {"role": "system", "content": self.systemContent},
                {"role": "user", "content": userSay},
                {"role": "assistant", "content": self.assistantContent},
            ]

        response = openai.ChatCompletion.create(
            # model="gpt-3.5-turbo",
            model='gpt-3.5-turbo-16k-0613',
            messages=self.messages
        )

        chatgptSay = response['choices'][0]['message']['content']
        if self.needTokens:
            re={'text':chatgptSay,'tokens':response['usage']['total_tokens']}
            
            return re
        else:
            return chatgptSay


class ChatGPTtoFile(ChatGPT):
    fileName = "chatHistory"

    def __init__(self, fn=fileName, language='中文'):
        import json
        
        self.fileName =thisPath+'/json/'+ str(fn) + '.json'
        self.messages=[]
        
        with open(self.fileName, "a+", encoding='utf-8') as f:
            f.close()
        with open(self.fileName, "r+", encoding='utf-8') as f:
            content = f.read()
            if content!='':
                self.messages=json.loads(content)
            else:
                self.messages.append({"role": "system", "content": '你始终使用'+language})
            f.close()

    def reply(self, userSay):
        import openai
        import json

        openai.api_key = key
        self.messages.append({"role": "user", "content": userSay})
        reply=super().reply(messages=self.messages,needTokens=True)
        chatgptSay=reply['text']
        tokens=reply['tokens']
        self.messages.append({"role": "assistant", "content": chatgptSay})

        if tokens > 12000:
            num=(len(self.messages)-1)//2//2
            tmp=[]
            for i in range(num):
                tmp.append(self.messages.pop(1))
            with open(self.fileName+'.bk', "a+", encoding='utf-8') as f:
                f.write(json.dumps(tmp))
                f.close()

        with open(self.fileName, "w+", encoding='utf-8') as f:
            f.write(json.dumps(self.messages))
            f.close()
        return chatgptSay


class ChatGPTBot(ChatGPTtoFile):

    def start(self):
        print('当你输入"exit"时,即退出')
        while True:
            userSay = input(">>请输入:\n")
            if userSay == 'exit':
                print('bye~')
                break
            print(self.reply(userSay))

