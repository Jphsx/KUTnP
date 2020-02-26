

f = open("tempaod.list", "r")
lines = f.readlines();
#print lines
uniquelist=[]
[uniquelist.append(x) for x in lines if x not in uniquelist ]


f2 = open("uniqueaod.list", "w")

#for i in range(len(lines)):
for i in range(len(uniquelist)):
	
	#for j in range(len(lines)):
	for j in range(len(uniquelist)):
		if( i==j ):
			continue
		if(uniquelist[i] == uniquelist[j]):
			print "match found!!!!"	
			print i,j,lines[i]
		
			

for x in uniquelist:
	x=x.rstrip()
	f2.write("'"+x+"',\n")

f2.close()
f.close()
