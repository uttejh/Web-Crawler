from html.parser import HTMLParser
from urllib import parser

class LinkFinder(object):
	"""docstring for LinkFinder"""
	# def __init__(self, arg):
	# 	super(LinkFinder, self).__init__()
	# 	self.arg = arg

	def __init__(self):
		super().__init__()
		
	def handle_starttag(self, tag, attrs):
		print(tag)

	def error(self, message):
		pass		