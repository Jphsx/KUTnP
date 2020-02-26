


import sys

filename= sys.argv[1]

f = open(filename,"r")

lines = f.readlines()

counts = []
for line in lines:
	line = line.rstrip()
	line = line.split()
	#[ files.append(x) for x in line if ".root" in x ]
	for i in range(len(line)):
		if line[i] == "events:":
			counts.append(line[i+1])

counts = map(int,counts)
count = sum(counts)
for x in counts:
	print x

print "total ", count
