import FWCore.ParameterSet.Config as cms
import FWCore.ParameterSet.VarParsing as VarParsing


process = cms.Process("TagProbe")

options = VarParsing.VarParsing('analysis')
#options.inputFiles = 'empty1.root'
#options.secondaryInputFiles = 'empty2.root'
options.outputFile = "jpsi2018_D.root"
options.parseArguments()




process.load('Configuration.StandardSequences.Services_cff')
process.load('FWCore.MessageService.MessageLogger_cfi')
process.options   = cms.untracked.PSet( wantSummary = cms.untracked.bool(True) )
process.MessageLogger.cerr.FwkReport.reportEvery = 5000

process.source = cms.Source("PoolSource", 
    fileNames = cms.untracked.vstring(options.inputFiles),
    secondaryFileNames = cms.untracked.vstring(options.secondaryInputFiles),
)
#process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1))
#process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(10))
process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(1000))
#process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(50000))
#process.maxEvents = cms.untracked.PSet( input=cms.untracked.int32(options.maxEvents ))


process.load('Configuration.StandardSequences.GeometryRecoDB_cff')
process.load('Configuration.StandardSequences.MagneticField_38T_cff')
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_condDBv2_cff')
process.load("Configuration.StandardSequences.Reconstruction_cff")

import os
if "CMSSW_10_2_" in os.environ['CMSSW_VERSION']:
    process.GlobalTag.globaltag = cms.string('102X_dataRun2_v12')
    #process.GlobalTag.globaltag = cms.string('102X_upgrade2018_realistic_v15')
#    process.GlobalTag.globaltag = cms.string('94X_mc2017_realistic_v14')
   #  process.GlobalTag.globaltag = cms.string('94X_dataRun2_ReReco_EOY17_v6')
#	qqq= 1
    process.source.fileNames = [
	'file:mini.root'
    ]
#    process.source.secondaryFileNames = [
#	'file:aod1.root'
#    ]
   
#	'/store/mc/RunIIFall17DRPremix/JpsiToMuMu_JpsiPt8_TuneCP5_13TeV-pythia8/AODSIM/RECOSIMstep_94X_mc2017_realistic_v10-v1/820000/5E7F1DB0-FA10-E811-B3EA-F01FAFE5CEFA.root'    
  	
    
    

else: raise RuntimeError, "Unknown CMSSW version %s" % os.environ['CMSSW_VERSION']

## SELECT WHAT DATASET YOU'RE RUNNING ON
#TRIGGER="SingleMu"
#TRIGGER="Any"

## ==== Fast Filters ====
process.goodVertexFilter = cms.EDFilter("VertexSelector",
    src = cms.InputTag("offlineSlimmedPrimaryVertices"),
    cut = cms.string("!isFake && ndof > 4 && abs(z) <= 25 && position.Rho <= 2"),
    filter = cms.bool(True),
)
process.noScraping = cms.EDFilter("FilterOutScraping",
    applyfilter = cms.untracked.bool(True),
    debugOn = cms.untracked.bool(False), ## Or 'True' to get some per-event info
    numtrack = cms.untracked.uint32(10),
    thresh = cms.untracked.double(0.25)
)
#process.fastFilter = cms.Sequence(process.goodVertexFilter + process.noScraping)

#process.load("HLTrigger.HLTfilters.triggerResultsFilter_cfi")
#process.triggerResultsFilter.triggerConditions = cms.vstring( 'HLT_Mu*_L2Mu*' )
#process.triggerResultsFilter.l1tResults = ''
#process.triggerResultsFilter.throw = True
#process.triggerResultsFilter.hltResults = cms.InputTag( "TriggerResults", "", "HLT" )
#process.HLTMu   = process.triggerResultsFilter.clone(triggerConditions = [ 'HLT_Mu*_L2Mu*' ])
#process.HLTBoth = process.triggerResultsFilter.clone(triggerConditions = [ 'HLT_Mu*_L2Mu*', 'HLT_Mu*_Track*_Jpsi*' ])



##    __  __                       
##   |  \/  |_   _  ___  _ __  ___ 
##   | |\/| | | | |/ _ \| '_ \/ __|
##   | |  | | |_| | (_) | | | \__ \
##   |_|  |_|\__,_|\___/|_| |_|___/
##                                 
## ==== Merge CaloMuons and Tracks into the collection of reco::Muons  ====
## ==== Trigger matching

##process.load("MuonAnalysis.MuonAssociators.patMuonsWithTrigger_cff")
## with some customization
##from MuonAnalysis.MuonAssociators.patMuonsWithTrigger_cff import *
#changeRecoMuonInput(process, "slimmedMuons")
##useExistingPATMuons(process,"slimmedMuons")


