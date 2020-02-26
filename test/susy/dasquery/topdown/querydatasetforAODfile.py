import sys
import subprocess
import os

def bash( bashCommand ):
        process = subprocess.Popen(bashCommand.split(), stdout=subprocess.PIPE)
        #process = subprocess.Popen(bashCommand.split())
        output, error = process.communicate()
        return output ,error

#example dataset
# /JpsiToMuMu_JpsiPt8_TuneCP5_13TeV-pythia8/RunIIFall17DRPremix-RECOSIMstep_94X_mc2017_realistic_v10-v1/AODSIM
#dataset= sys.argv[1]
dataset= "/JpsiToMuMu_JpsiPt8_TuneCP5_13TeV-pythia8/RunIIFall17DRPremix-RECOSIMstep_94X_mc2017_realistic_v10-v1/AODSIM"

query = ["dasgoclient -query=\"file dataset=",dataset,"\" > aodfiles.list\n"]

query = ''.join(query)

print query
temp1 = open("aodquery.sh","w")
bash("chmod 777 aodquery.sh")
temp1.write(query)
temp1.close()
rc = subprocess.call("./aodquery.sh", shell=True)
#rc = bash("./aodquery.sh")
