import scrapping_basket.get_nba_csv as gc


def main(year):
    gc.get_nba_csv(year)


if __name__ == "__main__":

    year = 2019
    main(year)

