#!/usr/bin/env python3
# -*- coding: utf-8 -*-
############################################################
# file			 : LanguageWrapper.py
# 制作			 : tatra 2024年11月12日
# 対象バージョン : python 3.x. 以上
# version 		 : '0.0.5'
# 
#
#
# メモ :
#
#""" Details about the module and for what purpose it was built for"""
# ---------------------------------------------------------------------------
# 外部モジュール : chardet
# ---------------------------------------------------------------------------
############################################################


import glob
import os
import json
import enum

from .debug import debug, LogLevel
from chardet import detect

self_dir = os.path.dirname(__file__)
default_lang_path = self_dir + "/../language/"
default_lang_conf_path = self_dir + "/../language/language.config"

#class 

class LangWap():
	class ConfTag():
		sub="sub"

	def __init__(self,
			lang_dir=default_lang_path,
			conf_path=default_lang_conf_path
	) -> None:
		lang_dir+="/*.lang"
		lang_list=glob.glob(lang_dir)
		self.sub_lang={}
		self.main_lang={}
		self.lang_list={}
		#debug.dprint(lang_list)
		self.__lang_list__(lang_list)
		self.__init_conf__(conf_path)
		self.loadLang(self.config.get(self.ConfTag.sub),True)

	def __init_conf__(self,conf_path):
		with open(conf_path, "r") as cf:
			self.config = json.load(cf)

	def __load_json__(self, path):
		with open(path, "rb") as bf:
			data = bf.read()
			encord = detect(data)
		with open(path, mode="r" , encoding=encord['encoding']) as f:
			llj = json.load(f)
		return llj

	def __lang_list__(self, lang_list):
		for path in lang_list:
			llj = self.__load_json__(path)
			lang_code=llj["header"]["LanguageCode"]
			self.lang_list[lang_code]=llj["header"]
			self.lang_list[lang_code]["path"]=path
			#debug.dprint(self.lang_list)


	def getLangList(self):
		return self.lang_list

	def __get_msgs__(self, lang):
		lpath=self.lang_list[lang]["path"]
		j = self.__load_json__(lpath)
		return j["messages"]

	def loadLang(self, lang, sub=False):
		if sub :
			self.sub_lang = self.__get_msgs__(lang)
		else:
			self.main_lang = self.__get_msgs__(lang)

	def getMessage(self, msg_tag):
		if self.main_lang.get(msg_tag):
			return self.main_lang.get(msg_tag)
		elif self.sub_lang.get(msg_tag):
			return self.sub_lang.get(msg_tag)

		return msg_tag

if __name__ == "__main__":
	debug.set_level(LogLevel.DEBUG)
	lang = LangWap()
	lang.loadLang("ja-jp")
	print(lang.getMessage("test"))
	print(lang.getMessage("none"))
	print(lang.getMessage("fragment"))