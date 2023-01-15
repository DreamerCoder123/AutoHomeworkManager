# 首先读取all.json中的数据
import json
import time
import os


def avg(array):
    total = 0
    for i in range(0, len(array)):
        total += array[i]
    return total/len(array)


def EncodeTime(times):
    hours = int(times/3600)
    min = int((times-hours*3600)/60)
    second = times-hours*3600-min*60
    return str(hours)+"时"+str(min)+"分"+str(second)+"秒"


def writeIn(info):
    files = open("all.json", mode="w")  # 以写入模式打开文件
    files.write(info)
    files.close()


time_cost = []
file = open("all.json")
currentData = json.loads(file.read())
file.close()
print("从文件中读取的数据：")
for i in range(0, len(currentData)):
    print(currentData[i]['content'], "剩余:",
          currentData[i]['page'], "序号：[", i, "]")

currentTracking = int(input("请输入序号"))

pages = currentData[currentTracking]['page']
while True:
    time_start = time.time()
    print("请专注....\n此面写完后请按下此按钮")
    os.system("pause")
    pages -= 1
    # 将更新的数据写入all.json
    currentData[currentTracking]['page'] = pages
    writeIn(str(json.dumps(currentData, ensure_ascii=False)))
    # 写入完毕
    # 判断pages的值
    if pages <= 0:
        print("当前科目作业已经完成！")
        exit()
    # 判断完毕
    time_end = time.time()
    time_cost.append(time_end-time_start)
    print("这一面花费的时间为", EncodeTime(round(time_end-time_start, 2)), "\n预计需要",
          EncodeTime(avg(time_cost)*currentData[currentTracking]['page']), "还剩余：", pages)
    time.sleep(1)
    os.system("cls")
