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

            # iterate through followers of user
            for follower in cursor.items():
                wait_time = randint(1,38)

                # follow user if following greater than or equal to num followers
                if follower.id != myid and 1.1*follower.friends_count >= follower.followers_count:
                    self.api.create_friendship(follower.id)
                    print 'Followed ' + str(follower.screen_name)
                    print 'Followers: ' + str(follower.followers_count)
                    print 'Friends: ' + str(follower.friends_count)
                    print 'Waiting ' + str(wait_time) + ' secs'
                    time.sleep(wait_time)
                else:
                    print 'Skipped following ' + follower.screen_name
        except tweepy.TweepError as e:
            print "Could not follow followers of " + handle + " at this time. Error: "
            print e
            quit()


    # unfollow all followers
    def unfollow_all(self):
        try:
            myid = self.api.me().id
            cursor = tweepy.Cursor(self.api.friends)
            periodic_delay = randint(289,580)
            max_count = randint(258,1090)
            count = 0

            # iterate through users following
            for following in cursor.items():
                wait_time = randint(1,31)

                # periodically introduce long delay to emulate human activity
                if (count >= max_count):
                    print 'Starting long delay'
                    wait_time = periodic_delay
                    periodic_delay = randint(289,580)
                    max_count = randint(258,1090)
                    count = 0

                # unfollow user following
                self.api.destroy_friendship(following.screen_name)
                print 'Unfollowed ' + str(following.screen_name)
                print 'Waiting ' + str(wait_time) + ' secs'

                time.sleep(wait_time)
                count += 1

        except tweepy.TweepError as e:
            print e
            quit()
