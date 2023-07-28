from os import environ, listdir
import pandas as pd 
from api_reader import data_reader
from utils import process_and_save_ground_data
from update import update_data
from datetime import datetime,timedelta

if __name__ == "__main__":
        current_datetime = datetime.now()
        # start_date='01-01-2023 00:00'
        # end_date='27-07-2023 23:45'
        start_date =current_datetime.strftime('%d-%m-%Y 00:00')
        end_date = current_datetime.strftime('%d-%m-%Y 23:45')
        sitename='Gorai'
        data = data_reader(start_date, end_date)
        updatedf=update_data(data,sitename)
        # print(updatedf)
        process=process_and_save_ground_data(updatedf,sitename)


    
