import FWCore.ParameterSet.Config as cms

process = cms.Process("TagProbe")

process.load('Configuration.StandardSequences.Services_cff')
process.load('FWCore.MessageService.MessageLogger_cfi')
process.options   = cms.untracked.PSet( wantSummary = cms.untracked.bool(True) )
process.MessageLogger.cerr.FwkReport.reportEvery = 5000

process.source = cms.Source("PoolSource", 
    fileNames = cms.untracked.vstring(),
    secondaryFileNames = cms.untracked.vstring(),
)
#process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1))
#process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(10))
process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(1000))
#process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(50000))

process.load('Configuration.StandardSequences.GeometryRecoDB_cff')
process.load('Configuration.StandardSequences.MagneticField_38T_cff')
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_condDBv2_cff')
process.load("Configuration.StandardSequences.Reconstruction_cff")

import os
#if "CMSSW_10_2_" in os.environ['CMSSW_VERSION']:
#    process.GlobalTag.globaltag = cms.string('94X_mc2017_realistic_v14')
#    process.source.fileNames = [
#	     '/store/mc/RunIIFall17MiniAODv2/DYJetsToLL_M-50_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017RECOSIMstep_12Apr2018_94X_mc2017_realistic_v14_ext1-v1/70000/DA1BE8CB-5444-E811-BDBF-0025905A48FC.root'
#    ] 
#    process.source.secondaryFileNames = [
#	'/store/mc/RunIIFall17DRPremix/DYJetsToLL_M-50_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/RECOSIMstep_94X_mc2017_realistic_v10_ext1-v1/00000/00EA8F62-2EF2-E711-AAAE-02163E01A748.root',
#'/store/mc/RunIIFall17DRPremix/DYJetsToLL_M-50_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/RECOSIMstep_94X_mc2017_realistic_v10_ext1-v1/00000/04BC9724-1FF3-E711-991F-02163E019DA2.root',
#'/store/mc/RunIIFall17DRPremix/DYJetsToLL_M-50_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/RECOSIMstep_94X_mc2017_realistic_v10_ext1-v1/00000/28FE5BFB-22F3-E711-A567-02163E0145F8.root',
#'/store/mc/RunIIFall17DRPremix/DYJetsToLL_M-50_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/RECOSIMstep_94X_mc2017_realistic_v10_ext1-v1/00000/52BB448E-24F3-E711-A595-02163E011CBF.root',
#'/store/mc/RunIIFall17DRPremix/DYJetsToLL_M-50_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/RECOSIMstep_94X_mc2017_realistic_v10_ext1-v1/00000/A4E3F7AC-23F3-E711-A2E7-02163E011B34.root',
#'/store/mc/RunIIFall17DRPremix/DYJetsToLL_M-50_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/RECOSIMstep_94X_mc2017_realistic_v10_ext1-v1/00000/A654B436-1FF3-E711-9FB9-02163E014575.root',
#'/store/mc/RunIIFall17DRPremix/DYJetsToLL_M-50_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/RECOSIMstep_94X_mc2017_realistic_v10_ext1-v1/00000/ACD9EC20-90F2-E711-9DF8-02163E014256.root',
#'/store/mc/RunIIFall17DRPremix/DYJetsToLL_M-50_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/RECOSIMstep_94X_mc2017_realistic_v10_ext1-v1/00002/CC7CEC9A-9EF2-E711-A81D-02163E0146DB.root'
#   ]
    
if "CMSSW_10_2_" in os.environ['CMSSW_VERSION']:
    #process.GlobalTag.globaltag = cms.string('102X_upgrade2018_realistic_v15-v1')
#    process.GlobalTag.globaltag = cms.string('80X_mcRun2_asymptotic_2016_TrancheIV_v6')
    #process.GlobalTag.globaltag = cms.string('94X_mcRun2_asymptotic_v3')94X_mcRun2_asymptotic_v3
    process.GlobalTag.globaltag= cms.string('94X_mcRun2_asymptotic_v3')
    process.source.fileNames = [
        '/store/mc/RunIISummer16MiniAODv2/DYJetsToLL_M-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v2/120000/2EBC1B59-57C5-E611-977E-00266CFFBF38.root'
    ]
    process.source.secondaryFileNames = [
 	'/store/mc/RunIISummer16DR80Premix/DYJetsToLL_M-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/110000/20DC5A01-A9B1-E611-BF3C-002590DB05DA.root'
    ]
else: raise RuntimeError, "Unknown CMSSW version %s" % os.environ['CMSSW_VERSION']

## SELECT WHAT DATASET YOU'RE RUNNING ON
TRIGGER="SingleMu"
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

