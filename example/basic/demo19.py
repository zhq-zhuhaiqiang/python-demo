#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
实现命令行进度条，带百分比
"""

import sys
import time
# sys.stdout.write("[%s%%|%-100s]" % (100, 100 * ('█')))　　
def progress(n,a):
    m = int(n / a * 100)
    x = int(n / a * 10)
    #只是为了让进度条明显
    time.sleep(0.2)
    #主要用到的是"\r"会每次打印都在本页面的起始位置，end=""不让print换行
    print("\r%s %s%%" %("="*x,m))
for i in range(101):
    progress(i,a=100)
# for i in range(10):
#     print(i)
# for i in range(101):
#     # 清除屏幕
#     sys.stdout.write("\r")

#     # 显示百分比和进度条
#     sys.stdout.write("[%s%%|%-100s]" % (i, i * ('█')))

#     # 从缓存刷入到屏幕
#     # sys.stdout.flush()

#     # 延时0.3秒
#     time.sleep(1)
