import json
import time

def writeIn(Message, filePath):
    file = open(filePath, mode="w", encoding="utf-8")
    file.write(Message)
    file.close()


def readCurrentSub():
    try:
        file = open("./all.json", mode="r")
        file = json.loads(file.read())
    except:
        print("检测到all.json配置出现问题,正在重置中")
        ori = '[{"content": "chi", "page": 0}]'
        writeIn(ori, "all.json")


def waitUserInput(hintmessage, ChooseArray):
    if len(ChooseArray) != 0:
        print(hintmessage)
        for x in range(0,len(ChooseArray)):
            print(ChooseArray[x],end=',')
        user_input=input("\n请选择...\n")
        if user_input in ChooseArray :
            return user_input
        else:
            print("非法输入")
            time.sleep(2)
            exit()

waitUserInput("你好啊",["1","2","3","4"])
readCurrentSub()
