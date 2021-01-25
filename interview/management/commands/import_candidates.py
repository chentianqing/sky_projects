# -*- coding: utf-8 -*-

# @Project:   sky_projects
# @Time:      2021-01-22 08:44
# @Author  :    TianQing Chen
# @File    :    import_candidates.py
# @function :   导入功能

import csv

from  django.core.management import BaseCommand
from interview.models import Candidate

class Command(BaseCommand):
    help = "从一个csv文件对内容中读取候选人列表，导入到数据库中"

    def add_arguments(self, parser):
