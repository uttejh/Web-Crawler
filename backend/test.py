from html.parser import HTMLParser
from urllib import parse
# from urllib.request import urlopen

class Test(HTMLParser):
	def __init__(self):
		super().__init__()

	def finder(self, tag):
		print(tag)


html_string = ''

# try:
# 	response = urlopen('https://www.youtube.com/watch?v=F2lbS-F0eTQ')
# 	if 'text/html' in response.getheader('Content-Type'):
# 		html_bytes = response.read()
# 		html_string = html_bytes.decode("utf-8")
# 		find = Test()
# 		find.feed('<h1></h1>')
# 		# print(html_string)
# except Exception as e:
# 	print(str(e))

finder = Test()
finder.feed('<html><p></p></html>')
