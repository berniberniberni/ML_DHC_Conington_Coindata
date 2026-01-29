import numpy as np

def add_date_features(df):
    df = df.copy()
    df["mid_date"] = (df["COIN_EDATE"] + df["COIN_LDATE"]) / 2
    df["date_span"] = df["COIN_LDATE"] - df["COIN_EDATE"]
    return df
