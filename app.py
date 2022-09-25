# -*- coding: utf-8 -*-
"""
Created on Fri Oct  9 18:11:10 2020

@author: sushanth
"""

from flask import *
import pandas as pd
import numpy
import os 
import fetch as fs
import Scraping_test as sp


app = Flask(__name__)

@app.route('/')
def home():
    return render_template('Main.html')

@app.route("/scrape",methods=['POST'])
def scrape():
    X = sp.final()
    return render_template('output.html')

@app.route("/report",methods=['POST'])
def report():
    
    return render_template('index.html')


@app.route("/predict",methods=['POST'])
def predict():
    input_District = request.form['District']
    input_Commodity = request.form['Commodity']
    input_Market = request.form['Market']
    input_Days = request.form['Days']
    data1=fs.Forecast(input_District,input_Market,input_Commodity,int(input_Days))
    return render_template('output1.html' , tables=[data1.to_html(classes='data1')])  
    
if __name__ == "__main__":
    app.run(debug=True, use_reloader=False)