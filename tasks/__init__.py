from files import CONFIG_LOCATION
from pyperclip import copy
import json
import time


#  显示任务
def show_task(key=None):
    with open(CONFIG_LOCATION, 'r') as task_file:
        index = 0
        for line in task_file.readlines():
            index = index + 1
            text = json.loads(line)['text']
            if key is None:
                print("\033[31m %d %s \033[0m" % (index, text.strip("\n")))
            elif key is not None and key in text:
                print("\033[31m %d %s \033[0m" % (index, text.strip("\n")))


# 新增任务
def add_task(record):
    with open(CONFIG_LOCATION, 'a+') as task_file:
        record = {
            "text": record,
            "step": 1,
            "date": time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()),
            "status": "NORMAL"
        }
        task_file.write(json.dumps(record))
        task_file.write("\n")


#  删除指定任务
def delete_task(index):
    #  将文件读入内存
    read_file = open(CONFIG_LOCATION, 'r')
    lines = read_file.readlines()

    #  检查序号，不写入此索引
    with open(CONFIG_LOCATION, 'w') as write_file:
        count = 0
        for i in lines:
            count = count + 1
            if count != index:
                write_file.write(i)
    read_file.close()


#  拷贝任务详情到剪切板
def copy_task(index):
    #  检查序号，不写入此索引
    with open(CONFIG_LOCATION, 'r') as file:
        count = 0
        for i in file.readlines():
            count = count + 1
            if count == index:
                copy(json.loads(i)['text'])
                break
