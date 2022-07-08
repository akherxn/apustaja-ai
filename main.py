from pepe import tweeter
from itertools import count
import tweepy
import re
import random
import time
import datetime
import os

last_seen_mention_id = 1529632475521089543


CONSUMER_KEY = os.environ["CONSUMER_KEY"]
CONSUMER_SECRET = os.environ["CONSUMER_SECRET"]
ACCESS_KEY = os.environ["ACCESS_KEY"]
ACCESS_SECRET = os.environ["ACCESS_SECRET"]
auth = tweepy.OAuth1UserHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth, wait_on_rate_limit=True)
print("authentication successful")
tweeter()



'''
p1 = multiprocessing.Process(target=tweeter)
p2 = multiprocessing.Process(target=reply)
  
# starting process 1
p1.start()
# starting process 2
p2.start()
  
# wait until process 1 is finished
p1.join()
# wait until process 2 is finished
p2.join()
  
print("both processes finished")
'''