from collections import Counter
import json

input_file_path = 'temp.txt'
output_path = 'twitter_fasttext_clean_level2'
output_path_json = "tf_clean_level2.json"

with open(input_file_path,'r') as fin:
    lines = fin.readlines()

counts = Counter()

for line in lines:
    counts.update(word for word in line.split())

with open(output_path_json,'w') as fout:
    json.dump(counts,fout,indent=4)