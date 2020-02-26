


import sys

filename= sys.argv[1]

f = open(filename,"r")

lines = f.readlines()

files = []
for line in lines:
	line = line.rstrip()
	line = line.split()
	[ files.append(x) for x in line if ".root" in x ]


for x in files:
	print x
