import sys
import os
import subprocess

filename= sys.argv[1]

f = open(filename,"r")

lines = f.readlines()

files = []
for line in lines:
        line = line.rstrip()
        line = line.split()
        [ files.append(x) for x in line if ".root" in x ]


#for x in files:
#        print x

#do a query for each file
def bash( bashCommand ):
        process = subprocess.Popen(bashCommand.split(), stdout=subprocess.PIPE)
        #process = subprocess.Popen(bashCommand.split())
        output, error = process.communicate()
        return output ,error


query = ["dasgoclient -query=\"parent file=","/dummyfile/","\"\n"]

temp1 = open("temp.sh","w")
bash("chmod 777 temp.sh")

for ifile in files:
	query[1] = ifile
	cmd = ''.join(query)
	#dasclient is weird print to a file then read it
#	temp1 = open("temp.sh","w")
#	bash("chmod 777 temp.sh")
	temp1.write(cmd)
	#temp1.close()
	#out = bash("./temp.sh")
	#print out[0]
	#temp2 = open("temp.out","r")
	#line = temp2.readlines()[0]
	#temp2.close()
	#out = bash("rm temp.out")
	#cmd2 = line
	#print "cmd2", cmd2
	#parentlist = bash(cmd2)
	#print parentlist[0]
#	break;
		
temp1.close()
#parentoutput = bash("./temp.sh")
#print parentoutput[0]
