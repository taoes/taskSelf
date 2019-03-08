import os

CONFIG_LOCATION = os.path.expandvars("$HOME") + "/.task_list"


#  初始化文件
def init():
    if not os.path.exists(CONFIG_LOCATION):
        os.system("touch %s" % CONFIG_LOCATION)
        print("配置文件初始化完成")
