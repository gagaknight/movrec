import sys

f = open('data/u.data','r')

movie_n = 1683

print "userid" + "," + "movieid" + "," + "rating"
for lines in f:
    line = lines.strip().split('\t')
    print line[0] + "," + line[1] + "," + line[2]
