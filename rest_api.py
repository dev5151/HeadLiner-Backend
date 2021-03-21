from flask import Flask, request, jsonify 
from textblob import TextBlob
import pandas as pd 
import requests
import json

     
# creating a Flask application
app = Flask(__name__)




@app.route("/all")

def fetchNews():

    news_api_url = ('http://newsapi.org/v2/top-headlines?''country=in&''apiKey=6efd3ee1e13b448a8e1c8b4c45ec0bc7')
    
    response = requests.get(news_api_url)

    data=response.json()
    
    return jsonify(data['articles'])
    

@app.route("/positive",methods=['GET'])

def fetchPositiveNews():
    list=[]
    titleList=[]
    positiveNews=[]
    newPositiveNews=[]
    totalLength=0

    news_api_url = ('http://newsapi.org/v2/top-headlines?''country=in&''apiKey=6efd3ee1e13b448a8e1c8b4c45ec0bc7')
    
    response = requests.get(news_api_url)

    data=response.json()

    totalLength=(len(data["articles"]))



    for i in range (0,totalLength):
        content = data["articles"][i]["description"]
        if not content :
            list.append(i)
        else:
            blob=TextBlob(content)
            titleList.append((i,blob.sentiment[0]))
        
    
    print(titleList) 
    print(list)

    for i in titleList:
        if 0<i[1]<=1:
            positiveNews.append(i[0])

    for i in range (0,totalLength):
        if i in positiveNews:
            newPositiveNews.append(data["articles"][i])

    return jsonify(newPositiveNews)

@app.route("/negative",methods=['GET'])

def fetchNegativeNews():

    list=[]
    titleList=[]
    negativeNews=[]
    totalLength=0
    newNegativeNews=[]
 

    news_api_url = ('http://newsapi.org/v2/top-headlines?''country=in&''apiKey=6efd3ee1e13b448a8e1c8b4c45ec0bc7')
    
    response = requests.get(news_api_url)

    data=response.json()

    print (json.dumps(data,indent=3))

    totalLength=(len(data["articles"]))

    for i in range (0,totalLength):
        content = data["articles"][i]["description"]
        if not content :
            list.append(i)
        else:
            blob=TextBlob(content)
            titleList.append((i,blob.sentiment[0]))
    
    for i in titleList:
        if -1<=i[1]<0:
            negativeNews.append(i[0])
        
    for i in range (0,totalLength):
        if i in negativeNews:
            newNegativeNews.append(data["articles"][i])

    return jsonify(newNegativeNews)

@app.route("/neutral",methods=['GET'])

def fetchNeutralNews():

    list=[]
    titleList=[]
    neutralNews=[]
    totalLength=0
    newNeutralNews=[]

    news_api_url = ('http://newsapi.org/v2/top-headlines?''country=in&''apiKey=6efd3ee1e13b448a8e1c8b4c45ec0bc7')
    
    response = requests.get(news_api_url)

    data=response.json()


    totalLength=(len(data["articles"]))


    for i in range (0,totalLength):
        content = data["articles"][i]["description"]
        if not content :
            list.append(i)
        else:
            blob=TextBlob(content)
            titleList.append((i,blob.sentiment[0]))

    for i in titleList:
        if i[1]==0:
            neutralNews.append(i[0])

    for i in range (0,totalLength):
        if i in neutralNews:
            newNeutralNews.append(data["articles"][i])

    return jsonify(newNeutralNews)


if __name__=='__main__':
    app.run(port=5000,debug=True)   