##    __  __                       
##   |  \/  |_   _  ___  _ __  ___ 
##   | |\/| | | | |/ _ \| '_ \/ __|
##   | |  | | |_| | (_) | | | \__ \
##   |_|  |_|\__,_|\___/|_| |_|___/
##                                 
## ==== Merge CaloMuons and Tracks into the collection of reco::Muons  ====

process.load("MuonAnalysis.MuonAssociators.patMuonsWithTrigger_cff")
## with some customization
process.muonMatchHLTL2.maxDeltaR = 0.3 # Zoltan tuning - it was 0.5
process.muonMatchHLTL3.maxDeltaR = 0.1
from MuonAnalysis.MuonAssociators.patMuonsWithTrigger_cff import *
#changeRecoMuonInput(process, "mergedMuons")
useExistingPATMuons(process,"slimmedMuons")
useL1Stage2Candidates(process)
appendL1MatchingAlgo(process)
#addHLTL1Passthrough(process)
changeTriggerProcessName(process, "HLT")



from MuonAnalysis.TagAndProbe.common_variables_cff import *
process.load("MuonAnalysis.TagAndProbe.common_modules_cff")

process.tagMuons = cms.EDFilter("PATMuonSelector",
    src = cms.InputTag("patMuonsWithTrigger"),
    cut = cms.string("pt > 15 && passed(8)"+
                     " && pfIsolationR04().sumChargedHadronPt/pt < 0.2"),
)
if TRIGGER != "SingleMu":
    process.tagMuons.cut = ("pt > 6 && (isGlobalMuon || isTrackerMuon) && isPFMuon "+
                            " && pfIsolationR04().sumChargedHadronPt/pt < 0.2")

process.oneTag  = cms.EDFilter("CandViewCountFilter", src = cms.InputTag("tagMuons"), minNumber = cms.uint32(1))

process.probeMuons = cms.EDFilter("PATMuonSelector",
    src = cms.InputTag("patMuonsWithTrigger"),
    cut = cms.string("track.isNonnull"),  # no real cut now
)

process.tpPairs = cms.EDProducer("CandViewShallowCloneCombiner",
    #cut = cms.string('60 < mass < 140 && abs(daughter(0).vz - daughter(1).vz) < 4'),
    cut = cms.string('60 < mass && abs(daughter(0).vz - daughter(1).vz) < 4'),
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
	#looseIsoFlag = cms.InputTag("muonMiniIsoNano","looseIsoFlag"),

    ),
    flags = cms.PSet(
       TrackQualityFlags,
       MuonIDFlags,
       HighPtTriggerFlags,
       HighPtTriggerFlagsDebug,
    ),
    tagVariables = cms.PSet(
       AllVariables,
        ExtraIsolationVariables,
        nVertices   = cms.InputTag("nverticesModule"),
       met = cms.InputTag("tagMetMt","met"),
        mt  = cms.InputTag("tagMetMt","mt"),
	miniIsoAll = cms.InputTag("muonMiniIsoNano","miniIsoAll"),
	#looseIsoFlag = cms.InputTag("muonMiniIsoNano","looseIsoFlag"),
   ),
    mcVariables = cms.PSet(),
 #       pt = cms.string('pt'),
 #       phi = cms.string('phi'),
 #       charge = cms.string('charge'),
 #       eta = cms.string('eta'),
 #       ),
    mcFlags = cms.PSet(),
#    tagFlags = cms.PSet( ),
    tagFlags = cms.PSet(
        HighPtTriggerFlags,
        HighPtTriggerFlagsDebug,
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
    pairFlags = cms.PSet(
        BestZ = cms.InputTag("bestPairByZMass"),
    ),
   
    isMC = cms.bool(False),
    addRunLumiInfo = cms.bool(True),
#    tagMatches       = cms.InputTag("tagMuonsMCMatch"),
#    probeMatches     = cms.InputTag("probeMuonsMCMatch"),
#    motherPdgId      = cms.vint32(22, 23),
#    makeMCUnbiasTree       = cms.bool(False), 
#    checkMotherInUnbiasEff = cms.bool(True),
    allProbes              = cms.InputTag("probeMuons"),
)
if TRIGGER != "SingleMu":
    for K,F in MuonIDFlags.parameters_().iteritems():
        setattr(process.tpTree.tagFlags, K, F)


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
    process.bestPairByZMass + 
    process.tpTree
)

process.tagAndProbe = cms.Path( 
    process.patMuonsWithTriggerSequence *
    process.tnpSimpleSequence
)


#process.TFileService = cms.Service("TFileService", fileName = cms.string("zmctrigtest.root"))
process.TFileService = cms.Service("TFileService", fileName = cms.string("pfisotest_2016.root"))
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
