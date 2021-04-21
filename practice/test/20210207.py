# -*- coding: utf-8 -*-

# @Project:   sky_projects
# @Time:      2021-02-07 22:49
# @Author  :    TianQing Chen
# @File    :    20210207.py
# @function :   please note~

l = [1,[2,1],23]
l.append(22)
print(l)
#删除index
l.pop(0)
#删除object
l.remove(23)
print(l)


#装饰器
def my_decorator(func):
    def wrapper():
        print("wrapper of decorator")
        func()
    return wrapper

# @my_decorator
def greet():
    print("hi")

greet = my_decorator(greet)
greet()




