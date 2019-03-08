
## 说明

TaskSelf 是一款运行在Unix系统中的任务管理工具，它可是以帮你更好地管理你的资料和临时数据

其基于Python3 开发，目前支持以下功能:

## 技术栈
+ Python 3.7
+ PyInstaller 
+ PyPerClip
+ ArgParse



## 功能

### 新增任务

> task -a 'content'

```bash
# ./task -a '新增测试任务 && 提高系统的并发数 && 修复3个bug并新增200个BUG'
```

### 搜索任务

> task -s 'searchKey'

```bash
# ./task -s '测试'
 1 新增测试任务 && 提高系统的并发数 && 修复3个bug并新增200个BUG
```

### 删除任务
> task -d index

```bash
./task -d 1
```

### 拷贝任务

> task -c index

```bash
./task -c 1
```

## 使用
下载编译好的文件放置与系统的PATH目录中即可


目前正处于开发中，欢迎ISSUSE 