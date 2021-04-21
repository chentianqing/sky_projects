# -*- coding: utf-8 -*-

# @Project:   sky_projects
# @Time:      2021-02-25 11:30
# @Author  :    TianQing Chen
# @File    :    testdb.py
# @function :   please note~



import pymysql

import pymysql

def main():
#创建连接
    conn=pymysql.connect(host='10.211.55.200',port=3306,user='root',passwd='123456',db='itopdb',charset='utf8')
    # 创建游标
    cur=conn.cursor()
    # 执行SQL，并返回收影响行数
    effect_row = cur.execute("show databases;")
    # print(cur.fetchone())
    # # 执行SQL，并返回受影响行数
    # effect_row = cur.execute("update student set Sname='小二' where Sno = '001'")
    print(effect_row)

    # 执行SQL，并返回受影响行数,执行多次
    # effect_row = cur.executemany("insert into student(Sno,Sname) values(%s,%s)", [('006',"老王"),('007','小五')])
    # print(effect_row)
    #提交，不然无法保存新建或者修改的数据
    conn.commit()
    # 关闭游标
    cur.close()
    # 关闭连接
    conn.close()

if __name__== '__main__':
    main()


