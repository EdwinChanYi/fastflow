#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys


class Obejct(object):
	_fileds = []

	def __init__(self, *args, **kwargs):
		if len(self._fileds) < len(args):
			raise TypeError('Expected {} arguments'.format(self._fileds))
		# 输入_filed
		for name_, value_ in zip(self._fileds, args):
			setattr(self, name_, value_)
		for name_, value_ in kwargs.items():
			setattr(self, name_, value_)

	def __str__(self):
		return "({})".format(','.join(["%s:%s" % item for item in self.__dict__.items()]))


class Type(object):
	def __init__(self, name, expect_type):
		self.name = name
		self.expected_type = expect_type

	def __get__(self, instance, owner):
		if not instance:
			return self
		return instance.__dict__[self.name]

	def __set__(self, instance, value):
		if not isinstance(value, self.expected_type):
			raise TypeError('Expected ' + str(self.expected_type))
		instance.__dict__[self.name] = value
		print("")

	def __delete__(self, instance):
		if not instance:
			return
		del instance.__dict__[self.name]


def typeassert(**kwargs):
	def decorator(cls):
		for name, expect_type in kwargs.items():
			setattr(cls, name, Type(name, expect_type))
		return cls
	return decorator


if __name__ == "__main__":
	@typeassert(name=str, num=int)
	class Tree(Obejct):
		_fileds = ["leafe"]

		def __init__(self, *args, **kwargs):
			super().__init__(*args, **kwargs)
			self.name = ""
			self.num = 1

		def func(self):
			pass
	a = Tree(12, dsds=12)
	print(a)
	print(a.__dict__)