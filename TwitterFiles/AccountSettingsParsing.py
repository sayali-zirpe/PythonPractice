from  flask import Flask ,jsonify,Response

import tweepy
from tweepy import OAuthHandler
from urllib.parse import urlencode
import json
from twitter import Twitter, OAuth, TwitterHTTPError, TwitterStream
from tweepy.api import API

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
    print(user)

    screen_name=user['screen_name']
    print(screen_name)

    language=user['language']
    print(language)
    sleep_time=user['sleep_time']
    print(sleep_time)

    sleep_time_enabled=user['sleep_time']['enabled']
    print(sleep_time_enabled)

    sleep_time_end_time=user['sleep_time']['end_time']
    print(sleep_time_end_time)

    sleep_time=user['sleep_time']['start_time']
    print(sleep_time)

    

    #time_zone=user['time_zone']
   # print(time_zone)
    #trend_location=user['trend_location']
   # print( trend_location)





   # user_profile_fields={

        #'name':user.name,
       # 'screen_name':user.screen_name,
        #'location':user.location,
        


    #response_name=user_profile_fields['name']
    #response_screen_name=user_profile_fields['screen_name']
    #response_body = response_name,response_screen_name
    #Response.append(profile)
    #return Response(
     #   response_body,
      #  status=200
   # )
    return jsonify({'message':'User Account Settings parsed successfully'})
    



#if __name__ == '__main__':
app.run(port=5000)
#app.run(debug=True)