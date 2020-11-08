import matplotlib.pyplot as plt
import pandas as pd
import os
from pathlib import Path


def get_analysis(csv):
    """
    Description: Function to preprocess the data set to perform the analysis
    :param csv:
    :return:
    """

    df_nba = pd.read_csv(csv)
    description = df_nba.describe()
    print(description)

    analysis = "analysis"

    if not os.path.exists(analysis):
        os.mkdir(analysis)
    description.to_csv(os.path.join(analysis, "description_data.csv"))

    df_types_variable = df_nba.dtypes
    df_types_variable.to_csv(os.path.join(analysis, "type_of_variables.csv"))

    number_of_nans = df_nba.isna().sum()
    number_of_nans.to_csv(os.path.join(analysis, "number_of_nans.csv"))

    ####All histogtrams
    df = df_nba
    for col in df.columns:
        try:
            df[col] = pd.to_numeric(df[col])
            df.hist(column=col)
            plt.savefig(os.path.join(analysis, f"{col}.png"))
        except ValueError:
            print('This column can not be represented as a histogram')

def preprocessing_dataset(csv):

    df_nba = pd.read_csv(csv)

# 1 Query for player --> Player --> (1/2/3% numericos 1 jugador)  !!
# 2 Query for team --> Team --> for player in team: Query Player (numericos todos los jugadores, wins)
# 3 Visualization --> for team in teams --> Query Team --> numerico teams--> all teams (1,2,3, barplot)





    """

    age_players = df_nba["Age"]


    plt.hist(age_players)
    plt.title("Age players")

    count = 1
    my_file = Path(f"/Users/Stephi/Documents/academic/UOC/tercer_semestre/tipologia/PRAC1/skobsar_jordiba90_prac1/histogram/histogram_{count}.csv")

    if my_file.is_file():

        count = count + 1
        output = f"histogram_{count}.png"
        path = "/Users/Stephi/Documents/academic/UOC/tercer_semestre/tipologia/PRAC1/skobsar_jordiba90_prac1/histograms"
        output = os.path.join(path, output)
        plt.savefig(output)

    else:
        pass
    """




if __name__ == "__main__":

    csv_name = "nba_stats_1.csv"
    path = "/Users/Stephi/Documents/academic/UOC/tercer_semestre/tipologia/PRAC1/skobsar_jordiba90_prac1/output_csv"
    abs_path_input_df = os.path.join(path, csv_name)
    get_analysis(abs_path_input_df)

