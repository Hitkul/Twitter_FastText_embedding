from __future__ import print_function
import tarfile
import os
import bz2
import json
from pprint import pprint






def extract_files(list_of_files):
    for f in list_of_files:
        print("extracting_file == "+f)
        try:
            tar = tarfile.open(f)
            tar.extractall(path="extracted_files/")
            tar.close()
        except:
            pass
        
        os.remove(f)


def get_tweets_from_compressed_file(f):
    try:
        with bz2.open(f, 'rt') as f:
            text = f.read()
        return text.split('\n')
    except:
        return None

    

def convert_string_to_dict(str_tweet):
    # json_acceptable_string = str_tweet.replace("'", "\"")
    return json.loads(str_tweet)


list_of_files = [f for f in os.listdir() if f.endswith('.tar')]

extract_files(list_of_files)


json_files = []
for path, subdirs, files in os.walk("extracted_files/"):
    for name in files:
        json_files.append(os.path.join(path, name))

count = 0
total_f = len(json_files)
tweet_file = open("twitter_data/Output.txt", "a")
for f in json_files: # Loop over all files in the TAR archive
    print(count,json_files)
    tweets_in_file = get_tweets_from_compressed_file(f)
    if tweets_in_file != None:
        for tweet in tweets_in_file[:-1]:
            tweet_json = convert_string_to_dict(tweet)
            # try:
            if 'delete' not in tweet_json.keys():
                if tweet_json['lang'] == 'en':
                    if 'retweeted_status' in tweet_json.keys():
                        t = tweet_json['retweeted_status']['text']
                    else:
                        t = tweet_json['text']
                    tweet_file.write(t)
    else:
        continue
    count+=1

tweet_file.close()
print('done')
