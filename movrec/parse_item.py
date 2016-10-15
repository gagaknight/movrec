import sys

f = open('data/u.item',"r")

i = 0

print "movieId" + "," + "title"

for lines in f:
  line = lines.strip().split('|')
  i = i + 1 
  title = line[1].strip().replace(",","")
  print str(i) + "," + title
