import pandas as pd

##Base de datos
eni_complete = pd.read_csv("data/eni_complete_T_secc.csv")
eni_complete = eni_complete.round(0)


