import numpy as np
import pandas as pd

fifa = pd.read_csv(r'/Users/zac/Downloads/archive/players_22.csv')

fifa[club_position].value_count()

