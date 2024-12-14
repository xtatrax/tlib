#!/usr/bin/env python3
# -*- coding: utf-8 -*-
############################################################
# file			 : Align.py
# 推奨TABサイズ	 : 4
# 制作			 : tatra 2024年11月24日
# 対象バージョン : python 3.10. 以上
# version 		 : '0.0.5'
# 説明			 :
#	座標系 アラインの定義 
#
# メモ :
#
# ---------------------------------------------------------------------------
# 外部モジュール : 
# ---------------------------------------------------------------------------
############################################################


import enum

class Align(enum.Flag):
	top=enum.auto()
	bottom=enum.auto()
	left=enum.auto()
	right=enum.auto()

	top_left=top | left
	bottom_left=bottom |left
	top_right=top | right
	bottom_right=bottom | right

	w_middle=top | bottom
	h_middle=left | right

	center=w_middle | h_middle
	pass
