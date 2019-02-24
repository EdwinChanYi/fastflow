#!/usr/bin/env python
# -*- coding: utf-8 -*-
from model.DBMgr import DBMgr
# 业务异常
bus_e = {
    # 同一业务业务异常编号相邻
    # 异常名称              编号              msg
    'TEST_ERROE': {'code': 10000, 'msg': 'test err'},
}

# redis key
REDIS_SHOP_DETAIL_HOST = 'shop_detail_host_%s'      # 商店根据域名获取详情
REDIS_USER_ID = 'user_detail_id_%s'                 # 用户根据id获取详情

# mysql key

DAILY_TASK_TABLE = "daily_task"
DAILY_TASK_KEY = {"id", "uid", "content", "summary", "state", "create_time", "aim"}


DBMGR = DBMgr()

WEEKLY_AIM_TABLE = 'weekly_aim'
WEEKLY_AIM_KEY = {"id", "uid", "weekId", "aim", "summary", "state", "create_time"}