##useL1Stage2Candidates(process)
##appendL1MatchingAlgo(process)
#addHLTL1Passthrough(process)
#changeTriggerProcessName(process, "*") # auto-guess

from MuonAnalysis.TagAndProbe.common_variables_cff import *
process.load("MuonAnalysis.TagAndProbe.common_modules_cff")

#PASS_HLT = "!triggerObjectMatchesByPath('%s').empty()" % ("HLT_Mu3",);
process.tagMuons = cms.EDFilter("PATMuonSelector",
    src = cms.InputTag("slimmedMuons"),
 #   src = cms.InputTag("patMuonsWithTrigger"),
 #   cut = cms.string("(isGlobalMuon || numberOfMatchedStations > 1) && pt>5"+" && "+PASS_HLT)
    cut = cms.string("(isGlobalMuon || numberOfMatchedStations > 1) && pt > 5"),# && !triggerObjectMatchesByCollection('hltIterL3MuonCandidates').empty()"),
)
#if TRIGGER != "SingleMu":
#    process.tagMuons.cut = ("pt > 6 && (isGlobalMuon || isTrackerMuon) && isPFMuon "+
#                            " && pfIsolationR04().sumChargedHadronPt/pt < 0.2")

process.oneTag  = cms.EDFilter("CandViewCountFilter", src = cms.InputTag("tagMuons"), minNumber = cms.uint32(1))

process.probeMuons = cms.EDFilter("PATMuonSelector",
    src = cms.InputTag("slimmedMuons"),
 #   src = cms.InputTag("patMuonsWithTrigger"),
    cut = cms.string("track.isNonnull")
 #   cut = cms.string("track.isNonnull && (!triggerObjectMatchesByCollection('hltTracksIter').empty() || !triggerObjectMatchesByCollection('hltMuTrackJpsiEffCtfTrackCands').empty() || !triggerObjectMatchesByCollection('hltMuTrackJpsiCtfTrackCands').empty() || !triggerObjectMatchesByCollection('hltL2MuonCandidates').empty())"),  # no real cut now
)

process.tpPairs = cms.EDProducer("CandViewShallowCloneCombiner",
    #cut = cms.string('60 < mass < 140 && abs(daughter(0).vz - daughter(1).vz) < 4'),
    cut = cms.string('2.8 < mass < 3.4 && abs(daughter(0).vz - daughter(1).vz) < 1'),
    decay = cms.string('tagMuons@+ probeMuons@-')
)
process.onePair = cms.EDFilter("CandViewCountFilter", src = cms.InputTag("tpPairs"), minNumber = cms.uint32(1))

process.tagMuonsMCMatch = cms.EDProducer("MCMatcher", # cut on deltaR, deltaPt/Pt; pick best by deltaR
    src     = cms.InputTag("tagMuons"), # RECO objects to match
    matched = cms.InputTag("goodGenMuons"),   # mc-truth particle collection
    mcPdgId     = cms.vint32(13),  # one or more PDG ID (13 = muon); absolute values (see below)
    checkCharge = cms.bool(False), # True = require RECO and MC objects to have the same charge
    mcStatus = cms.vint32(1),      # PYTHIA status code (1 = stable, 2 = shower, 3 = hard scattering)
    maxDeltaR = cms.double(0.3),   # Minimum deltaR for the match
    maxDPtRel = cms.double(0.5),   # Minimum deltaPt/Pt for the match
    resolveAmbiguities = cms.bool(True),    # Forbid two RECO objects to match to the same GEN object
    resolveByMatchQuality = cms.bool(True), # False = just match input in order; True = pick lowest deltaR pair first
)
process.probeMuonsMCMatch = process.tagMuonsMCMatch.clone(src = "probeMuons", maxDeltaR = 0.3, maxDPtRel = 1.0, resolveAmbiguities = False,  resolveByMatchQuality = False)

from MuonAnalysis.TagAndProbe.muon.tag_probe_muon_extraIso_cff import ExtraIsolationVariables


