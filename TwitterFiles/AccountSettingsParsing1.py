from  flask import Flask ,jsonify,Response

import tweepy
from tweepy import OAuthHandler
from urllib.parse import urlencode
import json
#from twitter import Twitter, OAuth, TwitterHTTPError, TwitterStream
#from TwitterFiles import Env
#from Env import api
#from tweepy.api import API

app=Flask(__name__)

@app.route('/account_settings_parsing',methods=['POST'])
def account_settings_parsing():

    consumer_key='zxwYSCOEug42LjRggdEsRJXo2'
    consumer_secret='KBgqcB0BDqH8ORacjaFqzM2N5qFgBskUx1wBm0FIaXlHf1RT5V'
    access_key='714494503822856193-fr3FGqtnNF0DnBHG4l6x56MRCdFmPwQ'
    access_secret='WReLl0jPAEHNCBZ3y2Ip8a1lyAWCZZuwbwjfZ70XOUo6G'

    auth = OAuthHandler(consumer_key,consumer_secret)
    api = tweepy.API(auth)
    auth.set_access_token(access_key,access_secret)

    user=api.get_settings()
    test=user['sleep_time']['enabled']
    test1=user['sleep_time']['end_time']

    print('null' if test is None else test )
    print(test1==None if test1 is None else test1 )
    print(test1)

    user_account={
       'screen_name':user['screen_name'],
       'language':user['language'],
       #'response_sleep_time':user['sleep_time'],
       'sleep_time_enabled': None if user['sleep_time']['enabled'] is None else user['sleep_time']['enabled']  ,
       'sleep_time_end_time':user['sleep_time']['end_time'],
       'sleep_time_start_time':user['sleep_time']['start_time']
    }
    
    #print(user_account['sleep_time_enabled'])

    #response_screen_name=user_account['screen_name']
   # response_language=user_account['language']
    #response_sleep_time=user_account['sleep_time']
    #response_sleep_time_enabled=user_account['sleep_time_enabled']
    # response_sleep_time_end_time=user_account['sleep_time_end_time']
    # response_sleep_time_start_time=user_account['sleep_time_start_time']
    #response_body =  response_screen_name,response_language,#response_sleep_time#response_sleep_time_enabled,response_sleep_time_end_time,response_sleep_time_start_time

    #response_body= {"message ":"Execution Done!"}
    #return Response(
        #response_body,
       # user_account
        #status=200
    #)
    

    return jsonify(user_account,user_account)

#return jsonify({'message':'User Account Settings parsed successfully'})
    

#if __name__ == '__main__':
app.run(port=5000)
#app.run(debug=True)