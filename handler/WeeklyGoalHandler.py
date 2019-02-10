#!/usr/bin/env python
# -*- coding: utf-8 -*-
from common import TimeUtil
from handler import BaseHandler, constant
from model import DBMgr


def CheckParam(dataDict):
	for key in dataDict.keys():
		if key not in constant.WEEKLY_GOAL_KEY:
			return False
	return True


# 查询周目标
class QueryWeeklyGoal(BaseHandler):

	async def get(self):
		print("query weekly goal")
		param = self.get_param()
		queryDate = param.get("date", TimeUtil.NowTimestamp())
		user = self.get_current_user()
		monday = TimeUtil.FirstDayOfWeek()
		back = DBMgr.DBMgr().Select(constant.DAILY_TASK_TABLE, uid=user, time=queryDate)
		self.success_ret(back)
		return True


# 添加周目标
class AddWeeklyGoal(BaseHandler):

	async def get(self):
		param = self.get_param()
		addData = param.get("addData", {})
		if CheckParam(addData):
			self.fail_ret(data={"msg": "param error"})
		user = self.get_current_user()
		addData["uid"] = user

		if DBMgr.DBMgr().Add(constant.WEEKLY_GOAL_TABLE, addData.keys(), [addData, ]):
			self.success_ret()
		else:
			self.fail_ret()


# 修改周目标
class UpdateWeeklyGoal(BaseHandler):

	async def get(self):
		return self.success_ret()


# 删除周目标
class DeleteWeeklyGoal(BaseHandler):
	async def get(self):
		param = self.get_param()
		deleteData = param.get("deleteData", {})
		if (CheckParam(deleteData)):
			return self.success_ret()
