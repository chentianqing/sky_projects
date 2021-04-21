# -*- coding: utf-8 -*-

# @Project:   sky_projects
# @Time:      2021-03-01 15:28
# @Author  :    TianQing Chen
# @File    :    20210301.py
# @function :   please note~


# 错误示例
"""
if (a <= 0):
   return
elif (a > b):
   return
else:
  b -= a

# 正确示例
if (transfer_amount <= 0):
   raise Exception('...')
elif (transfer_amount > balance):
   raise Exception('...')
else:
  balance -= transfer_amount
"""


# 错误示例
x = 27
y = 27
print(x == y)

x = 721
y = 721
print(x == y)