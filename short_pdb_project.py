#!/usr/bin/env python3

import sys

pdbname=sys.argv[1]
f=open(pdbname, 'r')
lines=f.readlines()


lis=[]
for line in lines:
	words=line.split()
	lis.append(words)
	print(words)
f.close()

f = open("new_file.pdb", 'w')
for line in lis:

	f.write("%-6s%5d %-4s%3s %-1s%4d %8.3f%8.3f%8.3f%6.2f%6.2f %-2s \n" %(line[0],int(line[1]),line[2],line[3],line[4],int(line[5]),float(line[6]),float(line[7]),float(line[8]),float(line[9]),float(line[10]),line[11]))	

f.close()
print("A new pdb file has been generated with formatted strings. Please type more new_file.pdb to open it.")
