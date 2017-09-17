from html.parser import HTMLParser
from urllib import parse

class Linky(HTMLParser):

	def __init__(self):
		super().__init__()

	def handle_starttag(self, tag, attrs):
		print(tag)

	# def error(self, message):
	# 	pass

finder = Linky()
finder.feed('<!DOCTYPE html><html lang="en"><head><meta charset="UTF-8"><title>Document</title></head><body></body></html>')