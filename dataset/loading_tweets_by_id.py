import pandas as pd
import tweepy
import time
import sys
from tweepy import OAuthHandler
from tweepy.error import TweepError
from time import sleep
from bcolor import bcolors

ckey="-"
csecret="-"
atoken="-"
asecret="-"

auth = OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)
api = tweepy.API(auth)

P_TAG = 'POSITIVO'
N_TAG = 'NEGATIVO'

p_array = list()
n_array = list()
b = 2250

with open('positivos.txt', 'r') as file:
    i = 1
    for line in file:
        try:
            sys.stdout.write(bcolors.GREEN)
            print('{} [{}] - Reading file {} of {} | {}%'.format(time.strftime("%H:%M:%S", time.localtime()), P_TAG, i, b, (i/b)*100))
            sys.stdout.write(bcolors.RESET)
            tweet_info = api.get_status(line)
            text = tweet_info.text
            p_array.append((text,1))
            sleep(3)
            i += 1
            if i == b:
                break
        except TweepError:
            sys.stdout.write(bcolors.RED)
            print('{} [{}] - Reading file {} of {} | {}%'.format(time.strftime("%H:%M:%S", time.localtime()), P_TAG, i, b, (i/b)*100))
            sys.stdout.write(bcolors.RESET)
            i += 1
            continue
            
print('Finish positivos indo para o to csv')
df = pd.DataFrame(p_array, columns=['tweets', 'label'])
df.to_csv('p_out.csv', index=False)

with open('negativos.txt', 'r') as file:
    i = 1
    for line in file:
        try:
            sys.stdout.write(bcolors.GREEN)
            print('{} [{}] - Reading file {} of {} | {}%'.format(time.strftime("%H:%M:%S", time.localtime()), N_TAG, i, b, (i/b)*100)) 
            sys.stdout.write(bcolors.RESET)
            tweet_info = api.get_status(line)
            text = tweet_info.text
            n_array.append((text,0))
            sleep(3)
            i += 1
            if i == b:
                break
        except TweepError:
            sys.stdout.write(bcolors.RED)
            print('{} [{}] - Reading file {} of {} | {}%'.format(time.strftime("%H:%M:%S", time.localtime()), N_TAG, i, b, (i/b)*100))
            sys.stdout.write(bcolors.RESET)
            i += 1
            continue

print('Finish negativos indo para o to csv')
df = pd.DataFrame(n_array, columns=['tweets', 'label'])
df.to_csv('n_out.csv', index=False)
