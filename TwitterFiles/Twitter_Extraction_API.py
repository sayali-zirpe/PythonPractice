# Twitter Extraction API 

from  flask import Flask ,jsonify,Response
from tweepy import OAuthHandler
import tweepy
import json

app=Flask(__name__)

@app.route('/Twitter_API')
def Twitter_API ():
    
    # authentication
    consumer_key='zxwYSCOEug42LjRggdEsRJXo2'
    consumer_secret='KBgqcB0BDqH8ORacjaFqzM2N5qFgBskUx1wBm0FIaXlHf1RT5V'
    access_key='714494503822856193-fr3FGqtnNF0DnBHG4l6x56MRCdFmPwQ'
    access_secret='WReLl0jPAEHNCBZ3y2Ip8a1lyAWCZZuwbwjfZ70XOUo6G'

    # authorization
    auth = OAuthHandler(consumer_key,consumer_secret)
    api = tweepy.API(auth)
    auth.set_access_token(access_key,access_secret)

    # API call
    settings=api.get_settings()
    user=api.verify_credentials()
    friends=api.friends()
    tweets = api.user_timeline()
   
    # get user account details and parse it
    user_account={
       'screen_name':settings['screen_name'],
       'language':settings['language'],
       'sleep_time_enabled':settings['sleep_time']['enabled'],
       'sleep_time_end_time':settings['sleep_time']['end_time'],
       'sleep_time_start_time':settings['sleep_time']['start_time']
    }

    # get user profile details and parse it
    user_profile={
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

    # get friends details and parse it
    friends={
        'name':friends[0].name,
        'screen_name':friends[0].screen_name,
        'id':friends[0].id,
        'profile_image_url':friends[0].profile_image_url,
        'created_at':friends[0].created_at,
        'location':friends[0].location,
        'favorites_count':friends[0].favourites_count,
        'url':friends[0].url,
        'listed_count':friends[0].listed_count,
        'lang':friends[0].lang,
        'followers_count':friends[0].followers_count,
        'time_zone':friends[0].time_zone,
        'description':friends[0].description,
        'statuses_count':friends[0].statuses_count,
        'friends_count':friends[0].friends_count
    }
    
    print("\nUser Account Details:")
    print(user_account)
    print("\nUser_profile:")
    print(user_profile)

    # get tweets
    print("\nTweets:")
    print(tweets)

    return jsonify(user_account,str(user_profile),friends,str(tweets))
    
#if __name__ == '__main__':
app.run(port=5000)
#app.run(debug=True)
