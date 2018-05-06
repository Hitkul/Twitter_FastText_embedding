from collections import Counter
import json
import fasttext

input_file_path = 'temp.txt'
output_path = 'twitter_fasttext_clean_level2'
output_path_json = "tf_clean_level2.json"

print("reading file")
with open(input_file_path,'r') as fin:
    lines = fin.readlines()

counts = Counter()

print("counting terms")
for line in lines:
    counts.update(word for word in line.split())

print("writing terms to json")
with open(output_path_json,'w') as fout:
    json.dump(counts,fout,indent=4)

dimensions = [50,100,300]

for d in dimensions:
    print('print traning of dimension ',d)
    model = fasttext.cbow(input_file_path, output_path+"_"+str(d), dim=d)