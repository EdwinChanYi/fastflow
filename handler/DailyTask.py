#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 日常任务
from handler.BaseHandler import BaseHandler
from model.DBMgr import DBMgr
from common import TimeUtil
from conf import constant


def CheckParam(dataDict):
	for key in dataDict.keys():
		if key not in constant.DAILY_TASK_KEY:
			return False
	return True

class QueryDailyTask(BaseHandler):

	async def get(self):
		print("dailytask")
		param = self.get_param()
		queryDate = param.get("date", TimeUtil.NowTimestamp())
		user = self.get_current_user()
		monday = TimeUtil.FirstDayOfWeek()
		back = DBMgr.Select(constant.DAILY_TASK_TABLE, uid=user, time=queryDate)
		self.success_ret(back)
		return True


class AddDailyTask(BaseHandler):
	async def get(self):
		param = self.get_param()
		addData = param.get("addData", {})
		if CheckParam(addData):
			self.fail_ret(data={"msg": "param error"})
		user = self.get_current_user()
		addData["uid"] = user

		if DBMgr.Add(constant.DAILY_TASK_TABLE, addData.keys(), [addData, ]):
			self.success_ret()
		else:
			self.fail_ret()


class DelDailyTask(BaseHandler):
	pass