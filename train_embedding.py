from collections import Counter
import json

input_file_path = 'temp.txt'
output_path = 'twitter_fasttext'

with open(input_file_path,'r') as fin:
    lines = fin.readlines()

counts = Counter()

for line in lines:
    counts.update(word for word in line.split())

with open('test.json','w') as fout:
    json.dump(counts,fout,indent=4)