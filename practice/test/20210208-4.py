# -*- coding: utf-8 -*-

# @Project:   sky_projects
# @Time:      2021-02-08 22:44
# @Author  :    TianQing Chen
# @File    :    20210208-4.py
# @function :   协程

import asyncio
import await

asyncio def worker_1():
    print("worker_1 start.")
    await asyncio.sleep(2)
    print("worker_1 done")

asyncio def worker_2():
    print("worker_2 start.")
    await asyncio.sleep(2)
    print("worker_2 done")

asyncio def main():
    print("before await")
    await worker_1()
    print("awaited worker_1")
    await worker_2()
    print("awaited worker_2")

%time asyncio.run(main())