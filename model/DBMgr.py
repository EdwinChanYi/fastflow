#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 数据管理模块
from model.BaseModel import BaseModel


def redis_get(**redisType):
	def decorator(func):
		def wrapper(*args, **kwgs):
			func(*args, **kwgs)
		return wrapper
	return decorator


def redis_del(**redisType):
	def decorator(func):
		def wrapper(*args, **kwgs):
			func(*args, **kwgs)
		return wrapper
	return decorator


def redis_add(**redisType):
	def decorator(func):
		def wrapper(*args, **kwgs):
			func(*args, **kwgs)
		return wrapper
	return decorator


def redis_modify(**redisType):
	def decorator(func):
		def wrapper(*args, **kwgs):
			func(*args, **kwgs)
		return wrapper
	return decorator


class DBMgr(BaseModel):

	@redis_del()
	async def Del(self, table, database="fastflow", **kwgs):
		if not len(kwgs):
			return -1
		deleteCond = []
		for key, value in kwgs.items():
			deleteCond.append("{}={}".format(key, value))

		delSql = "DELETE FROM {} WHERE {} AND {}".format(table, ",".join(deleteCond))
		result = await self.delete(delSql, mod=database)
		return result

	@redis_get()
	async def Select(self, table, database="fastflow", limit=100, **kwgs):
		if not len(kwgs):
			return -1
		queryCond = []
		for key, value in kwgs.items():
			queryCond.append("{}={}".format(key, value))
		selectSql = "SELECT FROM {} WHERE {} LIMIT {}".format(table, ",".join(queryCond), limit)
		result = await self.many(selectSql, limit, mod=database)
		return result

	@redis_add()
	async def Add(self, table, keys, dataList, database="fastflow"):
		if not len(dataList):
			return -1
		batchStr = []
		for data in dataList:
			insertOneData = []
			for key, value in data.items():
				insertOneData.append("{}={}".format(key, value))
			insertOneData = "({})".format(",".join(insertOneData))
			batchStr.append(insertOneData)
		instertSql = 'Replace INTO {}({}) VALUES {}'.format(table, ",".join(keys), ",".join(batchStr))
		result = await self.insert(instertSql, mod=database)
		return result

	@redis_modify()
	async def Modify(self, table, modifyData, condition, database="fastflow"):
		if not len(modifyData):
			return -1
		batchStr = []
		for key, value in modifyData.items():
			batchStr.append("{}={}".format(key, value))
		condStr = []
		for key, value in condition:
			condStr.append("{}={}".format(key, value))
		updateSql = 'UPDATE FROM {} SET {} WHERE {}'.format(table,
		        ",".join(batchStr), " AND ".join(condStr))
		result = await self.update(updateSql, mod=database)
		return result
