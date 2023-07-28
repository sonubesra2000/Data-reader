import os
from os import environ, listdir

import pandas as pd 

from utils import process_and_save_ground_data

os.environ["O2POWER_PROCESSED_DATA_DIR"] = "C:/Users/Sonu/Desktop/O2/processed-data"
os.environ["O2POWER_DATA_DIR"] = "C:/Users/Sonu/Desktop/O2/data"

sitename='Gorai'

def update_data(df, sitename):
    old_csv_path = os.environ["O2POWER_DATA_DIR"] + f"/O2POWER_{sitename}.csv"

    try:
        df_init = pd.read_csv(old_csv_path)
        df_concat = pd.concat([df_init, df])
    except FileNotFoundError:
        df_concat = df
    df_concat = df_concat.drop_duplicates(subset='Time', keep='last').reset_index(drop=True)
    df_concat.to_csv(old_csv_path, index=False)
    return df_concat





