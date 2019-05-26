# txt_to_csv
将弹幕文件从txt转成csv

使用：

下载仓库里的代码，将bilibili-vtuber-danmaku-master放在和代码同一个目录下，运行：

```
python3 txt_to_csv.py
```

结果会存在bilibili-vtuber-danmaku-CSV里.

⚠️注意⚠️

1. 时间轴被转换成了以分钟为单位的数字。例子：
 
    0:37 -> 37

2. 有的弹幕并没有提供UID，默认为：

    UID = 114514

3. 不含任何弹幕的txt文件不会被转换为csv文件
