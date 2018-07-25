import tweepy

def configure_api():
    """
    Does the authetincation
    Sets access accces token

    [] Read keys from a shelve, maybe
    """

    config ={"consumer_key" : input("\nconsumer_key>"),\
      "consumer_secret": input("\nconsumer_secret>"),\
        "access_token": input("\naccess_token>"),\
          "access_token_secret":input("\naccess_token_secret>")}
  auth = tweepy.OAuthHandler(config['consumer_key'], config['consumer_secret'])
  auth.set_access_token(config['access_token'], config['access_token_secret'])

  return tweepy.API(auth)  #for agent

#api
tweepy_agent = configure_api()

def user_details():
    """Returns a user model - to access other details"""
    global tweepy_agent
    user = tweepy_agent.get_user()
    return user

#user model
user = user_details(check)
def follower_info():
    global user
    print('Username: %s'%(user.screen_name))
    print('Follower count: %d'%(user.followers_count))

    #print followers
    if check:
        for tweep in user.friends(): #friends - followers
            print(tweep.screen_name)

    


#retrieve tweets home timeline

def retrieve_home_tweets():
    global tweepy_agent
    #public timeline tweets
    return tweepy_agent.home_timeline()
