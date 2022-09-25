#*- coding: utf-8 -*-
"""
Created on Sun Sep 27 22:35:36 2020

@author: sushanth
"""
import os
import glob
import shutil
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from datetime import date, datetime, timedelta
import functools 
import operator  


####################### Paths reqiured for commodity ##########################

def web():
    commodity1 = os.getcwd() + os.path.sep + "DataBase" + os.path.sep + "Commodity1"
    commodity2 = os.getcwd() + os.path.sep + "DataBase" + os.path.sep + "Commodity2"
    commodity3 = os.getcwd() + os.path.sep + "DataBase" + os.path.sep + "Commodity3"
    commodity4 = os.getcwd() + os.path.sep + "DataBase" + os.path.sep + "Commodity4"
    commodity5 = os.getcwd() + os.path.sep + "DataBase" + os.path.sep + "Commodity5"
    
    # checking for  temporary files
    if os.path.exists(commodity1):
        shutil.rmtree(commodity1)
    else:
        os.mkdir(commodity1)

    if os.path.exists(commodity2):
       shutil.rmtree(commodity2)
    else:
        os.mkdir(commodity2)        

    if os.path.exists(commodity3):
        shutil.rmtree(commodity3)
    else:
        os.mkdir(commodity3)
    
    if os.path.exists(commodity4):
        shutil.rmtree(commodity4)
    else:
        os.mkdir(commodity4)
    
    if os.path.exists(commodity5):
        shutil.rmtree(commodity5)
    else:
        os.mkdir(commodity5)
        
    if os.path.exists(os.getcwd() + os.path.sep + "Temp_DataBase"):
        shutil.rmtree(os.getcwd() + os.path.sep + "Temp_DataBase")
    else:
        print("No Temporary Files")
    webdriver1=('C:\\Program Files (x86)\\chromedriver.exe')
    ###################### Automate date for data extraction ######################
    today = datetime.now()
    #dd = today - timedelta(days=30)
    #dd_str = dd.strftime("%#d-%#b-%Y")
    #from mysql.connector import Error
    import MySQLdb
    connection = MySQLdb.connect(host="localhost",database='agmarknet_data', user="root",passwd="toor")
    cursor = connection.cursor()
    sql_select_query = "SELECT max(date) FROM agmarknet_data.west;"
    cursor.execute(sql_select_query)
    record = cursor.fetchone()
    print(record)
    def convertTuple(tup): 
        str = functools.reduce(operator.add, (tup)) 
        return str
  
    # Driver code 
    tuple = (record) 
    str = convertTuple(tuple) 
    print(str)

    dd_str= str.strftime("%d-%b-%Y")
    print(dd_str)


    ###############################################################################
    ################################commodity no- 17 ##############################
    ###############################################################################
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    # options.add_argument("--start-maximized")
    prefs = {"profile.default_content_settings.popups": 0,
             "download.default_directory":
                 commodity1,
             "directory_upgrade": True}
    options.add_experimental_option("prefs", prefs)
    driver = webdriver.Chrome(webdriver1, options=options)
    driver.get("https://agmarknet.gov.in/")
    driver.implicitly_wait(600)
    dropdown = Select(driver.find_element_by_id("ddlCommodity"))
    commodity = driver.find_element_by_id('ddlCommodity')
    # required commodity values
    commodities = ['17']
    for option in commodities:
        dropdown = Select(driver.find_element_by_id("ddlCommodity"))
        dropdown.select_by_value(option)

        # From Date
        start_date = driver.find_element_by_id('txtDate').clear()
        start_date = driver.find_element_by_id('txtDate')
        start_date.send_keys(dd_str)

        # State
        state = driver.find_element_by_id('ddlState')
        state.send_keys("West Bengal")

        district = driver.find_element_by_id('ddlDistrict')
        district.send_keys("Kolkata")

        search = driver.find_element_by_id('btnGo')
        search.click()
        driver.implicitly_wait(2000)

        importtoexcel = driver.find_element_by_id('cphBody_ButtonExcel')
        importtoexcel.click()
        home = driver.find_element_by_class_name('home')
        home.click()
        driver.implicitly_wait(2000)
    driver.quit
    ###############################################################################
    ############################## commodity no- 19 ###############################
    ###############################################################################
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    # options.add_argument("--start-maximized")
    prefs = {"profile.default_content_settings.popups": 0,
             "download.default_directory":
                 commodity2,
             "directory_upgrade": True}
    options.add_experimental_option("prefs", prefs)
    driver = webdriver.Chrome(webdriver1, options=options)
    driver.get("https://agmarknet.gov.in/")
    driver.implicitly_wait(600)
    dropdown = Select(driver.find_element_by_id("ddlCommodity"))
    commodity = driver.find_element_by_id('ddlCommodity')
    # required commodity values
    commodities = ['19']
    for option in commodities:
        dropdown = Select(driver.find_element_by_id("ddlCommodity"))
        dropdown.select_by_value(option)

        # From Date
        start_date = driver.find_element_by_id('txtDate').clear()
        start_date = driver.find_element_by_id('txtDate')
        start_date.send_keys(dd_str)

        # State
        state = driver.find_element_by_id('ddlState')
        state.send_keys("West Bengal")

        district = driver.find_element_by_id('ddlDistrict')
        district.send_keys("Kolkata")

        search = driver.find_element_by_id('btnGo')
        search.click()
        driver.implicitly_wait(2000)

        importtoexcel = driver.find_element_by_id('cphBody_ButtonExcel')
        importtoexcel.click()
        home = driver.find_element_by_class_name('home')
        home.click()
        driver.implicitly_wait(2000)
    driver.quit
    ###############################################################################
    ################################ commodity no-23 ##############################
    ###############################################################################
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    # options.add_argument("--start-maximized")
    prefs = {"profile.default_content_settings.popups": 0,
             "download.default_directory":
                 commodity3,
             "directory_upgrade": True}
    options.add_experimental_option("prefs", prefs)
    driver = webdriver.Chrome(webdriver1, options=options)
    driver.get("https://agmarknet.gov.in/")
    driver.implicitly_wait(600)
    dropdown = Select(driver.find_element_by_id("ddlCommodity"))
    commodity = driver.find_element_by_id('ddlCommodity')
    # required commodity values
    commodities = ['23']
    for option in commodities:
        dropdown = Select(driver.find_element_by_id("ddlCommodity"))
        dropdown.select_by_value(option)

        # From Date
        start_date = driver.find_element_by_id('txtDate').clear()
        start_date = driver.find_element_by_id('txtDate')
        start_date.send_keys(dd_str)

        # State
        state = driver.find_element_by_id('ddlState')
        state.send_keys("West Bengal")

        district = driver.find_element_by_id('ddlDistrict')
        district.send_keys("Kolkata")

        search = driver.find_element_by_id('btnGo')
        search.click()
        driver.implicitly_wait(2000)

        importtoexcel = driver.find_element_by_id('cphBody_ButtonExcel')
        importtoexcel.click()
        home = driver.find_element_by_class_name('home')
        home.click()
        driver.implicitly_wait(2000)
    driver.quit
    ###############################################################################
    ############################### commodity no-24 ###############################
    ###############################################################################
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    # options.add_argument("--start-maximized")
    prefs = {"profile.default_content_settings.popups": 0,
             "download.default_directory":
                 commodity4,
             "directory_upgrade": True}
    options.add_experimental_option("prefs", prefs)
    driver = webdriver.Chrome(webdriver1, options=options)
    driver.get("https://agmarknet.gov.in/")
    driver.implicitly_wait(600)
    dropdown = Select(driver.find_element_by_id("ddlCommodity"))
    commodity = driver.find_element_by_id('ddlCommodity')
    # required commodity values
    commodities = ['24']
    for option in commodities:
        dropdown = Select(driver.find_element_by_id("ddlCommodity"))
        dropdown.select_by_value(option)

        # From Date
        start_date = driver.find_element_by_id('txtDate').clear()
        start_date = driver.find_element_by_id('txtDate')
        start_date.send_keys(dd_str)

        # State
        state = driver.find_element_by_id('ddlState')
        state.send_keys("West Bengal")

        district = driver.find_element_by_id('ddlDistrict')
        district.send_keys("Kolkata")

        search = driver.find_element_by_id('btnGo')
        search.click()
        driver.implicitly_wait(2000)

        importtoexcel = driver.find_element_by_id('cphBody_ButtonExcel')
        importtoexcel.click()
        home = driver.find_element_by_class_name('home')
        home.click()
        driver.implicitly_wait(2000)
    driver.quit
    ###############################################################################
    ############################### commodity no-154 ##############################
    ###############################################################################
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    # options.add_argument("--start-maximized")
    prefs = {"profile.default_content_settings.popups": 0,
             "download.default_directory":
                 commodity5,
             "directory_upgrade": True}
    options.add_experimental_option("prefs", prefs)
    driver = webdriver.Chrome(webdriver1, options=options)
    driver.get("https://agmarknet.gov.in/")
    driver.implicitly_wait(600)
    dropdown = Select(driver.find_element_by_id("ddlCommodity"))
    commodity = driver.find_element_by_id('ddlCommodity')
    # required commodity values
    commodities = ['154']
    for option in commodities:
        dropdown = Select(driver.find_element_by_id("ddlCommodity"))
        dropdown.select_by_value(option)

        # From Date
        start_date = driver.find_element_by_id('txtDate').clear()
        start_date = driver.find_element_by_id('txtDate')
        start_date.send_keys(dd_str)

        # State
        state = driver.find_element_by_id('ddlState')
        state.send_keys("West Bengal")

        district = driver.find_element_by_id('ddlDistrict')
        district.send_keys("Kolkata")

        search = driver.find_element_by_id('btnGo')
        search.click()
        driver.implicitly_wait(2000)

        importtoexcel = driver.find_element_by_id('cphBody_ButtonExcel')
        importtoexcel.click()
        home = driver.find_element_by_class_name('home')
        home.click()
        driver.implicitly_wait(2000)
    driver.quit
    X = "Please Wait until updation in DB"
    #####################################END#######################################
    ###############################################################################
    return(X)



