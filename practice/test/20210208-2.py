# -*- coding: utf-8 -*-

# @Project:   sky_projects
# @Time:      2021-02-08 15:13
# @Author  :    TianQing Chen
# @File    :    20210208-2.py
# @function :   class

"""
class Student(object):
    def __init__(self,name,id):
        self.name = name
        self.id =  id

    def score(self):
        self.core = 3
        print(self.name,self.id)
        return self.core

student1 = Student("张三",23)
student1.score()
"""

class Box(object):
    def __init__(self,width,height,depth):
        self.width = width
        self.height = height
        self.depth = depth

    def getVolume(self):
        return self.width * self.height * self.depth

box_a = Box(3,4,5)
print(box_a.getVolume())