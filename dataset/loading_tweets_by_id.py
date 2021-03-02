import pandas as pd
import tweepy
import time
import sys
from tweepy import OAuthHandler
from tweepy.error import TweepError
from time import sleep
from bcolor import bcolors

ckey=""
csecret=""
atoken=""
asecret=""

auth = OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)
api = tweepy.API(auth)

P_TAG = 'POSITIVO'
N_TAG = 'NEGATIVO'

p_array = list()
n_array = list()

p_tweets = list()
n_tweets = list()
b = 0
i = 1
with open('positivos.txt', 'r') as pos_file:
    for line in pos_file:
        p_tweets.append(line)
        b += 1 
        if b >= 10000:
            break 
b = 0 
with open('negativos.txt', 'r') as neg_file:
        for line in neg_file:
            n_tweets.append(line)
            b += 1
            if b >= 10000:
                break

b = len(p_tweets)
for tweet_id in p_tweets:
    try:
        tweet_info = api.get_status(tweet_id)
        text = tweet_info.text
        sys.stdout.write(bcolors.GREEN)
        print('{} [{}] - Adding tweet {} of {} | {}%'.format(time.strftime("%H:%M:%S", time.localtime()), P_TAG, i, b, (i/b)*100))
        sys.stdout.write(bcolors.RESET)
        p_array.append((text,1))
        sleep(3)
        i += 1
        if i > b:
            break
    except TweepError:
        sys.stdout.write(bcolors.RED)
        print('{} [{}] - Failing tweet {} of {} | {}%'.format(time.strftime("%H:%M:%S", time.localtime()), P_TAG, i, b, (i/b)*100))
        sys.stdout.write(bcolors.RESET)
        i += 1
        if i > b:
            break
        continue
            
print('Finish positivos indo para o to csv')
df = pd.DataFrame(p_array, columns=['tweets', 'label'])
df.to_csv('p_out.csv', index=False)
i = 1
for tweets_id in n_tweets:
    try:
        tweet_info = api.get_status(tweets_id)
        text = tweet_info.text
        sys.stdout.write(bcolors.GREEN)
        print('{} [{}] - Adding tweet {} of {} | {}%'.format(time.strftime("%H:%M:%S", time.localtime()), N_TAG, i, b, (i/b)*100))
        sys.stdout.write(bcolors.RESET)
        n_array.append((text,0))
        sleep(3)
        i += 1
        if i > b:
            break
    except TweepError:
        sys.stdout.write(bcolors.RED)
        print('{} [{}] - Failing tweet {} of {} | {}%'.format(time.strftime("%H:%M:%S", time.localtime()), N_TAG, i, b, (i/b)*100))
        sys.stdout.write(bcolors.RESET)
        i += 1
        if i > b:
            break
        continue

print('Finish negativos indo para o to csv')
df = pd.DataFrame(n_array, columns=['tweets', 'label'])
df.to_csv('n_out.csv', index=False)
