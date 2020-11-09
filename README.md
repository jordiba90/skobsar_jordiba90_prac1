
# PRAC 1 asignatura tipología de datos, Master Degree Data Science, UOC. Semestre 1 curso 20/21. <h1> 

## Extracción de datos estadísticos sobre el rendimiento de los jugadores de la NBA para determinar las relaciones que hay entre las diferentes métricas, el rendimiento y las victorias de un equipo en una temporada. 

###Extracción de la información en forma de csv 



####**How to use:**
```
export PYTHONPATH=/path/to/your/machine/here
python scraping_basket/main.py
open ouput_csv/nba_stats.csv
```

####**Example:**

```
export PYTHONPATH=/Users/Stephi/Documents/academic/UOC/tercer_semestre/tipologia/PRAC1/skobsar_jordiba90_prac1
python scraping_basket/main.py
open ouput_csv/nba_stats.csv
```

####**nba_stats per year csv description:** 

| Campo | Descripción |
| :---: |   :---:     |
| Player  | Name of the player |
| Pos  | Position of the player |
|Age| Age|
|Tm| Team|
|G| Games|
|GS| Games Started|
|MP| Minutes Played Per Game|
|FG| field goals per game|
|FGA| Field goals attempts per game|
|FG%| field goal %|
|3P'| 3 points fg per gam|
|3PA| 3 points attempts per game|
|3P%| 3 point %|
|2P'| 2 points fg per game|
|2PA| 2 points attempts per game|
|2P%'| 2 point %|
|eFG%  |Effective field goal % (This statistic adjusts for the fact that a 3-point field goal is worth one more point than a 2-point field goal.)|
|FT  | free throws per game|
|FTA  |free throws attempts per game|
|FT%  |free throws %|
|ORB  | offensive rebounds per game|
|DRB| defensive rebounds per game|
|TRB| total rebounds per game|
|AST| Assists per game|
|STL| Steals per game|
|BLK| blocks per game|
|TOV| turnovers per game|
|PF| Personal Fouls per game|
|PTS| points per game|

###Preprocessing the data automation:

####Automate generation of all variable histograms to preprocess the data: 

![GitHub Logo](/Users/Stephi/Desktop/BLK.png)
![GitHub Logo](/Users/Stephi/Desktop/FG.png)

# Current status and future prospects


- [X] Web Scrapping to extract the nba stats and convert it to a csv file
- [X] Preprocessing of data: Missing value treatment
- [X] Get first metrics 

- [] Answer the initial hypothesis relating the FG data off al players, then related it with the team data for a given year and correlate if a lower %2FG in mid distance throw turns in higher victories to a team in a season. 



