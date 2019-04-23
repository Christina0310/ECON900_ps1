from bs4 import BeautifulSoup
import os
import glob
	
if not os.path.exists("parsed_files"):
	os.mkdir("parsed_files")
	
	
	
f = open("html_files/boardgamegeek1.html", "r", encoding = "utf-8")

	
soup = BeautifulSoup(f.read(), 'html.parser')
	
print(soup)