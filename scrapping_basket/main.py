import scrapping_basket.get_nba_csv as gc


def main(url):

    gc.get_nba_csv(url)


if __name__ == "__main__":

    year = 2019
    url_players = f"https://www.basketball-reference.com/leagues/NBA_{year}_per_game.html"
    url_teams_wins = "https://www.basketball-reference.com/leagues/NBA_wins.html"


    main(url_teams_wins)

