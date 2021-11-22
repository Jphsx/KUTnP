#gensublists Maxfiles FilesPerList Outputdir

#python querydatasetforMiniAODfile.py "/JpsiToMuMu_JpsiPt8_TuneCP5_13TeV-pythia8/RunIIFall17MiniAODv2-PU2017RECOSIMstep_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"
#python gensublists.py 10 1 "./JpsiMC/"
#python genparentsublists.py "./JpsiMC/"

 #### this dataset parent is RAW python querydatasetforMiniAODfile.py "/SingleMuon/Run2017C-17Nov2017-v1/MINIAOD"
#python querydatasetforMiniAODfile.py "/SingleMuon/Run2017C-31Mar2018-v1/MINIAOD"
#python gensublists.py 30 1 "./JpsiData/"
#python genparentsublists.py "./JpsiData/"


#python querydatasetforMiniAODfile.py "/DYJetsToLL_M-50_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIFall17MiniAODv2-PU2017RECOSIMstep_12Apr2018_94X_mc2017_realistic_v14_ext1-v1/MINIAODSIM"
#python gensublists.py 1 1 "./ZmumuMC/"
#python genparentsublists.py "./ZmumuMC/"


#python querydatasetforMiniAODfile.py "/SingleMuon/Run2017C-31Mar2018-v1/MINIAOD"
#python gensublists.py 1 1 "./ZmumuData/"
#python genparentsublists.py "./ZmumuData/"



#python querydatasetforMiniAODfile.py "/DYJetsToLL_M-50_TuneCP2_13TeV-madgraphMLM-pythia8/RunIIFall17MiniAODv2-PUFall17Fast_pilot_94X_mc2017_realistic_v15_ext1-v1/MINIAODSIM"
#python gensublists.py 20 20 "./ZmumuFastsim/" 


python querydatasetforMiniAODfile.py ""
python gensublists.py 1 1 "./ZmumuMC/"
