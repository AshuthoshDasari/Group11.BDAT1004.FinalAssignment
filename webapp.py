#importing libraries
from flask import Flask, render_template, request, jsonify
import json
import requests
import certifi
from pymongo import MongoClient
import time
import pandas as pd


app = Flask(__name__)
summary_url_temp="https://api.covid19api.com/summary" #api link


client = MongoClient("mongodb+srv://ashuthosh:test@ashuthoshcluster.wzfht.mongodb.net", tlsCAFile=certifi.where())
db = client.get_database('db')
records = db.data

x = records.find()


@app.route('/', methods=['GET','POST'])
def home():
    
    while True:
        for data in x:
            Global=data["Global"]
            new_deaths= Global["NewDeaths"]
            total_deaths=Global["TotalDeaths"]
            new_cases= Global["NewConfirmed"]
            total_cases=Global["TotalConfirmed"]
            new_recovered= Global["NewRecovered"]
            total_recovered=Global["TotalRecovered"]
            updated=data["Date"]

            return render_template("index.html",date=updated, nd_n=new_deaths, td_n=total_deaths,nc_n=new_cases,tc_n=total_cases,nr_n=new_recovered, tr_n=total_recovered)


def google_bar_chart():

    country_df = pd.DataFrame(columns=["Country", "TotalConfirmed", "TotalDeaths", "TotalRecovered"])
    while True:
        for data in x:
            countries_data=data["Countries"]
            for i in range(0, len(countries_data)):
                currentItem = countries_data[i]
                country_df.loc[i] = [countries_data[i]['Country'], countries_data[i]['TotalConfirmed'], countries_data[i]['TotalDeaths'], countries_data[i]['TotalRecovered']]
                CountryNames = country_df['Country']
                TotalConfirmed = country_df['TotalConfirmed']

                return render_template('index.html')



##testing 
# @app.route('/', methods=['GET','POST'])
# def home():
    
#     # response = requests.get(summary_url_temp)#get the response from the link
#     ##response = records.json()
#     if response.ok:
#         resp_data=response.json() #convert the response into json format
#         message=resp_data["Message"]
#         if (message!=""):
#             return(str(message) +"!! Please Refresh the page after few minutes")
#         else:
            
#             Global=resp_data["Global"]
#             new_deaths= Global["NewDeaths"]
#             total_deaths=Global["TotalDeaths"]
#             new_cases= Global["NewConfirmed"]
#             total_cases=Global["TotalConfirmed"]
#             new_recovered= Global["NewRecovered"]
#             total_recovered=Global["TotalRecovered"]
#             updated=resp_data["Date"]

#             return render_template("index.html",date=updated, nd_n=new_deaths, td_n=total_deaths,nc_n=new_cases,tc_n=total_cases,nr_n=new_recovered, tr_n=total_recovered)
#     else:
#         print(response.reason)







#### original code

# @app.route('/', methods=['GET','POST'])
# def home():
    
#     response = requests.get(summary_url_temp)#get the response from the link
#     # response = records.json()
#     if response.ok:
#         resp_data=response.json() #convert the response into json format
#         message=resp_data["Message"]
#         if (message!=""):
#             return(str(message) +"!! Please Refresh the page after few minutes")
#         else:
            
#             Global=resp_data["Global"]
#             new_deaths= Global["NewDeaths"]
#             total_deaths=Global["TotalDeaths"]
#             new_cases= Global["NewConfirmed"]
#             total_cases=Global["TotalConfirmed"]
#             new_recovered= Global["NewRecovered"]
#             total_recovered=Global["TotalRecovered"]
#             updated=resp_data["Date"]

#             return render_template("index.html",date=updated, nd_n=new_deaths, td_n=total_deaths,nc_n=new_cases,tc_n=total_cases,nr_n=new_recovered, tr_n=total_recovered)
#     else:
#         print(response.reason)




    
if __name__=="__main__":
    app.run(port=5085, debug="true")
