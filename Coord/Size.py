#!/usr/bin/env python3
# -*- coding: utf-8 -*-
############################################################
# file			 : Size.py
# 推奨TABサイズ	 : 4
# 制作			 : tatra 2024年11月24日
# 対象バージョン : python 3.10. 以上
# version 		 : '0.0.5'
# 説明			 :
#	座標系サイズの定義
#
# メモ :
#
# ---------------------------------------------------------------------------
# 外部モジュール : 
# ---------------------------------------------------------------------------
############################################################
import os

from typing import overload
from typing import TYPE_CHECKING
if TYPE_CHECKING:
	from .Point import Point

if __name__ == "__main__":
	from debug import debug, LogLevel
else :
	from ..debug import debug, LogLevel


class Size():
	pass
class Size():
	w=0
	h=0
	def __init__(self) -> None:
		pass
	@overload
	def __init__(self,size:Size) -> None:
		pass
	@overload
	def __init__(self,point:'Point') -> None:
		pass
	@overload
	def __init__(self,size:os.terminal_size) -> None:
		pass
	@overload
	def __init__(self,w:int,h:int) -> None:
		pass
	def __init__(self, arg1, arg2=None) -> None:
		if type(arg1) is int:
			if type(arg2) is int:
				self.w = arg1
				self.h = arg2
				return
			debug.iprint(" please if ( (type(arg1) is int) and (type(arg2) is int))")
			debug.cprint("if arg1 is int case of arg2 is int please")

		elif str(type(arg1)) == '<class \''+__package__+'.Point.Point\'>':
			self.w = arg1.x
			self.h = arg1.y
			return
		elif type(arg1) is Size:
			self.w = arg1.w
			self.h = arg1.h
			return
		elif type(arg1) is os.terminal_size:
			self.w = arg1.columns
			self.h = arg1.lines
			return
		debug.cprint("invalid argument")


	@overload
	def __add__(self, other:'Point')->Size:
		pass
	@overload
	def __add__(self, other:Size)->Size:
		pass
	@overload
	def __add__(self, other:int)->Size:
		pass
	def __add__(self, other)->Size:
		if str(type(other)) == '<class \''+__package__+'.Point.Point\'>':
			return Size(self.w + other.x,self.h + other.y)
		elif type(other) is Size:
			return Size(self.w + other.w,self.h + other.h)
		elif type(other) is int:
			return Size(self.w + other, self.h + other)
		debug.cprint(str(type(other)) + "? そいつぁしらねぇなぁ?")

	@overload
	def __iadd__(self, other:'Point')->Size:
		pass
	@overload
	def __iadd__(self, other:Size)->Size:
		pass
	@overload
	def __iadd__(self, other:int)->Size:
		pass
	def __iadd__(self, other)->Size:
		if str(type(other)) == '<class \''+__package__+'.Point.Point\'>':
			self.w += other.x
			self.h += other.y
			return self
		elif type(other) is Size:
			self.w += other.w
			self.h += other.h
			return self
		elif type(other) is int:
			self.w += other
			self.h += other
			return self
		debug.cprint(str(type(other)) + "? そいつぁしらねぇなぁ?")

	@overload
	def __sub__(self, other:'Point')->Size:
		pass
	@overload
	def __sub__(self, other:Size)->Size:
		pass
	@overload
	def __sub__(self, other:int)->Size:
		pass
	def __sub__(self, other)->Size:
		if str(type(other)) == '<class \''+__package__+'.Point.Point\'>':
			return Size(self.w - other.x, self.h - other.y)
		elif type(other) is Size:
			return Size(self.w - other.w, self.h - other.h)
		elif type(other) is int:
			return Size(self.w - other, self.h - other)
		debug.cprint(str(type(other)) + "? そいつぁしらねぇなぁ?")

	@overload
	def __isub__(self, other:'Point')->Size:
		pass
	@overload
	def __isub__(self, other:Size)->Size:
		pass
	@overload
	def __isub__(self, other:int)->Size:
		pass
	def __isub__(self, other)->Size:
		if str(type(other)) == '<class \''+__package__+'.Point.Point\'>':
			self.w -= other.x
			self.h -= other.y
			return self
		elif type(other) is Size:
			self.w -= other.w
			self.h -= other.h
			return self
		elif type(other) is int:
			self.w -= other
			self.h -= other
			return self
		debug.cprint(str(type(other)) + "? そいつぁしらねぇなぁ?")

	# self < other
	def __lt__(self, other:'Point'):
		return (self.w < other.x and self.h < other.y)
	def __lt__(self, other:Size):
		return (self.w < other.w and self.h < other.h)
	# self <= other
	def __le__(self, other:'Point'):
		return (self.w <= other.x and self.h <= other.y)
	def __le__(self, other:Size):
		return (self.w <= other.w and self.h <= other.h)
	# self == other
	def __eq__(self, other:'Point'):
		return (self.w == other.x and self.h == other.y)
	def __eq__(self, other:Size):
		return (self.w == other.w and self.h == other.h)
	# self != other
	def __ne__(self, other:'Point'):
		return not (self.w == other.x and self.h == other.y)
	def __ne__(self, other:Size):
		return not (self.w == other.w and self.h == other.h)
	# self > other
	def __gt__(self, other:'Point'):
		return (self.w > other.x and self.h > other.y)
	def __gt__(self, other:Size):
		return (self.w > other.w and self.h > other.h)
	# self >= other
	def __ge__(self, other:'Point'):
		return (self.w >= other.x and self.h >= other.y)
	def __ge__(self, other:Size):
		return (self.w >= other.w and self.h >= other.h)
