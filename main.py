import tweepy

class BoostFollowers:
    def __init__(self,screen_name,consumer_key,consumer_secret,access_token_key,access_token_secret):
        self.consumer_key = consumer_key
        self.consumer_secret = consumer_secret
        self.access_token_key = access_token_key
        self.access_token_secret = access_token_secret
        self.screen_name = screen_name

        self.auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
        self.auth.set_access_token(access_token_key, access_token_secret)
        self.api = tweepy.API(self.auth)

    # follow followers based on a given handle
    def follow_followers(self,handle):
        try:
            followers = self.api.followers(handle)
            for follower in followers:
                if follower.screen_name != self.screen_name:
                    self.api.create_friendship(follower.screen_name)
                    print follower.screen_name
        except tweepy.TweepError as e:
            print "Could not follow followers of " + handle + " at this time. Error: "
            print e
