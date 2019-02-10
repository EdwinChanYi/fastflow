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


class DBMgr(BaseModel):

	@redis_del()
	async def Del(self, table, database="fastflow", **kwgs):
		if not len(kwgs):
			return -1
		deleteCond = []
		for key, value in kwgs.items():
			deleteCond.append("{}={}".format(key, value))

		delSql = "DELETE FROM {} WHERE {} AND {}".format(table, ",".join(deleteCond))
		return self.delete(delSql, mod=database)

	@redis_get()
	async def Select(self, table, database="fastflow", limit=100, **kwgs):
		if not len(kwgs):
			return -1
		queryCond = []
		for key, value in kwgs.items():
			queryCond.append("{}={}".format(key, value))
		selectSql = "SELECT FROM {} WHERE {} LIMIT {}".format(table, ",".join(queryCond), limit)
		return self.many(selectSql, limit, mod=database)

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
		return self.insert(instertSql, mod=database)
