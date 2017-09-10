from urllib.parse import urlparse
# from urlparse import urlparse


# Gets domain name (example.com)
def get_domain_name(url):
	try:
		results = get_sub_domain_name(url).split('.')
		return results[-2] + '.' + results[-1]
	except:
		return ''

# Gets sub domain name (name.example.com)
def get_sub_domain_name(url):
	try:
		return urlparse(url).netloc
	except:
		return ''

# print(get_domain_name('https://www.youtube.com/watch?v=PPonGS2www.youtube.comRZNc'))
