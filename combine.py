from __future__ import print_function

filenames = ['Output_2017_08.txt','Output_2017_09.txt','Output.txt']
with open('data/raw_twitter_data.txt', 'w') as outfile:
    for fname in filenames:
        print("writing from  ",fname)
        count = 0
        with open('data/'+fname) as infile:
            for line in infile:
                print("writing line number ", count,end='\r')
                outfile.write(line)
                count+=1