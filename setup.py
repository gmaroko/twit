import tweepy

config ={"consumer_key" : input("\nconsumer_key>"),\
  "consumer_secret": input("\nconsumer_secret>"),\
    "access_token": input("\naccess_token>"),\
      "access_token_secret":input("\naccess_token_secret>")}


def setup(setup_info):
  auth = tweepy.OAuthHandler(config['consumer_key'], config['consumer_secret'])
  auth.set_access_token(config['access_token'], config['access_token_secret'])

  return tweepy.API(auth)  #for agent


def main():
    with open("config.cfg") as info:
        tweet_agent = setup(info)
        text = input("\nTweet>")
        tweet_agent.update_status(text)

if __name__ == "__main__":
main()
