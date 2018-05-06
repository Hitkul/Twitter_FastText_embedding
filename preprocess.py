from __future__ import print_function
import string
import re

input_file_path = 'data/raw_twitter_data.txt'
output_file_path = 'data/clean_twitter_level2.txt'

input_file_path = "temp.txt"
output_file_path = 'out.txt'



def remove_punctuation(s):
    list_punctuation = list(string.punctuation)
    for i in list_punctuation:
        s = s.replace(i,'')
    return s


def clean(sentence,level_flag = 0):
    #level_flag = 0 : to lower, remove punctuation
    #level_flag = 1 : to lower, remove punctuation, remover twitter usernames, remove # from #tags
    #level_flag = 2 : to lower, remove punctuation, remover twitter usernames, remove # from #tags,
    #                 remove web links, remove non alphabetic
    sentence = sentence.lower()
    tokens = sentence.split()
    tokens = [remove_punctuation(w) for w in tokens]
    if level_flag == 0:
        tokens = ' '.join(tokens)
        return tokens
    
    if level_flag != 0:
        sentence = re.sub(r"\@(\w+)", "", sentence)
        sentence = sentence.replace('#','')
        if level_flag == 1:
            tokens = sentence.split()
            tokens = [remove_punctuation(w) for w in tokens]
            return ' '.join(tokens)
        sentence = re.sub(r'(?P<url>https?://[^\s]+)', r'', sentence)
        sentence = re.sub(r'([^a-zA-Z ])','',sentence )
        tokens = sentence.split()
        tokens = [remove_punctuation(w) for w in tokens]
        return ' '.join(tokens)

count = 0
def wraper_fun(s,flag,l):
    global count
    print(count,l,end='\r')
    count+=1
    return clean(s,level_flag=flag)

with open(input_file_path,'r') as fin:
    ele = fin.readlines()
    length = len(ele)
    clean_sentences = [wraper_fun(s,2,length) for s in ele]
     
print("writing to file")
with open(output_file_path,'w') as f:
    f.write('\n'.join(clean_sentences))
    