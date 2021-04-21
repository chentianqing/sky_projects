# -*- coding: utf-8 -*-

# @Project:   sky_projects
# @Time:      2021-02-08 00:02
# @Author  :    TianQing Chen
# @File    :    log1.py
# @function :   装饰器
def printlog2(func):
    def log2():
        print("print log2")
        func()
    return log2


def printlog(func):
    def log(self,*args,**kwargs):
        print("print log:{}".format(self,*args))
        func(self,*args,**kwargs)
    return log

# @printlog2
@printlog
def server1(a):
    print("server1:{}".format(a))
    # print("print log")
    # printlog()


@printlog
def server2():
    print("server2")
    # print("print log")
    # printlog()


# server2()
server1(222)