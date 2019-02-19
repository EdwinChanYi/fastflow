#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 路由文件，遵守restful规范
# 格式 : (路径, 处理器, 构造函数参数, 名称)
# 注意:名称不可重复

from handler import *

route = [
    # 微信
    (r"/wechatVerify", WechatVerifyHandler, None, '微信接入验证'),
    (r"/QueryDailyTask", QueryDailyTask, None, '日常任务'),
    (r"/AddDailyTask", AddDailyTask, None, '添加任务'),
    (r"/DelDailyTask", DelDailyTask, None, '删除任务'),
    (r"/ModifyDailyTask", ModifyDailyTask, None, '修改任务'),
    (r"/queryWeeklyGoal", QueryWeeklyGoal, None, "查询周目标"),
    (r"/addWeeklyGoal", AddWeeklyGoal, None, "新增周目标"),
    (r"/updateWeeklyGoal", UpdateWeeklyGoal, "更新周目标"),
    (r"/deleteWeeklyGoal", DeleteWeeklyGoal, None, "删除周目标"),
]