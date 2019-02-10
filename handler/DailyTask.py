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


def operator(**opType):
	def decorator(func):
		def wrapper(*args, **kwgs):
			func(*args, **kwgs)

		return wrapper
	return decorator


class QueryDailyTask(BaseHandler):
	DBMGR = DBMgr()
	async def get(self):
		print("dailytask")
		param = self.get_param()
		queryDate = param.get("date", TimeUtil.NowTimestamp())
		user = self.get_current_user()
		monday = TimeUtil.FirstDayOfWeek()
		back = constant.DBMGR.Select(constant.DAILY_TASK_TABLE, uid=user, time=queryDate)
		self.success_ret(back)
		return True


class AddDailyTask(BaseHandler):
	DBMGR = DBMgr()
	async def get(self):
		param = self.get_param()
		addData = param.get("addData", {})
		if CheckParam(addData):
			self.fail_ret(data={"msg": "param error"})
		user = self.get_current_user()
		addData["uid"] = user

		if constant.DBMGR.Add(constant.DAILY_TASK_TABLE, addData.keys(), [addData, ]):
			self.success_ret()
		else:
			self.fail_ret()


class DelDailyTask(BaseHandler):
	DBMGR = DBMgr()

	async def get(self):
		param = self.get_param()
		delTask = param.get("delTask", None)
		user = self.get_current_user()
		delCond = {"uid": user, "taskID": delTask}
		if constant.DBMGR.Del(constant.DAILY_TASK_TABLE, delCond):
			self.success_ret()
		else:
			self.fail_ret()


class ModifyDailyTask(BaseHandler):
	DBMGR = DBMgr()

	async def get(self):
		param = self.get_param()
		data = param.get("data", None)
		condition = param.get("condition", None)
		user = self.get_current_user()
		condition["uid"] = user
		if constant.DBMGR.Modify(constant.DAILY_TASK_TABLE, data, condition):
			self.success_ret()
		else:
			self.fail_ret()