import tweepy
import time
from random import randint


class BoostFollowers:
    def __init__(self,screen_name,consumer_key,consumer_secret,access_token_key,access_token_secret):
        self.consumer_key = consumer_key
        self.consumer_secret = consumer_secret
        self.access_token_key = access_token_key
        self.access_token_secret = access_token_secret

        self.auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
        self.auth.set_access_token(access_token_key, access_token_secret)
        self.api = tweepy.API(self.auth,wait_on_rate_limit=True,wait_on_rate_limit_notify=True,compression=True)

    # follow followers based on a given handle
    def follow_followers(self,handle):
        try:
            myid = self.api.me().id
            cursor = tweepy.Cursor(self.api.followers,screen_name=handle)
            for follower in cursor.items():
                wait_time = randint(1,30)
                if follower.id != myid and 1.1*follower.friends_count >= follower.followers_count:
                    self.api.create_friendship(follower.id)
                    print 'Followed ' + str(follower.screen_name)
                    print follower.followers_count
                    print follower.friends_count
                    print 'Waiting ' + str(wait_time) + ' secs'
                    time.sleep(wait_time)
                else:
                    print 'Skipped following ' + follower.screen_name
        except tweepy.TweepError as e:
            print "Could not follow followers of " + handle + " at this time. Error: "
            print e
            time.sleep(60*15)
            quit()
