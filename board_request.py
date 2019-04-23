import urllib.request
import os
import time
import datetime

if not os.path.exists("html_files"):
	os.mkdir("html_files")



for i in range(1,161):                                                  #request for page 1 , 2...160 of boardgamegeek.com
	current_page = str(i)
	print("page " + current_page)
	f = open("html_files/boardgamegeek" + current_page + ".html", "wb")
	url = "https://boardgamegeek.com/browse/boardgame/page/%d" %i 
	req = urllib.request.Request(url)
	response = urllib.request.urlopen(req)
	html = response.read()
	f.write(html)
	f.close()
	time.sleep(100)