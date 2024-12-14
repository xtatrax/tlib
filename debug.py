
import enum

@enum.unique
class LogLevel(enum.Flag):
	NONE= enum.auto()
	INFO = enum.auto()
	DEBUG = enum.auto()
	WARNING = enum.auto()
	ERROR = enum.auto()
	EX_IGNORE = enum.auto()
	CRITICAL = enum.auto()
	ALL = INFO | DEBUG | WARNING | ERROR | CRITICAL


class debug():
	logLevel=LogLevel.ALL

	@classmethod
	def get_isDEBUG(cls):
		return (LogLevel.DEBUG in cls.logLevel)

	@classmethod
	def set_level(cls,level:LogLevel):
		cls.logLevel = level

	@classmethod
	def print(cls,comment, ll:LogLevel=LogLevel.ALL):
		if cls.logLevel in ll:
			print(comment)
	
	@classmethod
	def dprint(cls,comment):
		if (LogLevel.DEBUG in cls.logLevel):
			print(comment)

	@classmethod
	def iprint(cls,comment):
		if (LogLevel.INFO in cls.logLevel):
			print(comment)

	@classmethod
	def wprint(cls,comment):
		if (LogLevel.WARNING in cls.logLevel):
			print(comment)

	@classmethod
	def eprint(cls,comment):
		if (LogLevel.ERROR in cls.logLevel):
			print(comment)

	@classmethod
	def cprint(cls,comment):
		if not (LogLevel.EX_IGNORE in cls.logLevel):
			raise Exception(comment)
		if (LogLevel.CRITICAL in cls.logLevel):
			print(comment)
