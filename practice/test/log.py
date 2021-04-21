# -*- coding: utf-8 -*-

# @Project:   sky_projects
# @Time:      2021-02-07 23:40
# @Author  :    TianQing Chen
# @File    :    log.py
# @function :   please note~

def printLog(func):
    def log():
        print("this is a log,write it")
        func()
    return log


def server1():
    print("server1 log")

@printLog
def server2():
    print("server2 log")

server1 = printLog(server1)
server1()
server2()