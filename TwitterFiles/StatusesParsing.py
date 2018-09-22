from  flask import Flask ,jsonify,Response

import tweepy
from tweepy import OAuthHandler
from urllib.parse import urlencode
import json

app=Flask(__name__)

@app.route('/statuses_parsing',methods=['POST'])
def statuses_parsing():

    consumer_key='zxwYSCOEug42LjRggdEsRJXo2'
    consumer_secret='KBgqcB0BDqH8ORacjaFqzM2N5qFgBskUx1wBm0FIaXlHf1RT5V'
    access_key='714494503822856193-fr3FGqtnNF0DnBHG4l6x56MRCdFmPwQ'
    access_secret='WReLl0jPAEHNCBZ3y2Ip8a1lyAWCZZuwbwjfZ70XOUo6G'

    auth = OAuthHandler(consumer_key,consumer_secret)
    api = tweepy.API(auth)
    auth.set_access_token(access_key,access_secret)
    
    
    tweets = api.user_timeline()
    print(tweets)
   
    return jsonify({'message':'User Account Details parsed successfully'})

    #take user_details and parse it
    #user_statuses={

        
    
   # }
    

   # response_name=user_profile_fields['name']
    #response_screen_name=user_profile_fields['screen_name']
   # response_body = response_name,response_screen_name
    #Response.append(profile)
   # return Response(
   #     response_body,
   #     status=200
   # )
  
    
#if __name__ == '__main__':
app.run(port=5000)
#app.run(debug=True)