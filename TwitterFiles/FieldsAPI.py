#Twitter API -Field specific

from  flask import Flask ,jsonify,Response
import tweepy
from tweepy import OAuthHandler

app=Flask(__name__)

consumer_key='zxwYSCOEug42LjRggdEsRJXo2'
consumer_secret='KBgqcB0BDqH8ORacjaFqzM2N5qFgBskUx1wBm0FIaXlHf1RT5V'
access_key='714494503822856193-fr3FGqtnNF0DnBHG4l6x56MRCdFmPwQ'
access_secret='WReLl0jPAEHNCBZ3y2Ip8a1lyAWCZZuwbwjfZ70XOUo6G'
    
auth = OAuthHandler(consumer_key,consumer_secret)
api = tweepy.API(auth)
auth.set_access_token(access_key,access_secret)

# get username ##
@app.route('/get_username')
def get_username():
    screen_name=auth.get_username()
    return (screen_name)

# get userid ##
@app.route('/get_id')
def get_id():
    user=api.get_user(screen_name=get_username())
    user_id=str(user.id)
    print(user_id)
    return (user_id)

# get description ##
@app.route('/get_description')
def get_description():
    test = api.lookup_users(user_ids=[get_id()])
    for user in test:
          desc=user.description
          print('desc:' +desc)
    return (desc)  

# get url ##
@app.route('/get_url')
def get_url():

    test = api.lookup_users(user_ids=[get_id()])
    for user in test:
          url= str(user.get_url)
          print('URL:' +url)
    return (url) 

# get location  ##
@app.route('/get_location')
def get_location():

    test = api.lookup_users(user_ids=[get_id()])
    for user in test:
          loc=user.location
          print('LOcation:' +loc)
    return (loc) 


#get statuses count ##
@app.route('/get_statuses_count')
def get_statuses_count():

    test = api.lookup_users(user_ids=[get_id()])

    for user in test:
          no_of_tweets= str(user.statuses_count)
          print('Tweets Count:' +no_of_tweets)
    return (no_of_tweets) 

#get statuses ##
@app.route('/get_statuses')
def get_statuses():

    tweets = api.user_timeline(user_ids=[get_id()])
    print(tweets)
    return str(tweets) 


#get followers count ##
@app.route('/get_followers_count')
def get_followers_count():

    test = api.lookup_users(user_ids=[get_id()])
    for user in test:
          no_of_followers= str(user.followers_count)
          print('No. of Followers:' +no_of_followers)
    return (no_of_followers) 


#get_my_followers_ids
@app.route('/get_followers_ids')
def get_followers_ids():

    followers_ids = api.followers_ids(get_id())
    print('followersid:' +str(followers_ids))
    return str(followers_ids) 

#get followers
@app.route('/get_followers')
def get_followers ():
    followers = api.followers(get_id())
    print('Followers:' +str(followers))
    return str(followers) 

#get friends count
@app.route('/get_friends_count')
def get_friends():

    test = api.lookup_users(user_ids=[get_id()])
    for user in test:
          frnd= str(user.friends_count)
          print('frnd:' +frnd)
    return (frnd) 

#get friends ids #following
@app.route('/get_friends_ids')
def get_friends_ids():

    friends_ids = api.friends_ids(get_id())
      
    print('Friends_ids:' +str(friends_ids))
    return str(friends_ids) 


app.run(port=5000)