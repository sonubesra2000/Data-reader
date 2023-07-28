import os
from os import environ
import pandas as pd
from numpy import nan
from pandas import Grouper, to_datetime
#from api_reader import data_reader

os.environ["O2POWER_PROCESSED_DATA_DIR"] = "C:/Users/Sonu/Desktop/O2/processed-data"
os.environ["O2POWER_DATA_DIR"] = "C:/Users/Sonu/Desktop/O2/data"


INDEX_NAME = "Time"
sitename='Gorai'

def process_and_save_ground_data(df,sitename):
    #print(df)
    saveraw(df,sitename)
    df = select_values(df,sitename)
    create_hourly_daily_monthly(df,sitename)

def saveraw(df,sitename):
    df.to_csv(
        environ["O2POWER_DATA_DIR"]
        + "/O2POWER_"
        + str(sitename)
        + ".csv"
    ,index=False)


def select_values(df,sitename):
    #print(df)
    df['Time']=pd.to_datetime(df['Time'])
    df.set_index('Time',inplace=True)
    df = df.sort_index()
    df = df.groupby(Grouper(freq="15T")).mean()
    df = df.astype(float)
    df['GHI']=0
    df = df.rename(columns={"PSEGPL_10MW Block1 WMS POA": 'Ground POA', "GHI": 'Ground GHI'}, errors="ignore")

    df.index.name = INDEX_NAME
    df = df.replace(nan, 0)
    df = round(df, 2)
    df.index = df.index.tz_localize("Asia/Kolkata")
    save_15min_ground_data(df,sitename)
    return df

def create_hourly_daily_monthly(df,sitename):
    ddf = df.groupby(Grouper(freq="H")).mean()
    save_hourly_ground_data(ddf,sitename)
    ddf = ddf.groupby(Grouper(freq="D")).sum() / 1000.0
    ddf.index.name = "Date"
    ddf = ddf.round(2)
    save_daily_ground_data(ddf,sitename)

    mdf = ddf.groupby(Grouper(freq="M")).sum()
    mdf.index.name = "Month"
    mdf.index = mdf.index.strftime("%b %Y")
    save_monthly_ground_data(mdf,sitename)


def save_15min_ground_data(df,sitename):
    df.to_csv(
        environ["O2POWER_PROCESSED_DATA_DIR"]
        + "/O2POWER_Subhourly_"
        + str(sitename)
        + ".csv"
    )

def save_hourly_ground_data(df, sitename):
    df.to_csv(
        environ["O2POWER_PROCESSED_DATA_DIR"] + "/O2POWER_Hourly_" + sitename + ".csv"
    )
    #print("-" * 50)
def save_daily_ground_data(df, sitename):
    # print(df)
    df.to_csv(environ["O2POWER_PROCESSED_DATA_DIR"] + "/O2POWER_Daily_" + sitename + ".csv")
    # print("=" * 50)
    #  
def save_monthly_ground_data(df, sitename):
    df.to_csv(
        environ["O2POWER_PROCESSED_DATA_DIR"] + "/O2POWER_Monthly_" + sitename + ".csv"
    )

