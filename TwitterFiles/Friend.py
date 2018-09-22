from  flask import Flask ,jsonify,Response

import tweepy
from tweepy import OAuthHandler
from urllib.parse import urlencode
import json
from twitter import Twitter, OAuth, TwitterHTTPError, TwitterStream
from tweepy.api import API

app=Flask(__name__)

@app.route('/friends_list',methods=['POST'])
def friends_list():

    consumer_key='zxwYSCOEug42LjRggdEsRJXo2'
    consumer_secret='KBgqcB0BDqH8ORacjaFqzM2N5qFgBskUx1wBm0FIaXlHf1RT5V'
    access_key='714494503822856193-fr3FGqtnNF0DnBHG4l6x56MRCdFmPwQ'
    access_secret='WReLl0jPAEHNCBZ3y2Ip8a1lyAWCZZuwbwjfZ70XOUo6G'

    auth = OAuthHandler(consumer_key,consumer_secret)
    api = tweepy.API(auth)
    auth.set_access_token(access_key,access_secret)

    test=api.friends()
    print(test)
    
   # user1=test.user
    #print(user1)
    name=test[0].name
    print(name)

    screen_name=test[0].screen_name
    print(screen_name)

    id=test[0].id
    print(id)

    profile_image_url=test[0].profile_image_url
    print(profile_image_url)

    created_at=test[0].created_at
    print(created_at)

    location=test[0].location
    print(location)

    favorites_count=test[0].favourites_count
    print(favorites_count)

    url=test[0].url
    print(url)

    listed_count=test[0].listed_count
    print(listed_count)
    
    lang=test[0].lang
    print(lang)

    followers_count=test[0].followers_count
    print(followers_count)
  
    time_zone=test[0].time_zone
    print(time_zone)

    description=test[0].description
    print(description)

    statuses_count=test[0].statuses_count
    print(statuses_count)


    friends_count=test[0].friends_count
    print(friends_count)






    #users: friendsShow.users 
   # friendsShow.users.map((usr) => ({
    #name: user.name
   # screen_name: usr.screen_name
   # id: usr.id
   # profile_image_url: usr.profile_image_url 
   # created_at: usr.created_at
    #location: usr.location 
    #favorites_count: usr.favorites_count 
    #url: usr.url
   # listed_count: usr.listed_count
   # lang: usr.lang,
   # followers_count: usr.followers_count
   # time_zone: usr.time_zone
   # description: usr.description
   # statuses_count: usr.statuses_count
   # friends_count: usr.friends_count






    #friends_list={
    #   'screen_name':user['screen_name'],
      # 'language':user['language'],
      # 'sleep_time':user['sleep_time'],
       #'sleep_time_enabled':user['sleep_time']['enabled'],
       #'sleep_time_end_time':user['sleep_time']['end_time'],
       #'sleep_time_start_time':user['sleep_time']['start_time']
   # }


   # response_screen_name=user_account['screen_name']
  #  response_language=user_account['language']
   # response_sleep_time=user_account['sleep_time']
   # response_sleep_time_enabled=user_account['sleep_time_enabled']
   # response_sleep_time_end_time=user_account['sleep_time_end_time']
   # response_sleep_time_start_time=user_account['sleep_time_start_time']
   # response_body =  response_screen_name, response_language,response_sleep_time,response_sleep_time_enabled,response_sleep_time_end_time,response_sleep_time_start_time
    #Response.append(profile)
   # return Response(
   #     response_body,
  #      status=200
  #  )
    

    return jsonify({'message':'Friends details parsed successfully'})
    

#if __name__ == '__main__':
app.run(port=5000)
#app.run(debug=True)