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
dataset= sys.argv[1]
#dataset= "/JpsiToMuMu_JpsiPt8_TuneCP5_13TeV-pythia8/RunIIFall17MiniAODv2-PU2017RECOSIMstep_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"

query = ["dasgoclient -query=\"file dataset=",dataset,"\" > miniaodfiles.list\n"]

query = ''.join(query)

print query
temp1 = open("miniaodquery.sh","w")
#bash("chmod 777 miniaodquery.sh")
temp1.write(query)
temp1.close()
bash("chmod 777 miniaodquery.sh")
rc = subprocess.call("./miniaodquery.sh", shell=True)
#rc = bash("./aodquery.sh")
                                                   
