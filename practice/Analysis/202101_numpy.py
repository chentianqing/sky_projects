# -*- coding: utf-8 -*-

# @Project:   sky_projects
# @Time:      2021-01-21 12:35
# @Author  :    chentianqing
# @File    :    202101_numpy.py

import numpy

s = {1,3,4}
print(s)
s.add(5)
print(s)
id = 30020
name = "chentianqing"
print('no data available for person with id: %s, name: %s' % (id, name))


list = [1,2,34,23,4,9]
list.sort()
# dist = {1:222,3:233}
# print(dist[1])
print(list)



import json

params = {
    "symbol":'1232',
    "type":"limit",
    "price":122.1,
    "amount":23,
}
params_str = json.dumps(params)
print(params_str)




attributes = ['name', 'dob', 'gender']
values = [['jason', '2000-01-01', 'male'],
['mike', '1999-01-01', 'male'],
['nancy', '2001-02-01', 'female']
]

# # expected output:
# [{'name': 'jason', 'dob': '2000-01-01', 'gender': 'male'},
# {'name': 'mike', 'dob': '1999-01-01', 'gender': 'male'},
# {'name': 'nancy', 'dob': '2001-02-01', 'gender': 'female'}]

list = []
for value in values:
    d = {}
    for i in range(3):
        d[attributes[i]] = value[i]
        print(i)
        print(d)
    list.append(d)
# print(list)


try:
    s = 0  10
    print(s)
except ValueError as err:
    print(err)