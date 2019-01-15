##This script returns the correct logging level
import logging

def getLoggingLevel(log_level):
	if log_level == 'debug':
		return logging.DEBUG
	elif log_level == 'info':
		return logging.INFO
	elif log_level == 'warning':
		return logging.WARNING
	elif log_level == 'error':
		return logging.ERROR
	elif log_level == 'critical':
		return logging.CRITICAL
	else:
		return logging.DEBUG



