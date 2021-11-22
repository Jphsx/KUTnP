
import sys
import os
import subprocess

#do a query for each file
def bash( bashCommand ):
        process = subprocess.Popen(bashCommand.split(), stdout=subprocess.PIPE)
        #process = subprocess.Popen(bashCommand.split())
        output, error = process.communicate()
        return output ,error

listdir = sys.argv[1]

listnames = bash("ls "+listdir)
listnames = listnames[0]
listnames = listnames.split("\n")
#make sure there is not sub lists
listnames = [ x for x in listnames if "sub" not in x ]
listnames = [ x for x in listnames if "list" in x ]
print listnames
b = bash("rm "+listdir+"sub*")
#if there are sublists remove them


#get child file queries
for ilist in listnames:
        fullname = listdir+ilist
        f2 = open(fullname,"r")

        lines = f2.readlines()
        temp1 = open("temp.sh", "w")
        bash("chmod 777 temp.sh")
	ctr = 1
        for line in lines:
                line = line.rstrip()
                query = ["dasgoclient -query=\"parent file=",line,"\" > ",listdir,"PRE",str(ctr),"sub",ilist,"\n"]
                query = ''.join(query)
                print query
                temp1.write(query)
		ctr = ctr+1

        temp1.close()
        rc = subprocess.call("./temp.sh",shell=True)
        f2.close()

	#merge the pre sub lists
	f2 = open( listdir+"sub"+ilist,"w")
	f2.close()
	for x in range(1,ctr):
		rc = subprocess.call("cat "+listdir+"PRE"+str(x)+"sub"+ilist+" >> "+listdir+"sub"+ilist, shell=True)
		rc = subprocess.call("rm "+listdir+"PRE"+str(x)+"sub"+ilist, shell=True)
	
	
	 #open the newly made sublist and remove duplicate files
        f2 = open( listdir+"sub"+ilist, "r")
        lines = f2.readlines()
        uniquefiles = []
        [uniquefiles.append(x) for x in lines if x not in uniquefiles]
        f2.close()
        f2 = open( listdir+"sub"+ilist, "w" )
        for line in uniquefiles:
                f2.write(line)

        f2.close()

