__author__ = 'wenwen'

import argparse

parser=argparse.ArgumentParser()
parser.add_argument("p",help="input your path of file")

filepath=parser.parse_args().p

counts=[]
i=0

def count_word(mystr):
    words=mystr.split()
    #print mystr[-1]
    # return len(words)
    if mystr[-1].isspace():
        return len(words)
    else:
#	print words[-1]
	backbit=len(words[-1])
	f.seek(-backbit,1)
#	print backbit
        return len(words)-1

def summation(x,y):
    count=x+y
    return count

f = open(filepath,'r')
while True:
    f1 = f.read(1024)
    if f1 == "":
        break
    i+=1
    newf1=f1.replace(',',' ').replace('?',' ')\
        .replace('.',' ').replace('"',' ')\
        .replace("_"," ").replace("!"," ").replace(";"," ").replace("|"," ")
    count=count_word(newf1)
    counts.append(count)
total_count=reduce(summation,counts)
print total_count
f.close()



