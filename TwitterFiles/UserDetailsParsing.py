from  flask import Flask ,jsonify,Response

import tweepy
from tweepy import OAuthHandler
from urllib.parse import urlencode
import json
from tweepy.api import API

app=Flask(__name__)

@app.route('/user_details_parsing',methods=['POST'])
def user_details_parsing():

    consumer_key='zxwYSCOEug42LjRggdEsRJXo2'
    consumer_secret='KBgqcB0BDqH8ORacjaFqzM2N5qFgBskUx1wBm0FIaXlHf1RT5V'
    access_key='714494503822856193-fr3FGqtnNF0DnBHG4l6x56MRCdFmPwQ'
    access_secret='WReLl0jPAEHNCBZ3y2Ip8a1lyAWCZZuwbwjfZ70XOUo6G'

    auth = OAuthHandler(consumer_key,consumer_secret)
    api = tweepy.API(auth)
    auth.set_access_token(access_key,access_secret)
    
    user=api.verify_credentials()
   
    #take user_details and parse it
    user_profile_fields={

        'name':user.name,
        'screen_name':user.screen_name,
        'location':user.location,
        'description':user.description,
        'url':user.url,
        'entities':user.entities,
        'followers_count': user.followers_count,
        'friends_count':user.friends_count,
        'listed_count':user.listed_count,
        'created_at':user.created_at,
        'time_zone':user.time_zone,
        'statuses_count': user.statuses_count,
        'lang':user.lang,
        'status':user.status,
        'created_at':user.status.created_at,
        'text':user.status.text, 
        'entities':user.status.entities,
        'hashtags':user.status.entities['hashtags'], 
        'user_mentions_screen_name':user.status.entities['user_mentions'][0]['screen_name'],
        'user_mentions_name':user.status.entities['user_mentions'][0]['name'],
        'urls':user.status.entities['urls'], 
        'source':user.status.source, 
        'geo':user.status.geo, 
        'cordinates':user.status.coordinates, 
        'contributors':user.status.contributors, 
        'retweet_count':user.status.retweet_count, 
        'favorite_count':user.status.favorite_count,
        'favorited':user.status.favorited,
        'retweeted':user.status.retweeted,
        'lang':user.status.lang,
        'profile_image_url':user.profile_image_url
    
    }
    

    response_name=user_profile_fields['name']
    response_screen_name=user_profile_fields['screen_name']
    response_body = response_name,response_screen_name
    #Response.append(profile)
    return Response(
        response_body,
        status=200
    )
   # return jsonify({'message':'User Account Details parsed successfully'})
    



#if __name__ == '__main__':
app.run(port=5000)
#app.run(debug=True)