from CRABClient.UserUtilities import config#, getUsernameFromSiteDB
config = config()

config.General.requestName = 'TnP_ZmumuM502018_zmumu'
config.General.workArea = '../crab_projects'
config.General.transferOutputs = True
config.General.transferLogs = True
config.JobType.allowUndistributedCMSSW = True


config.JobType.pluginName = 'Analysis'
config.JobType.psetName = '/home/t3-ku/janguian/CMSSW_10_2_5/src/MuonAnalysis/TagAndProbe/test/susy/zmumu/KUTnP_MC_2018testing.py'

config.Data.inputDataset = '/DYJetsToLL_M-50_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM'
#/JpsiToMuMu_JpsiPt8_TuneCP5_13TeV-pythia8/RunIIFall17MiniAODv2-PU2017RECOSIMstep_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM
config.Data.useParent = True
config.Data.inputDBS = 'global'
config.Data.splitting = 'FileBased'
#config.Data.splitting = 'Automatic'
config.Data.unitsPerJob = 1
config.Data.outLFNDirBase = '/store/user/jsingera/TnP/'
config.Data.publication = True
config.Data.outputDatasetTag = 'TnP_ZmumuM502018_zmumu'

config.Site.storageSite = 'T2_US_Nebraska'
