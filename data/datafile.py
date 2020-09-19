import pandas as pd
import xlrd
import os
#-------------for geography--------------------#
from geopy.geocoders import Nominatim
from geopy.extra.rate_limiter import RateLimiter
geolocator = Nominatim(user_agent="my-dashboard")
geocode = RateLimiter(geolocator.geocode, min_delay_seconds=1)

def update():
    #Here you can define your database connection crediential to connect to the source system
    cwd_old = os.getcwd()
    new = cwd_old+'\data'
    os.chdir(new)
    df = pd.read_excel('US Superstore data.xls')
    df.to_csv('complete.csv')
    os.chdir(cwd_old)
    return df

def complete():
    cwd_old = os.getcwd()
    new = cwd_old+'\data'
    os.chdir(new)
    try:
        df = pd.read_csv('complete.csv')
    except:
        df = pd.read_excel('US Superstore data.xls')
    os.chdir(cwd_old)
    return df

def sales_sub():
    cwd_old = os.getcwd()
    new = cwd_old+'\data'
    os.chdir(new)
    try:
        df = pd.read_csv('complete.csv')
    except:
        df = pd.read_excel('US Superstore data.xls')
    os.chdir(cwd_old)
    
    d = []
    for i in df['Sub-Category'].unique():
        sales = round(df[df['Sub-Category']==i]['Sales'].sum(),2)
        profit = round(df[df['Sub-Category']==i]['Profit'].sum(),2)
        d.append([i,sales,profit])
    temp = pd.DataFrame(d,columns=['Sub-Category','Sales','Profit'])
    temp = temp.sort_values('Sales',ascending=True)
    return temp

def sales_week():
    cwd_old = os.getcwd()
    new = cwd_old+'\data'
    os.chdir(new)
    try:
        df = pd.read_csv('complete.csv')
    except:
        df = pd.read_excel('US Superstore data.xls')
    os.chdir(cwd_old)

    df['Order Date'] = pd.to_datetime(df['Order Date'],errors='coerce')
    # df['Lead Time'] = (df['Ship Date'] - df['Order Date']).dt.days
    df['Week'] = df['Order Date'].dt.week
    df['Year'] = df['Order Date'].dt.year

    week14 = df[df['Year']==2014][['Week','Sales']].groupby(['Week']).sum()
    week15 = df[df['Year']==2015][['Week','Sales']].groupby(['Week']).sum()
    week16 = df[df['Year']==2016][['Week','Sales']].groupby(['Week']).sum()
    week17 = df[df['Year']==2017][['Week','Sales']].groupby(['Week']).sum()

    week14.rename(columns={'Sales':'Sales14'},inplace=True)
    week15.rename(columns={'Sales':'Sales15'},inplace=True)
    week16.rename(columns={'Sales':'Sales16'},inplace=True)
    week17.rename(columns={'Sales':'Sales17'},inplace=True)
    
    return week14.join(week15,on='Week').join(week16,on='Week').join(week17,on='Week')

def sales_month():
    cwd_old = os.getcwd()
    new = cwd_old+'\data'
    os.chdir(new)
    try:
        df = pd.read_csv('complete.csv')
    except:
        df = pd.read_excel('US Superstore data.xls')
    os.chdir(cwd_old)

    df['Order Date'] = pd.to_datetime(df['Order Date'],errors='coerce')
    df['Year'] = df['Order Date'].dt.year
    df['Month'] = df['Order Date'].dt.month

    month14 = df[df['Year']==2014][['Month','Sales']].groupby(['Month']).sum()
    month15 = df[df['Year']==2015][['Month','Sales']].groupby(['Month']).sum()
    month16 = df[df['Year']==2016][['Month','Sales']].groupby(['Month']).sum()
    month17 = df[df['Year']==2017][['Month','Sales']].groupby(['Month']).sum()

    month14.rename(columns={'Sales':'Sales14'},inplace=True)
    month15.rename(columns={'Sales':'Sales15'},inplace=True)
    month16.rename(columns={'Sales':'Sales16'},inplace=True)
    month17.rename(columns={'Sales':'Sales17'},inplace=True)

    return month14.join(month15,on='Month').join(month16,on='Month').join(month17,on='Month')

def geography():
    cwd_old = os.getcwd()
    new = cwd_old+'\data'
    os.chdir(new)
    try:
        df = pd.read_csv('complete.csv')
        df_geography = pd.read_csv('geography.csv')
    except:
        df = pd.read_excel('US Superstore data.xls')
    address_new = set(df.City.unique()) - set(df_geography.City.unique())

    l = []
    if address_new:
        for address in address_new:
            location = geocode(address)
            l.append([address,location.latitude,location.longitude])
        df_geography_new = pd.DataFrame(l,columns=['City','Latitude','Longitude'])
        df_geography = df_geography.append(df_geography_new,ignore_index=True)
        df_geography = df_geography[['City','Latitude','Longitude']]
        del df_geography_new
        df_geography.to_csv('geography.csv')
    os.chdir(cwd_old)
    return pd.merge(df,df_geography,on='City',how='left')[['City','Profit','Sales','Latitude','Longitude']]

def regionwise():
    cwd_old = os.getcwd()
    new = cwd_old+'\data'
    os.chdir(new)
    try:
        df = pd.read_csv('complete.csv')
        df_geography = pd.read_csv('geography.csv')
    except:
        df = pd.read_excel('US Superstore data.xls')
    os.chdir(cwd_old)
    return df

