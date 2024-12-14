#!/usr/bin/env python3
# -*- coding: utf-8 -*-
############################################################
# file			 : Rect.py
# 推奨TABサイズ	 : 4
# 制作			 : tatra 2024年11月24日
# 対象バージョン : python 3.10. 以上
# version 		 : '0.0.5'
# 説明			 :
#	座標系矩形の定義
#
# メモ :
#
# ---------------------------------------------------------------------------
# 外部モジュール : 
# ---------------------------------------------------------------------------
############################################################


from typing import overload

from .Size import Size
from .Point import Point
from .Align import Align

if __name__ == "__main__":
	from debug import debug, LogLevel
else :
	from ..debug import debug, LogLevel

class Rect():
	pass
class Rect():
	@overload
	def __init__(self,x:int,y:int,w:int,h:int,base_point:Align=Align.top_left,abs:bool=False):
		pass
	@overload
	def __init__(self,start:Point,size:Size,base_point:Align=Align.top_left,abs:bool=False)-> None:
		pass
	@overload
	def __init__(self,start:Point,end:Point,base_point:Align=Align.top_left,abs:bool=True)-> None:
		pass
	@overload
	def __init__(self,point:Point,size:Size,base_point:Align=Align.top_left,abs:bool=False) :
		pass
	@overload
	def __init__(self,rect:Rect):
		pass
	def __init__(
			self,
			rect:Rect=None,
			point:Point=None,
			start:Point=None,
			end:Point=None,
			size:Size=None,
			x:int=None,
			y:int=None,
			w:int=None,
			h:int=None,
			align:Align=None,
			abs:bool=None,
			**kwargs) :
		"""
			使い方
			1 start:Point, size:Size, [abs:bool] / 描画開始地点, サイズ
			2 start:Point, end:Point, [abs:bool] / 描画開始地点, 描画終了地点
			3 point:Point, size:Size, [align:Align], [abs:bool] / 描画地点, サイズ, 描画開始地点の設定
			4 x:int, y:int, w:int, h:int, [abs:bool] / x, y, w, h
			5 Rect 
		"""
		self.m_base_point:Align
		self.m_point:Point
		self.m_size:Size
		self.m_isAbsolute:bool

		isAbs=False
		if type(rect) is Rect :
			self.m_point = Point(point=rect.m_point)
			self.m_size = Size(rect.m_size)
			self.m_base_point = rect.m_base_point
			self.m_isAbsolute = rect.m_isAbsolute
			return
		elif start and size:
			self.m_point = Point(point=start)
			self.m_size  = Size(size)
			isAbs=False
			pass
		elif start and end :
			self.m_point = Point(point=start)
			self.m_size  = Size(end)
			isAbs=True
			pass
		elif point and size:
			self.m_point=Point(point=point)
			self.m_size=Size(size)
			isAbs=False
			pass
		elif x and y and w and h:
			self.m_point=Point(x=x,y=y)
			self.m_size=Size(w,h)
			isAbs=False
			pass
		elif (
			not point and
			not start and
			not end and
			not size and
			not x and
			not y and
			not w and
			not h and
			len(kwargs) == 0
		):
			self.m_point=Point(0,0)
			self.m_size=Size(0,0)
			isAbs=False
		else:
			raise Exception()
		
		if align:
			self.m_base_point=align
		else :
			self.m_base_point=Align.top_left

		if abs is not None:
			isAbs = abs
		self.m_isAbsolute = isAbs

	@overload
	def __add__(self, other:Point)->Rect:
		pass
	@overload
	def __add__(self, other:Size)->Rect:
		pass
	@overload
	def __add__(self, other:int)->Rect:
		pass
	@overload
	def __add__(self, other:Rect)->Rect:
		pass
	def __add__(self, other)->Rect:
		if type(other) is Point:
			return Rect(
				point = (self.m_point + other),
				size  = self.m_size,
				align = self.m_base_point
			)
		elif type(other) is Size:
			return Rect(
				point = self.m_point,
				size  = (self.m_size + other),
				align = self.m_base_point
			)
		elif type(other) is Rect:
			return Rect(
				point = (self.m_point + other.m_point),
				size  = (self.m_size + other.m_size),
				align = self.m_base_point
			)
		elif type(other) is int:
			return Rect(
				point = (self.m_point + other) ,
				size  = (self.m_size + other),
				align=self.m_base_point
			)
		debug.cprint(str(type(other)) + "? そいつぁしらねぇなぁ?")

	@overload
	def __sub__(self, other:Point)->Rect:
		pass
	@overload
	def __sub__(self, other:Point)->Rect:
		pass
	@overload
	def __sub__(self, other:int)->Rect:
		pass
	@overload
	def __sub__(self, other:Rect)->Rect:
		pass
	def __sub__(self, other)->Rect:
		if type(other) is Point:
			return Rect(
				point = (self.m_point - other),
				size  = self.m_size,
				align = self.m_base_point
			)
		elif type(other) is Size:
			return Rect(
				point = self.m_point,
				size  = (self.m_size - other),
				align = self.m_base_point
			)
		elif type(other) is Rect:
			return Rect(
				point = (self.m_point - other.m_point),
				size  = (self.m_size - other.m_base_point),
				align = self.m_base_point
			)
		elif type(other) is int:
			return Rect(
				point = (self.m_point - other) ,
				size  = (self.m_size - other),
				align = self.m_base_point
			)
		debug.cprint(str(type(other)) + "? そいつぁしらねぇなぁ?")


	def isInPoint(self, point:Point):
		match self.m_base_point:
			case Align.top_left:
				#if self.m_isAbsolute :
				return ((self.m_point <= point) and (point <= self.m_size))
				#return ((self.m_point <= point) and (point <= ( self.m_size - self.m_point)))
				pass
			case Align.top_right:
				debug.cprint("Not implemented  未実装")
				pass
			case Align.bottom_left:
				debug.cprint("Not implemented  未実装")
				pass
			case Align.bottom_right:
				debug.cprint("Not implemented  未実装")
				pass
		pass

	def isAbsolute(self)->bool:
		return self.m_isAbsolute
	def getSize(self)->Size:
		return self.m_size
	def getWide(self)->int:
		return self.m_size.w
	def getHeight(self)->int:
		return self.m_size.h
	def getBegin(self)->Point:
		return self.m_point
	def getBeginX(self)->int:
		return self.m_point.x
	def getBeginY(self)->int:
		return self.m_point.y
	def getEnd(self)->Point:
		if self.m_isAbsolute :
			return self.m_size
		return Size(self.m_point + self.m_size)
	def getEndX(self)->int:
		if self.m_isAbsolute :
			return self.m_size.w
		return self.m_point.x + self.m_size.w
	def getEndY(self)->int:
		if self.m_isAbsolute :
			return self.m_size.h
		return self.m_point.y + self.m_size.h
