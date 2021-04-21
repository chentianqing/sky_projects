# -*- coding: utf-8 -*-

# @Project:   sky_projects
# @Time:      2021-04-15 15:36
# @Author  :    TianQing Chen
# @File    :    20210415.py
# @function :   please note~


# 1重复元素判定,set() 函数来移除所有重复元素
def all_unique(lst):
    return len(lst) == len(set(lst))

x = [1,1,2,2,3,2,3,4,5,6]
y = [1,2,3,4,5]

print("No.1 result --%s" %set(x))
print(all_unique(x))
print(all_unique(y))


# 2字符元素组成判定
from collections import Counter
def anagram(first,second):
    return Counter(first) == Counter(second)
print("No.2 result -- %s" %anagram("abcd3","3ac5d"))

# 3,内节内存占用
import sys
variable = 380980800
print("No.3 result -- {}".format(sys.getsizeof(variable)))

#检查字符串占用的字节数
def byte_size(string):
    return(len(string.encode( "utf-8" )))
print(byte_size("No.4 result : {}".format("hello")))


#5,打印N次
n = 2
s = "my hello "
print(s * n)


#6,使用 title() 方法，从而大写字符串中每一个单词的首字母。
name = "my name is tqchen"
print(name.title())


#7

#8,这个方法可以将布尔型的值去掉，例如（False，None，0，“”），它使用 filter() 函数。
def compact(lst):
    return list(filter(bool,lst))
print(compact([0,1,False,23,"tqchen"]))


# 9,如下代码段可以将打包好的成对列表解开成两组不同的元组
#  nt a,b,c,d,e,f
array = [[ 1,2 ],[3,4],[5,6]]
transposed = zip(*array)
print(transposed)

# 12,元音统计
import re
# def count_vowels(str):
#     # return len(re.findall(re,[aefsfd],str,re.IGNORECASE))
# count_vowels( "foobar")


# 21,我们常用 For 循环来遍历某个列表，同样我们也能枚举列表的索引与值。
list = ["a","b","c","d","a"]
print(enumerate(list))
for index,count in enumerate(list):
    print("value",count,"Index",index)

# 22,如下代码块可以用来计算执行特定代码所花费的时间
import time
start_time = time.time()
def sum_22(a,b):
    return a + b
sum_22(12121212121,323232323)
end_time = time.time()
print("use time: {}".format(end_time - start_time))


# 23,error catch
try:
    file = open("20210417","r")
    # file.write("This is a test file . try excep")
except IOError:
    print("Error: 没有该文件，需要先创建文件")
else:
    print("文件写入成功")
    file.close()


