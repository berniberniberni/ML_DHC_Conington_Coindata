import pandas as pd

def load_conington_register(path="../data/A14_Conington_coin_data02.csv"):
    return pd.read_csv(path)