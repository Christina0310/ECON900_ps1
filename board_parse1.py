from bs4 import BeautifulSoup
import os
import glob
import pandas as pd

if not os.path.exists("parsed_files"):
    os.mkdir("parsed_files")

df = pd.DataFrame()



f = open("html_files/boardgamegeek1.html", "r")

#print(f.read())


soup = BeautifulSoup(f.read(), 'html.parser')

boardgames_table = soup.find("table", {"id": "collectionitems"})
#boardgames_tbody = boardgames_table.find("tbody")
boardgames_rows = boardgames_table.find_all("tr", {"id":"row_"})



boardgames_name = boardgames_rows[0].find("td", {"class": "collection_objectname"}).find("div",{"id":"results_objectname1"}).find("a").text
boardgames_ratings= boardgames_rows[0].find_all("td",{"class":"collection_bggrating"})
#game_iter = iter(boardgames_ratings)
boardgames_geek_rating= boardgames_ratings[0].text #next(game_iter).text
boardgames_ave_rating = boardgames_ratings[1].text
boardgames_num_voters = boardgames_ratings[2].text
#boardgames_rating2 = next(game_iter).text

#boardgames_geekrating = boardgames_ratings[0]#.find("td", {"class":"collection_bggrating"})


print(boardgames_name)
print(boardgames_geek_rating)
print(boardgames_ave_rating)
print(boardgames_num_voters)
#print(boardgames_price)

'''for r in boardgames_rows: 
    boardgames_name = r.find("td", {"class": "collection_objectname"}).find("div",{"style":"z-index:1000;"}).find("a").text
    boardgames_rating'''

