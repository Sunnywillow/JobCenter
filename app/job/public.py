# -*- coding: utf-8 -*-
# @Author: guomaoqiu
# @File Name: public.py
# @Date:   2019-03-12 11:01:33
# @Last Modified by:   guomaoqiu
# @Last Modified time: 2019-03-19 11:50:42

import subprocess
import json
import datetime
from datetime import date
import os

def exec_shell(cmd):
    '''执行shell命令函数'''
    if "rm" in cmd:
        return False
    # export PATH="$PATH:/home/yang/.local/share/virtualenvs/JobCenter-6lJXnf_S/bin/python"
    # my_env = os.environ.copy()
    # my_env = os.environ.copy()
    # python_bin = "/home/yang/.local/share/virtualenvs/JobCenter-6lJXnf_S/bin/python"
    # my_env ="/home/yang/.local/share/virtualenvs/JobCenter-6lJXnf_S/bin/python"
    sub2 = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    # sub2 = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, env={})
    stdout, stderr = sub2.communicate()
    ret = sub2.returncode
    return ret, stdout.decode('utf-8')


class DateEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime.datetime):
            return obj.strftime('%Y-%m-%d %H:%M:%S')
        elif isinstance(obj, date):
            return obj.strftime("%Y-%m-%d")
        else:
            return json.JSONEncoder.default(self, obj)