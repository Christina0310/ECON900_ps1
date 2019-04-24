# ECON900_ps1 REPORT                   --JIA LI
FILE NAMES:
	1. html_files: html files of 160 pages of boardgeekgame.com/browse/boardgame
	2. output: html file of just one page. It is output of testing my code, so there is no need to read it.
	3. parsed_files: .csv of data
	4. LICENSE: no need to read it
	5. README.md: report of my homework
	6. board_kmc.py
	7. board_parse.py
	8. board_regression.py
	9. board_request.py
All board.py files in 6,7,8,9 above are codes with results to be explained below
	10. scatter_color.png: picture of kmean clustering

STEPS OF DATA SCRAPPING:
	1. REQUEST: in Terminal/Git bash, run the whole file of "board_request.py." This generates html files of 160 pages of boardgeekgame in the html_files folder.
	2. PARSE: run the whole file of "board_parse.py". This generates the .csv file in the parsed_files folder. It includes Index, Geek_rating, Average_rating, Number_of_voters, Title of the game, 5 columns in total.

RESULTS OF MACHINE LEARNING:
    1.KMEAN CLUSTERING: run "board_kmc.py" to the boardgeekgame_dataset.csv file. It prints out descriptive statistics of the data. There is 16, 000 counts of data. And it classifies the games into 4 categories. 
Reason for choosing kmc: I choose kmean clustering because there is no specific categories shown in my data, so I conducted unsupervised learning for classification. 
Results of kmc show: If I classify game into 4 categories, it results in the following: a. Low Number_of_voting, Low rating
           b. Low or medium Number_of_voting, Medium rating
           c. Low Number_of_voting, High rating
           d. High Number_of_voting, Low rating
           So if the number of voters is very small, the rating cannot be high; but with large number of voters, the rating could be either high or low.
scatterplot_color.png: horizontal axis is rating, vertical axis is number of voters(scaled to the same as rating by dividing 10000).
	2. REGRESSION: run "board_regression.py".The regression predicts rating from voting number.The purpose is to see whether we can conclude whether a game is highly-rated depending merely on the number of players.  The test data, X, is selected from page 169, a page I did not scrape. As is printed out, the 3 predictions are over 6, which is not that accurate. The ratings should be below 5. This is because of the reason stated in KMC: high voting numbers do not necessarily lead to high rating.

NOTE: 
	1. I did not manage to scrape the data of price. I do not know how to do it when it did not show in the html scripts.
	2. I only scraped the highest 160 pages of data. The voting number for pages over 160 are very small, and sometimes there is no rating. Therefore, it is not worthy of scraping in my opinion. 
	3. I found out "categories" on another page of the website. If the category data is scraped, then I can do supervised learning. However, the feature data in the file is not relevant to classification of the games. Because the categories on the website depends mainly on the theme of games, not ratings, num_of_voters etc. 