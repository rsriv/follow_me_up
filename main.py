import tweepy

class BoostFollowers:
    def __init__(self,consumer_key,consumer_secret,access_token_key,access_token_secret):
        self.consumer_key = consumer_key
        self.consumer_secret = consumer_secret
        self.access_token_key = access_token_key
        self.access_token_secret = access_token_secret

        self.auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
        self.auth.set_access_token(access_token_key, access_token_secret)
        self.api = tweepy.API(self.auth)


    # follow followers based on a given handle
    def follow_followers(self,handle):
        try:
            followers = self.api.followers(handle)
            for follower in followers:
                self.api.create_friendship(handle)
        except tweepy.TweepError as e:
            print "Could not follow followers of " + handle + " at this time. Error: "
            print e
