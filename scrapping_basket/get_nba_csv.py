from urllib.request import urlopen
from bs4 import BeautifulSoup
import pandas as pd


def get_nba_csv(year):
    url = f"https://www.basketball-reference.com/leagues/NBA_{year}_per_game.html"
    # this is the HTML from the given URL
    html = urlopen(url)
    soup = BeautifulSoup(html, 'html.parser')
    # use findALL() to get the column headers
    soup.findAll('tr', limit=2)

    # use getText()to extract the text we need into a list
    headers = [th.getText() for th in soup.findAll('tr', limit=2)[0].findAll('th')]

    # exclude the first column as we will not need the ranking order from Basketball Reference for the analysis
    headers = headers[1:]

    # avoid the first header row
    rows = soup.findAll('tr')[1:]
    player_stats = [[td.getText() for td in rows[i].findAll('td')]
                for i in range(len(rows))]

    stats = pd.DataFrame(player_stats, columns = headers)

    csv_file = stats.to_csv("/Users/Stephi/Documents/academic/UOC/tercer_semestre/tipologia/PRAC1/skobsar_jordiba90_prac1/output_csv/nba_stats.csv")

    return csv_file





