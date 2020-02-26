


#run jpsimc
python querydatasetforAODfile.py "/JpsiToMuMu_JpsiPt8_TuneCP5_13TeV-pythia8/RunIIFall17DRPremix-RECOSIMstep_94X_mc2017_realistic_v10-v1/AODSIM"
python gensublists.py 5 2 "./jpsiMC/"
python genchildsublist.py "./jpsiMC/"
python modifyspecialcases.py
