#!/usr/bin/env python
# -*- coding: utf-8 -*-
from common import TimeUtil
from handler import BaseHandler, constant


def CheckParam(dataDict):
	for key in dataDict.keys():
		if key not in constant.WEEKLY_AIM_KEY:
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
		back = await constant.DBMGR.Select(constant.WEEKLY_AIM_TABLE, uid=user)
		self.success_ret(back)


# 添加周目标
class AddWeeklyGoal(BaseHandler):

	async def get(self):
		param = self.get_param()
		addData = param.get("addData", {})
		aim = param.get("aim", "")
		if aim == "":
			self.fail_ret()
		addData['aim'] = aim
		if CheckParam(addData):
			self.fail_ret(data={"msg": "param error"})

		user = self.get_current_user()
		addData["uid"] = user
		monday = TimeUtil.FirstDayOfWeek()
		addData['weekId'] = int(monday)

		result = await constant.DBMGR.Add(constant.WEEKLY_AIM_TABLE, addData.keys(), [addData, ])
		if result:
			self.success_ret()
		else:
			self.fail_ret()


# 修改周目标
class UpdateWeeklyGoal(BaseHandler):

	async def get(self):
		param = self.get_param()
		id = param.get('id', -1)
		aim = param.get("aim", "")
		summary = param.get("summary", "")
		state = param.get("state", 0)

		if id == -1 :
			self.fail_ret(data={"msg": "ID 为空"})
			return

		updateData = {}
		conditionData = {}

		conditionData['id'] = int(id)
		if aim != "":
			updateData["aim"] = aim
		if summary != "":
			updateData["summary"] = summary
		updateData['state'] = int(state)

		if CheckParam(updateData) == False:
			self.fail_ret(data={"msg": "param error"})
			return

		user = self.get_current_user()
		conditionData["uid"] = int(user)

		result = await constant.DBMGR.Modify(constant.WEEKLY_AIM_TABLE, updateData, conditionData)
		if result:
			self.success_ret()
		else:
			self.fail_ret()


# 删除周目标
class DeleteWeeklyGoal(BaseHandler):

	async def get(self):
		param = self.get_param()

		conditionData = {}
		conditionData['id'] = param.get("id", {})
		user = self.get_current_user()
		conditionData["uid"] = user

		modifyData = {
			'state': int(2)
		}

		result = await constant.DBMGR.Modify(constant.WEEKLY_AIM_TABLE, modifyData, conditionData)
		if result:
			self.success_ret()
		else:
			self.fail_ret()
