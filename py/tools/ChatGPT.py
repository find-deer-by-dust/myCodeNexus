import datetime

key = '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'


class ChatGPT():
    userSay = ''
    assistantContent = ''
    systemContent = ''
    userSayEx = ''
    chatgptSay = ''

    def reply(self, userSay):
        import openai
        import time
        # timeStart = time.perf_counter()
        openai.api_key = key
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": self.systemContent},
                {"role": "user", "content": self.userSayEx + userSay},
                {"role": "assistant", "content": self.assistantContent},
            ]
        )
        chatgptSay = self.chatgptSay + \
            response['choices'][0]['message']['content']
        # timeEnd = time.perf_counter()
        # return chatgptSay + '\n\t\t--耗时 ' + str(round(timeEnd - timeStart, 3)) + 's'
        return chatgptSay+'\n'


class ChatGPTCompression(ChatGPT):
    def __init__(self):
        self.systemContent = '你需要把接受的对话内容简洁化,其中关于双方的个人信息必须保留,' \
                             '必须保留原意,' \
                             '在满足以上条件后尽可能简洁,' \
                             '回复优化后的对话内容'
        self.assistantContent = self.systemContent + ''


class ChatGPTReserveOrNot(ChatGPT):
    def __init__(self):
        self.systemContent = "你先回复'是'或者'否'" \
                             "给你一段对话,是用户即我与ChatGPT即你的聊天,其中用户是A,ChatGPT是B," \
                             "你判断这段对话是否有必要保留在本地." \
                             "判断的依据包括" \
                             "会影响未来ChatGPT对用户的回答," \
                             "会导致在今后的对话中ChatGPT可以更个性化地对待用户," \
                             "会提供有价值的信息," \
                             "包含用户信息"
        self.assistantContent = self.systemContent + ''


class ChatGPTRwFile(ChatGPT):
    fileName = "Chat_History"

    def __init__(self, fn=fileName):
        self.fileName = str(fn) + '.txt'
        self.systemContent = '当你接收到我给你发的聊天记录后,你只需要依据历史聊天记录和当前对你的提问,做出回应就够了'
        with open(self.fileName, "a+", encoding='utf-8') as f:
            1
        with open(self.fileName, "r+", encoding='utf-8') as f:
            tmp = f.read()
            if tmp == '':
                tmp = "A:\nB:"
                f.write(tmp)
            tmp = f.read()
            f.close()

    def reply(self, userSay):
        import openai
        import time
        timeStart = time.perf_counter()
        openai.api_key = key

        with open(self.fileName, "r+", encoding='utf-8') as f:
            tmp = f.read()
            f.close()
        self.assistantContent = '这是你和用户的历史聊天记录,你是A,用户是B\n' + tmp + '\nA:' + userSay

        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": self.systemContent},
                {"role": "user", "content": self.userSayEx + userSay},
                {"role": "assistant", "content": self.assistantContent},
            ]
        )
        chatgptSayNotReplace = response['choices'][0]['message']['content'].replace(
            'B:', '').replace('A:', '')
        chatgptSay = chatgptSayNotReplace.replace("\n", '').replace(' ', '')

        if ChatGPTReserveOrNot().reply('A:' + userSay + '\nB:' + chatgptSay)[0] == '是':
            tmp = tmp + "\nA:" + userSay + "\nB:" + chatgptSay
        if response['usage']['total_tokens'] > 3000:
            AList = []
            fn = self.fileName + str(datetime.date.today()).replace('-', '.')
            with open(fn, "a+", encoding='utf-8') as f:
                f.write(tmp)
                f.close()
            for i in range(len(tmp)):
                if tmp[i] == 'A' and tmp[i + 1] == ':':
                    AList.append(i)

            x = len(AList)
            for i in range(x - 1):
                if i % 2 == 1:
                    tmp2 = tmp[AList[i]:AList[i + 1]]
                    tmp = tmp.replace(tmp2, '^' * len(tmp2))
            tmp = tmp.replace('^', '')
            tmp = ChatGPTCompression().reply(tmp)
            chatgptSay = '##目前云端历史聊天记录过多,已停止加载部分聊天记录,因此可以会忘记部分信息,请见谅,但云端依然有保存.\n' + chatgptSay
        with open(self.fileName, "w+", encoding='utf-8') as f:
            f.write(tmp)
            f.close()
        timeEnd = time.perf_counter()
        return chatgptSayNotReplace + '\n\t\t--耗时 ' + str(round(timeEnd - timeStart, 3)) + 's'


class ChatGPTBot(ChatGPTRwFile):

    def start(self):
        print('当你输入"exit"时,即退出')
        while True:
            userSay = input(">>请输入:\n")
            if userSay == 'exit':
                print('bye~')
                break
            print(self.reply(userSay))


class CatChatGPTBot(ChatGPTBot):
    fileName = "CatChatGPTBot"

    def __init__(self, fn=fileName):
        super(CatChatGPTBot, self).__init__(fn)
        self.systemContent = '我们来玩cosplay,你现在是一个喜欢吃鱼的傲娇的猫娘,你的一切回答都从你是一个猫娘出发,' \
                             '你以后说话不要说自己作为一个语言模型,你现在应该彻底扮演cosplay的角色,' \
                             '而我就是你的主人'
