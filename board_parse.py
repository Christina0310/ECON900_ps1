from bs4 import BeautifulSoup
import os
import glob
import pandas as pd

if not os.path.exists("parsed_files"):
    os.mkdir("parsed_files")

df = pd.DataFrame()

for i in range(1,161):#one_file_name in glob.glob("html_files/*.html"):
        current_page = str(i)
        one_file_name ="html_files/boardgamegeek" + current_page + ".html"
        print("parsing " + one_file_name)
        f = open(one_file_name, "r")
        soup = BeautifulSoup(f.read(), 'html.parser')
        f.close()
        boardgames_table = soup.find("table", {"id": "collectionitems"})
        boardgames_rows = boardgames_table.find_all("tr", {"id":"row_"})
        for r in boardgames_rows: 
            boardgames_name = r.find("td", {"class": "collection_objectname"}).find("div",{"style":"z-index:1000;"}).find("a").text
            boardgames_neg_year = r.find("td", {"class": "collection_objectname"}).find("div",{"style":"z-index:1000;"}).find("a").text[1]
            boardgames_ratings= r.find_all("td",{"class":"collection_bggrating"})
            boardgames_geek_ratingq= boardgames_ratings[0].text #next(game_iter).text
            boardgames_ave_ratingq = boardgames_ratings[1].text
            boardgames_num_votersq = boardgames_ratings[2].text
            boardgames_year = boardgames_neg_year[1:5]
            boardgames_geek_rating = float(boardgames_geek_ratingq)
            boardgames_ave_rating = float(boardgames_ave_ratingq)
            boardgames_num_voters = int(boardgames_num_votersq)
            df = df.append({ 
                'title': boardgames_name,
                'year': boardgames_year,
                'geek_rating': boardgames_geek_rating,
                'average_rating': boardgames_ave_rating,
                'num_of_voters': boardgames_num_voters
                }, ignore_index=True)



df.to_csv("parsed_files/boardgeekgame_dataset.csv")