process.tpTree = cms.EDAnalyzer("TagProbeFitTreeProducer",
    # choice of tag and probe pairs, and arbitration
    tagProbePairs = cms.InputTag("tpPairs"),
    arbitration   = cms.string("None"),
    # probe variables: all useful ones
    variables = cms.PSet(
        AllVariables,
	miniIsoAll = cms.InputTag("muonMiniIsoNano","miniIsoAll"),


    ),
    flags = cms.PSet(
       TrackQualityFlags,
       MuonIDFlags,
#	HighPtTriggerFlags,
#	jpsitestTrigFlag,
#        LowPtTriggerFlagsEfficiencies,
#	LowPtTriggerFlagsEfficienciesTag,
#	LowPtTriggerFlagsPhysics,
#	LowPtTrig,
#	LowPtTestProbe,
#	LowPtTriggerFlagsEfficienciesProbe,
	jpsi18,
    ),
    tagVariables = cms.PSet(
        AllVariables,
        ExtraIsolationVariables,
        nVertices   = cms.InputTag("nverticesModule"),
        met = cms.InputTag("tagMetMt","met"),
        mt  = cms.InputTag("tagMetMt","mt"),
	miniIsoAll = cms.InputTag("muonMiniIsoNano","miniIsoAll"),

   ),
    mcVariables = cms.PSet(),
 #       pt = cms.string('pt'),
 #       phi = cms.string('phi'),
 #       charge = cms.string('charge'),
 #       eta = cms.string('eta'),
 #       ),
    mcFlags = cms.PSet(),
    tagFlags = cms.PSet(#HighPtTriggerFlags,
#			jpsitestTrigFlag,
#			LowPtTriggerFlagsEfficienciesTag,
 #       			LowPtTriggerFlagsPhysics 
#			LowPtTrig,
			jpsi18,
    ),   
    pairVariables = cms.PSet(
    
        dz      = cms.string("daughter(0).vz - daughter(1).vz"),
        pt      = cms.string("pt"), 
        rapidity = cms.string("rapidity"),
        deltaR   = cms.string("deltaR(daughter(0).eta, daughter(0).phi, daughter(1).eta, daughter(1).phi)"), 
      ## Gen related variables
        genWeight    = cms.InputTag("genAdditionalInfo", "genWeight"),
        truePileUp   = cms.InputTag("genAdditionalInfo", "truePileUp"),
        actualPileUp = cms.InputTag("genAdditionalInfo", "actualPileUp"),
       ),
    pairFlags = cms.PSet( ),
     #   BestZ = cms.InputTag("bestPairByZMass"),
   # ),
   
    isMC = cms.bool(False),
    addRunLumiInfo = cms.bool(True),
#    tagMatches       = cms.InputTag("tagMuonsMCMatch"),
#    probeMatches     = cms.InputTag("probeMuonsMCMatch"),
#    motherPdgId      = cms.vint32(22, 23),
#    makeMCUnbiasTree       = cms.bool(False), 
#    checkMotherInUnbiasEff = cms.bool(True),
    allProbes              = cms.InputTag("probeMuons"),
)
#if TRIGGER != "SingleMu":
#    for K,F in MuonIDFlags.parameters_().iteritems():
#        setattr(process.tpTree.tagFlags, K, F)


process.miniIsoSeq = cms.Sequence(
	process.muonMiniIsoNano
)
process.tnpSimpleSequence = cms.Sequence(
    process.tagMuons + #  * process.tagMuonsMCMatch   +
    process.oneTag     +
    process.probeMuons + #* process.probeMuonsMCMatch +
    process.tpPairs    +
    process.onePair    +
    process.nverticesModule +
    process.miniIsoSeq +
#    process.bestPairByZMass + 
    process.tpTree
)

process.tagAndProbe = cms.Path(
    #process.HLTBoth * 
 #   process.patMuonsWithTriggerSequence *
    process.tnpSimpleSequence
)


#process.TFileService = cms.Service("TFileService", fileName = cms.string("tnpJ_MC.root"))
#process.TFileService = cms.Service("TFileService", fileName = cms.string("triggerMatchTest_MC.root"))
#process.TFileService = cms.Service("TFileService", fileName = options.outputFile )
process.TFileService = cms.Service("TFileService", fileName = cms.string(options.outputFile) )

"""
if True: # enable and do cmsRun tp_from_aod_MC.py /eos/path/to/run/on [ extra_postfix ] to run on all files in that eos path 
    import sys
    args = sys.argv[1:]
    if (sys.argv[0] == "cmsRun"): args = sys.argv[2:]
    scenario = args[0] if len(args) > 0 else ""
    if scenario:
        if scenario.startswith("/"):
            import subprocess
            files = subprocess.check_output([ "/afs/cern.ch/project/eos/installation/0.3.15/bin/eos.select", "ls", scenario ])
            process.source.fileNames = [ scenario+"/"+f for f in files.split() ]
            import os.path
            process.TFileService.fileName = "tnpZ_MC_%s.root" % os.path.basename(scenario)
        else:
            process.TFileService.fileName = "tnpZ_MC_%s.root" % scenario
    if len(args) > 1:
        process.TFileService.fileName = process.TFileService.fileName.value().replace(".root", ".%s.root" % args[1])
"""
