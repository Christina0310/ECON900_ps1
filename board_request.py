'''import urllib.request
	
response = urllib.request.urlopen('https://boardgamegeek.com/browse/boardgame')
	
html = response.read()
	
print(html)'''
	
import urllib.request
import os
	
response = urllib.request.urlopen('https://boardgamegeek.com/browse/boardgame')
	
html = response.read()
	
#print(html)
	
	
if not os.path.exists("output"):
	os.mkdir("output")
	
f = open("output/boardgamegeek.html", "wb")

f.write(html)