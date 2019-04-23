import urllib.request
	
response = urllib.request.urlopen('https://boardgamegeek.com/browse/boardgame')
	
html = response.read()
	
print(html)
	
