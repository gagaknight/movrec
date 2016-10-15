import sys

f1 = open("item.txt","r")
f2 = open("ratings.txt","r")

for lines in f1:
    line2 = f2.readline()
    line = line2.strip().split(" ")
    print lines.strip() + "," + line[0] + "," + line[1]
