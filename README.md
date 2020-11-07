# skobsar_jordiba90_prac1
PRAC 1 asignatura tipología de datos, Master Degree Data Science, UOC. Semestre 1 curso 20/21.

Extracción de datos estadísticos sobre el rendimiento de los jugadores de la NBA para determinar las relaciones que hay entre las diferentes métricas, el rendimiento y las victorias de un equipo en una temporada. 


Extracción de la información en forma de csv:

How to use:
```
#export PYTHONPATH

python scraping_basket/main.py
open ouput_csv/nba_stats.csv
```

nba_stats per year csv description: 

'Player': Name of the player
'Pos': Position of the player
'Age': Age
'Tm': Team
'G': Games
'GS': Games Started
'MP': Minutes Played Per Game
'FG': field goals per game
'FGA': Field goals attempts per game
'FG%': field goal %
'3P': 3 points fg per gam
'3PA': 3 points attempts per game
'3P%': 3 point %
'2P': 2 points fg per game
'2PA': 2 points attempts per game
'2P%': 2 point %
'eFG%': Effective field goal % (This statistic adjusts for the fact that a 3-point field goal is worth one more point than a 2-point field goal.)
'FT': free throws per game
'FTA': free throws attempts per game
'FT%': free throws %
'ORB': offensive rebounds per game
'DRB': defensive rebounds per game
'TRB': total rebounds per game
'AST': Assists per game
'STL': Steals per game
'BLK': blocks per game
'TOV': turnovers per game
'PF': Personal Fouls per game
'PTS': points per game


