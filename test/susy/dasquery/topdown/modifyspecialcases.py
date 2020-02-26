
import sys
import os
import subprocess

#do a query for each file
def bash( bashCommand ):
        process = subprocess.Popen(bashCommand.split(), stdout=subprocess.PIPE)
        #process = subprocess.Popen(bashCommand.split())
        output, error = process.communicate()
        return output ,error


#for jpsi mc there are two possible sets of children files, select miniaodv2 not v1
#rewrite these sublists
listdir = "./jpsiMC/"
listnames = bash("ls "+listdir)
listnames = listnames[0]
listnames = listnames.split("\n")
listnames = [x for x in listnames if "sub" in x ]

print listnames

for ilist in listnames:
        fullname = listdir+ilist
        f2 = open(fullname,"r")
	lines = f2.readlines()
	lines = [x for x in lines if "RunIIFall17MiniAODv2" in x]	
	f2.close()
	f2 = open(fullname,"w")
	for line in lines:
		f2.write(line)	
	f2.close()	











#### end j/psi modifications
