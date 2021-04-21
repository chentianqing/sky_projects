# -*- coding: utf-8 -*-

# @Project:   sky_projects
# @Time:      2021-02-23 11:05
# @Author  :    TianQing Chen
# @File    :    memory.py
# @function :   please note~

import os
import psutil

def show_memory_info(hint):
    pid = os.getpid()
    p = psutil.Process(pid)

    info = p.memory_full_info()
    memory1 = info.uss / 1024 /1024
    print("{} memory used: {} MB".format(hint,memory1))



def func():
    show_memory_info("initial")
    a = [i for i in range(1000)]
    show_memory_info("after a created")
#
# func()
# show_memory_info('finished')

# print(psutil.Process(os.getpid()))

p = psutil.cpu_stats()
print(p)
print(p.interrupts)