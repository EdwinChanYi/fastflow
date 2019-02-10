#!/usr/bin/env python
#-*- coding: utf-8 -*-

import datetime
import time


def Now():
	return datetime.date.today()


def NowTimestamp():
	return int(time.time())


def TimeToDatetime(timestamp):
	return datetime.datetime.utcfromtimestamp(timestamp)


def FirstDayOfWeek(timestamp=None):
	today = TimeToDatetime(timestamp) if timestamp else Now()
	weekday = today.weekday()
	monday = today - datetime.timedelta(weekday - 1)
	return monday.strftime("%Y%m%d")

