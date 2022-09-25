# -*- coding: utf-8 -*-
"""
Created on Fri Oct  9 18:11:10 2020

@author: sushanth
"""

#merging the files
import pandas as pd
import glob
import os

import time
import pymysql
import pandas as pd
from sqlalchemy import create_engine
import shutil


def Pre_Raw():
    today1 = time.strftime('%d %b %Y')
    glb = glob.glob(os.getcwd() + os.path.sep + "Temp_DataBase" + os.path.sep + "*.xls")
    a_dta = pd.DataFrame()
    for g in glb:
        s_data = pd.read_html(g)
        a_dta = a_dta.append(s_data, ignore_index=True)
    # removing no data found records and filling State Name
    ndf = a_dta[(a_dta['State Name'] == 'No Data Found')].index
    a_dta.drop(ndf, inplace=True)
    a_dta['State Name'].fillna("west bengal", inplace=True)
    # dropping unused columns
    a_dta.columns
    a_dta = a_dta.iloc[:, [11,2, 3, 5, 6, 7, 14]]
    a_dta.rename(columns={'State Name': 'state', 'District Name': 'district',
                         'Market Name': 'market',
                          'Commodity': 'commodity',
                          'Modal Price (Rs./Quintal)': 'modal_price',
                          'Price Date': 'date'}, inplace=True)
    a_dta.to_csv(os.getcwd() + os.path.sep + 'DataBase' + os.path.sep + 'Final-Merged - ' + today1 + '.csv')
    ######  Inserting Data Into DB  ######
    engine = create_engine("mysql+pymysql://root:toor@localhost/agmarknet_data")
    df = pd.read_csv(os.getcwd() + os.path.sep + 'DataBase' + os.path.sep + 'Final-Merged - ' + today1 + '.csv')
    del df['Unnamed: 0']
    df['date']= pd.to_datetime(df['date'])# converting date to ecaxt format
    df.to_sql(
        name='west',
        con=engine,
        index=False,
        if_exists='append'
    )
    path = os.getcwd() + os.path.sep + "Temp_DataBase" + os.path.sep
    commodity1 = os.getcwd() + os.path.sep + "DataBase" + os.path.sep + "Commodity1"
    commodity2 = os.getcwd() + os.path.sep + "DataBase" + os.path.sep + "Commodity2"
    commodity3 = os.getcwd() + os.path.sep + "DataBase" + os.path.sep + "Commodity3"
    commodity4 = os.getcwd() + os.path.sep + "DataBase" + os.path.sep + "Commodity4"
    commodity5 = os.getcwd() + os.path.sep + "DataBase" + os.path.sep + "Commodity5"
    shutil.rmtree(path)
    shutil.rmtree(commodity1)
    shutil.rmtree(commodity2)
    shutil.rmtree(commodity3)
    shutil.rmtree(commodity4)
    shutil.rmtree(commodity5)
    Z="Plese wait until data is stored in data Base"
    return(Z)




