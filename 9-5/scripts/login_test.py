# ⚠️ 导入自写包之前,先把"上级目录(9-5)"加入模块搜索路径 sys.path
# 原因:直接运行本文件时,Python 只会搜索 scripts 文件夹,找不到隔壁的 api 包
# __file__ = 当前文件路径 → dirname 两次 = 上一级目录(9-5) → 加进 sys.path
import sys, os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from api.login import num_test

test_data = [{"username": "13488888888", "password": "123456"},
 {"username": "", "password": "123456"}]


for item in test_data:
    username=item["username"]
    password=item["password"]
    result=num_test(username,password)
