from CRABClient.UserUtilities import config #, getUsernameFromSiteDB
config = config()

config.General.requestName = 'TnP_SingleMuon2018A_zmumu'
config.General.workArea = '../crab_projects'
config.General.transferOutputs = True
config.General.transferLogs = True
config.JobType.allowUndistributedCMSSW = True


config.JobType.pluginName = 'Analysis'
config.JobType.psetName = '/home/t3-ku/janguian/CMSSW_10_2_5/src/MuonAnalysis/TagAndProbe/test/susy/zmumu/KUTnP_Data_2018.py'

#config.Data.inputDataset = '/SingleMuon/Run2018C-UL2018_MiniAODv2-v1/MINIAOD'
config.Data.inputDataset = '/SingleMuon/Run2018A-17Sep2018-v2/MINIAOD'
#config.Data.useParent = True
config.Data.inputDBS = 'global'
config.Data.lumiMask = 'https://cms-service-dqm.web.cern.ch/cms-service-dqm/CAF/certification/Collisions18/13TeV/PromptReco/Cert_314472-325175_13TeV_PromptReco_Collisions18_JSON.txt'

config.Data.splitting = 'EventAwareLumiBased'
config.Data.unitsPerJob = 50000
config.Data.outLFNDirBase = '/store/user/jsingera/TnP'
config.Data.publication = True
config.Data.outputDatasetTag = 'TnP_SingleMuon2018A_zmumu'

config.Site.storageSite = 'T2_US_Nebraska'
