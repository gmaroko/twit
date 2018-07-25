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

#retrieve tweets home timeline

def retrieve_home_tweets():
    global tweepy_agent
    #public timeline tweets
    return tweepy_agent.home_timeline()
