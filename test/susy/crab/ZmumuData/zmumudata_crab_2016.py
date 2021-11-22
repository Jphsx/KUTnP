from CRABClient.UserUtilities import config #, getUsernameFromSiteDB
config = config()

config.General.requestName = 'TnP_SingleMuon2016C_zmumu'
config.General.workArea = '../crab_projects'
config.General.transferOutputs = True
config.General.transferLogs = True
config.JobType.allowUndistributedCMSSW = True


config.JobType.pluginName = 'Analysis'
config.JobType.psetName = '/home/t3-ku/janguian/CMSSW_10_2_5/src/MuonAnalysis/TagAndProbe/test/susy/zmumu/KUTnP_Data_2016.py'

config.Data.inputDataset = '/SingleMuon/Run2016C-17Jul2018-v1/MINIAOD'
config.Data.useParent = True
config.Data.inputDBS = 'global'
#config.Data.lumiMask = 'https://cms-service-dqm.web.cern.ch/cms-service-dqm/CAF/certification/Collisions16/13TeV/PromptReco/Cert_271036-284044_13TeV_23Sep2016ReReco_Collisions16_JSON.txt'
config.Data.lumiMask = 'https://cms-service-dqm.web.cern.ch/cms-service-dqm/CAF/certification/Collisions16/13TeV/ReReco/Final/Cert_271036-284044_13TeV_23Sep2016ReReco_Collisions16_JSON.txt'
# Cert_271036-284044_13TeV_23Sep2016ReReco_Colli
config.Data.splitting = 'EventAwareLumiBased'
config.Data.unitsPerJob = 50000
config.Data.outLFNDirBase = '/store/user/jsingera/TnP'
config.Data.publication = True
config.Data.outputDatasetTag = 'TnP_SingleMuon2016C_zmumu'

config.Site.storageSite = 'T2_US_Nebraska'
