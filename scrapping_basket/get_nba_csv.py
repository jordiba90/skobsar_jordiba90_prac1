from urllib.request import urlopen
from bs4 import BeautifulSoup
import pandas as pd
from pathlib import Path


def get_nba_csv(url, several = True):

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

    count = 1
    my_file = Path(f"/Users/Stephi/Documents/academic/UOC/tercer_semestre/tipologia/PRAC1/skobsar_jordiba90_prac1/output_csv/nba_stats_{count}.csv")

    if my_file.is_file():
        pass
    else:
        count = count + 1
        csv_file = stats.to_csv(f"/Users/Stephi/Documents/academic/UOC/tercer_semestre/tipologia/PRAC1/skobsar_jordiba90_prac1/output_csv/nba_stats_{1}.csv")

    return csv_file





