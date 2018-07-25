import tweepy

def configure_api():
    from config import get
    inf = get() #loads credentials from untracked file //git
    """
    Does the authetincation
    Sets access accces token

    [] Read keys from a shelve, maybe
    """
    auth = tweepy.OAuthHandler(inf['consumer_key'], inf['consumer_secret'])
    auth.set_access_token(inf['access_token'], inf['access_token_secret'])

    return tweepy.API(auth)  #for agent

#api
tweepy_agent = configure_api()

def user_details():
    """Returns a user model - to access other details"""
    global tweepy_agent
    user = tweepy_agent.get_user()
    return user

#user model
user = user_details()
def follower_info(check):
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
