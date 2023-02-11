# -*- coding: utf-8 -*-
"""
Created on Sun Jan 29 21:51:23 2023

@author: mukhe
"""
import pandas as pd

#file_name=pd.read_csv('file.csv')<-->read_csv
data=pd.read_csv('transaction.csv')
data=pd.read_csv('transaction.csv',sep=';')
#summary of the data
data.info()
#working with calculation

#variable=dataframe['Column_name']
CostPerItem=data['CostPerItem']
NumberOfItemsPurchased=data['NumberOfItemsPurchased']
CostPerTransaction=CostPerItem*NumberOfItemsPurchased
#Adding new column to dataframe
data['CostPerTransaction']=CostPerTransaction
#Other way of doing it
data['SalesPerTransaction']=data['SellingPricePerItem']*data['NumberOfItemsPurchased']
data['ProfitPerTransaction']=data['SalesPerTransaction']-data['CostPerTransaction']
data['Markup']=data['ProfitPerTransaction']/data['CostPerTransaction']
#Splitting the Columns
new = data["ClientKeywords"].str.split(",", n = -1, expand = True)
data["Demography"]= new[0]
data["Type"]= new[1]
data["AgeofInvolvement"]= new[2]

data["Demography"]=data["Demography"].str.replace('[','')  
data["AgeofInvolvement"]=data["AgeofInvolvement"].str.replace(']','')
#bringing new file
seasons=pd.read_csv('value_inc_seasons.csv',sep=';')
#merging files
data=pd.merge(data,seasons,on='Month')
#dropping coumuns-->data.drop(columns =["____"], inplace = True)
#data.drop(columns =["ClientKeywords"], inplace = True)
data.drop(columns =["Day"], inplace = True)
#data.drop(columns =["Year","Month"], inplace = True)
data.drop(columns =["Time"], inplace = True)
#export in csv
data.to_csv('ValueIncCleaned.csv',index=True)