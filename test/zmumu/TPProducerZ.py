import FWCore.ParameterSet.Config as cms

process = cms.Process("TagProbe")

######### EXAMPLE CFG 
###  A simple test of runnning T&P on Zmumu to determine muon isolation and identification efficiencies
###  More a showcase of the tool than an actual physics example

process.load('FWCore.MessageService.MessageLogger_cfi')
process.options   = cms.untracked.PSet( wantSummary = cms.untracked.bool(True) )
process.MessageLogger.cerr.FwkReport.reportEvery = 1000

process.source = cms.Source("PoolSource", 
    fileNames = cms.untracked.vstring(
	'file:/home/t3-ku/janguian/files/Run2018D_SingleMuon_MINIAOD/8052F052-51B3-E811-B2AE-FA163EB3873F.root'
	# 'file:/home/t3-ku/janguian/dpg/files/ZeroBias_MC_2018/1092F256-8B94-E811-8230-0025905B8594.root',
	# 'file:/home/t3-ku/janguian/dpg/files/ZeroBias_MC_2018/94A20E83-7794-E811-92D7-0CC47A4D7698.root'
   	 
   #'/store/relval/CMSSW_7_2_1/RelValZMM_13/GEN-SIM-RECO/PU50ns_PHYS14_25_V1_Phys14-v1/00000/287B9489-B85E-E411-95DF-02163E00EB3F.root'
    )
)
process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )    





## Tags. In a real analysis we should require that the tag muon fires the trigger, 
##       that's easy with PAT muons but not RECO/AOD ones, so we won't do it here
##       (the J/Psi example shows it)
process.tagMuons = cms.EDFilter("PATMuonRefSelector",
    src = cms.InputTag("slimmedMuons"),
    cut = cms.string("isGlobalMuon"),
) 
## Probes. Now we just use Tracker Muons as probes
process.probeMuons = cms.EDFilter("PATMuonRefSelector",
    src = cms.InputTag("slimmedMuons"),
    cut = cms.string("isTrackerMuon"), 
)

## Here we show how to define passing probes with a selector
## although for this case a string cut in the TagProbeFitTreeProducer would be enough
#process.probesPassingCal = cms.EDFilter("MuonRefSelector",
#    src = cms.InputTag("muons"),
#    cut = cms.string(process.probeMuons.cut.value() + " && caloCompatibility > 0.6"),
#)

## Here we show how to use a module to compute an external variable
#process.drToNearestJet = cms.EDProducer("DeltaRNearestJetComputer",
#    probes = cms.InputTag("muons"),
       # ^^--- NOTA BENE: if probes are defined by ref, as in this case, 
       #       this must be the full collection, not the subset by refs.
#    objects = cms.InputTag("ak5CaloJets"),
#    objectSelection = cms.InputTag("et > 20 && abs(eta) < 3 && n60 > 3 && (.05 < emEnergyFraction < .95)"),
#)

## Combine Tags and Probes into Z candidates, applying a mass cut
process.tagProbes = cms.EDProducer("CandViewShallowCloneCombiner",
    decay = cms.string("tagMuons@+ probeMuons@-"), # charge coniugate states are implied
    cut   = cms.string("40 < mass < 200"),
    #cut = cms.string("2.6 < mass < 3.6"),
)

## Match muons to MC
#process.muMcMatch = cms.EDProducer("MCTruthDeltaRMatcherNew",
#    pdgId = cms.vint32(13),
#    src = cms.InputTag("muons"),
#    distMin = cms.double(0.3),
#    matched = cms.InputTag("genParticles")
#)

## Make the tree
process.muonEffs = cms.EDAnalyzer("TagProbeFitTreeProducer",
    # pairs
    tagProbePairs = cms.InputTag("tagProbes"),
#    pvtx = cms.InputTag("offlinePrimaryVertices"),
    arbitration   = cms.string("OneProbe"),
    # variables to use
    variables = cms.PSet(
        ## methods of reco::Candidate
        eta = cms.string("eta"),
        pt  = cms.string("pt"),
        ## a method of the reco::Muon object (thanks to the 3.4.X StringParser)
        #nsegm = cms.string("numberOfMatches"), 
        ## this one is an external variable
        #drj = cms.InputTag("drToNearestJet"),
    ),
    # choice of what defines a 'passing' probe
    flags = cms.PSet(
        ## one defined by an external collection of passing probes
	#try tight track iso
 	#passingTest = cms.string("isMediumMuon && trackIso() < 0.05"),
	passingTest = cms.string("isMediumMuon")


	#isGolden = cms.InputTag(" ")??
    ),
    # mc-truth info
    addRunLumiInfo = cms.bool(True),
   # addEventVariablesInfo = cms.bool(True),
    isMC = cms.bool(False),
)
##    ____       _   _     
##   |  _ \ __ _| |_| |__  
##   | |_) / _` | __| '_ \ 
##   |  __/ (_| | |_| | | |
##   |_|   \__,_|\__|_| |_|
##                         
process.tagAndProbe = cms.Path( 
    (process.tagMuons + process.probeMuons) *   # 'A*B' means 'B needs output of A'; 
#    (process.probesPassingCal +                 # 'A+B' means 'if you want you can re-arrange the order'
#     process.drToNearestJet   +
      (process.tagProbes)*
#     process.muMcMatch) *
    process.muonEffs
)

process.TFileService = cms.Service("TFileService", fileName = cms.string("TPtreeZ.root"))




