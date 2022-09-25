# -*- coding: utf-8 -*-
"""
Created on Sun Sep 27 22:35:36 2020

@author: sushanth
"""

import warnings
import itertools
import numpy as np
import pandas as pd
import statsmodels.api as sm
import matplotlib.pyplot as plt
plt.style.use('fivethirtyeight')
import os
import pymysql
from sqlalchemy import create_engine 


warnings.filterwarnings("ignore")


def Forecast(District_name,Market_name,commodity_name,Number_of_Days):
    global df
    engine = create_engine('mysql+pymysql://root:toor@localhost/agmarknet_data')
    
    df = pd.read_sql_table('west', engine, columns=['date','district','market','commodity','modal_price','Grade','Variety'])
    
    #df = pd.read_csv(os.getcwd() + os.path.sep + "final_data (1).csv")
    #########  Potato  ##########
    #District_name = 'Kolkata'
    #Market_name = 'Sealdah Koley Market'
    #commodity_name = 'Cabbage'
    #Number_of_Days = 7  # number of days 7 for weekly and #0 days For Month

    def get_commodity():
        data = df.groupby('district').get_group(District_name)  # district
        for market in data:
            market = data.groupby('market').get_group(Market_name)  # market
            for commodity in market:
                comm = market.groupby('commodity').get_group(commodity_name)  # commodity
                return comm
                # for grade in comm:
                #   comm_df = comm.groupby('Grade').get_group('Medium') # grade
                #  return comm_df

    df = get_commodity()

    ###########  Data Check  ###########
    ##########  Data Preprocessing  ###########
    def preprocess(df):
        # timestamps
        df['date'] = pd.to_datetime(df['date'])
        df = df.sort_values(by='date')
        df.reset_index(inplace=True)
        del df['index']
        df.index = pd.DatetimeIndex(df['date']).floor('D')
        df = df['modal_price']

        # removing duplicates
        df = df[~df.index.duplicated(keep='last')]

        # data imputation
        df = df.resample('D').interpolate()
        df = pd.DataFrame(df)
        return df

    df = preprocess(df)
    X = df.index.min()
    Y = df.index.max()
    # Taking the current year data
    df = df[X: Y]
    #########  Monthly Averages  #########
    y = df['modal_price'].resample('D').mean()

    ##############  ARIMA Model  ###############
    # The parameters p,d,q are account for seasonality, trend and noise which is resids
    def arima_model_optimization(y):
        p = d = q = range(0, 2)
        pdq = list(itertools.product(p, d, q))
        seasonal_pdq = [(x[0], x[1], x[2], 12) for x in list(itertools.product(p, d, q))]
        print('Examples of parameter combinations for Seasonal ARIMA...')
        print('SARIMAX: {} x {}'.format(pdq[1], seasonal_pdq[1]))
        print('SARIMAX: {} x {}'.format(pdq[1], seasonal_pdq[2]))
        print('SARIMAX: {} x {}'.format(pdq[2], seasonal_pdq[3]))
        print('SARIMAX: {} x {}'.format(pdq[2], seasonal_pdq[4]))
        # To avoid some overload warning messages
        for param in pdq:  # hyper parameter optimization for model selection
            for param_seasonal in seasonal_pdq:
                try:
                    model = sm.tsa.statespace.SARIMAX(y, order=param, seasonal_order=param_seasonal,
                                                      enforce_stationarity=False, enforce_invertibility=False)
                    results = model.fit()
                    print('ARIMA{}x{}12 - AIC:{}'.format(param, param_seasonal, results.aic))
                except:
                    continue

    arima_model_optimization(y)
    # Taking Lowest AIC parameters to fit the model
    # Fitting Params in Model
    ARIMA_model = sm.tsa.statespace.SARIMAX(y,
                                            order=(1, 1, 1),
                                            seasonal_order=(1, 1, 1, 12),
                                            enforce_stationarity=False,
                                            enforce_invertibility=False)
    model = ARIMA_model.fit()
    ##########  Forecasting Validation  ###########
    pred = model.get_prediction(start=pd.to_datetime('2019-01-01'), dynamic=False)
    pred_ci = pred.conf_int()
    ax = y['2016':'2019'].plot(label='observed')
    pred.predicted_mean.plot(ax=ax, label='One-step ahead Forecasted', alpha=.7, figsize=(10, 5))
    ax.fill_between(pred_ci.index,
                    pred_ci.iloc[:, 0],
                    pred_ci.iloc[:, 1], color='k', alpha=.2)
    ax.set_xlabel('Date')
    ax.set_ylabel('Price')
    plt.legend()
    plt.show()
    ##########  Future Forecasting  ###########
    # Forecasting the Future Price
    pred_uc = model.get_forecast(steps=Number_of_Days)  # or 30 for weekly or monthly
    pred_ci = pred_uc.conf_int()
    pred_ci.rename(columns={'lower modal_price':'Min Price','upper modal_price':'Max Price'}, inplace=True)
    return(pred_ci)

#df = pd.read_csv("D:/DATA SCIENCES/Forecasting/final_data (1).csv")
#final = Forecast('Kolkata','Sealdah Koley Market','Cabbage',7)
#print(final)
