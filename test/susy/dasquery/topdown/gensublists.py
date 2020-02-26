

import sys
import os
import subprocess

#do a query for each file
def bash( bashCommand ):
        process = subprocess.Popen(bashCommand.split(), stdout=subprocess.PIPE)
        #process = subprocess.Popen(bashCommand.split())
        output, error = process.communicate()
        return output ,error




maxfiles = int(sys.argv[1])
filesperlist = int(sys.argv[2])

outdir = str(sys.argv[3])

#rm old lists
bash("rm "+outdir+"*.list")


f = open("aodfiles.list","r")
lines = f.readlines()
f.close()

f = open(outdir+"list_1.list","w")
filecnt = 1
filesinlist = 1
listcnt = 1
for line in lines:
	
	if filecnt > maxfiles:
		f.close()
		break

	if filesinlist > filesperlist:
		f.close()
		listcnt = listcnt + 1
		f = open(outdir+"list_"+str(listcnt)+".list", "w")
		filesinlist = 1
	
	f.write(line)
	filecnt = filecnt+1
	filesinlist = filesinlist+1


if f.closed:
	listcnt=listcnt
else:
	f.close()
	
