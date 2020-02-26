import FWCore.ParameterSet.Config as cms

process = cms.Process("TagProbe")

process.load('Configuration.StandardSequences.Services_cff')
process.load('FWCore.MessageService.MessageLogger_cfi')
process.options   = cms.untracked.PSet( wantSummary = cms.untracked.bool(True) )
process.MessageLogger.cerr.FwkReport.reportEvery = 5000

process.source = cms.Source("PoolSource", 
    fileNames = cms.untracked.vstring(),
)
process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1))
#process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(10))
#process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(1000))
#process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(50000))

process.load('Configuration.StandardSequences.GeometryRecoDB_cff')
process.load('Configuration.StandardSequences.MagneticField_38T_cff')
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_condDBv2_cff')
process.load("Configuration.StandardSequences.Reconstruction_cff")

import os

if "CMSSW_10_2_" in os.environ['CMSSW_VERSION']:
    process.GlobalTag.globaltag = cms.string('94X_dataRun2_ReReco_EOY17_v2')
    process.source.fileNames = [
	'/store/data/Run2017C/SingleMuon/MINIAOD/17Nov2017-v1/70000/FE39A6C4-7FDA-E711-8C6B-02163E014496.root',
	'/store/data/Run2017C/SingleMuon/MINIAOD/17Nov2017-v1/70000/FCDAA686-73DA-E711-BBE6-02163E013747.root',
	'/store/data/Run2017C/SingleMuon/MINIAOD/17Nov2017-v1/70000/FC32D4AD-76DA-E711-A512-02163E011A81.root',
	'/store/data/Run2017C/SingleMuon/MINIAOD/17Nov2017-v1/70000/FA2EB26A-1CDC-E711-842C-7845C4FC39D1.root',
	'/store/data/Run2017C/SingleMuon/MINIAOD/17Nov2017-v1/70000/F240A0AA-1BDC-E711-98BD-02163E01A653.root',
	'/store/data/Run2017C/SingleMuon/MINIAOD/17Nov2017-v1/70000/EE313DA3-49DB-E711-A719-0025905B8610.root',
	'/store/data/Run2017C/SingleMuon/MINIAOD/17Nov2017-v1/70000/E6779F8C-7ADA-E711-B6D7-02163E019B8F.root',
	'/store/data/Run2017C/SingleMuon/MINIAOD/17Nov2017-v1/70000/E0A6D12C-3DDB-E711-A2B4-0025905C2CA4.root',
	'/store/data/Run2017C/SingleMuon/MINIAOD/17Nov2017-v1/70000/DE508AFB-9EDB-E711-997D-02163E011F60.root',
	'/store/data/Run2017C/SingleMuon/MINIAOD/17Nov2017-v1/70000/D67F76F6-82DA-E711-B497-0CC47A7C3628.root',
       #'file:/home/t3-ku/janguian/files/TnP_verificationFiles/miniAOD/F2283B5C-6044-E811-B61D-0025905B859A.root'
    ] 
    

else: raise RuntimeError, "Unknown CMSSW version %s" % os.environ['CMSSW_VERSION']

## SELECT WHAT DATASET YOU'RE RUNNING ON
TRIGGER="SingleMu"
#TRIGGER="Any"

## ==== Fast Filters ====
#process.goodVertexFilter = cms.EDFilter("VertexSelector",
#    src = cms.InputTag("offlineSlimmedPrimaryVertices"),
#    cut = cms.string("!isFake && ndof > 4 && abs(z) <= 25 && position.Rho <= 2"),
#    filter = cms.bool(True),
#)
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

from MuonAnalysis.TagAndProbe.common_variables_cff import *
process.load("MuonAnalysis.TagAndProbe.common_modules_cff")

process.tagMuons = cms.EDFilter("PATMuonSelector",
    src = cms.InputTag("slimmedMuons"),
    cut = cms.string("pt > 15 && passed(8)"+
                     " && pfIsolationR04().sumChargedHadronPt/pt < 0.2"),
)
if TRIGGER != "SingleMu":
    process.tagMuons.cut = ("pt > 6 && (isGlobalMuon || isTrackerMuon) && isPFMuon "+
                            " && pfIsolationR04().sumChargedHadronPt/pt < 0.2")

process.oneTag  = cms.EDFilter("CandViewCountFilter", src = cms.InputTag("tagMuons"), minNumber = cms.uint32(1))

process.probeMuons = cms.EDFilter("PATMuonSelector",
    src = cms.InputTag("slimmedMuons"),
    cut = cms.string("track.isNonnull"),  # no real cut now
)

process.tpPairs = cms.EDProducer("CandViewShallowCloneCombiner",
    #cut = cms.string('60 < mass < 140 && abs(daughter(0).vz - daughter(1).vz) < 4'),
    cut = cms.string('60 < mass && abs(daughter(0).vz - daughter(1).vz) < 4'),
    decay = cms.string('tagMuons@+ probeMuons@-')
)
process.onePair = cms.EDFilter("CandViewCountFilter", src = cms.InputTag("tpPairs"), minNumber = cms.uint32(1))
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

    ),
    tagVariables = cms.PSet(
       AllVariables,
        ExtraIsolationVariables,
        nVertices   = cms.InputTag("nverticesModule"),
       met = cms.InputTag("tagMetMt","met"),
        mt  = cms.InputTag("tagMetMt","mt"),
   ),
   tagFlags = cms.PSet(
            ),
    pairVariables = cms.PSet(
    
        dz      = cms.string("daughter(0).vz - daughter(1).vz"),
        pt      = cms.string("pt"), 
        rapidity = cms.string("rapidity"),
        deltaR   = cms.string("deltaR(daughter(0).eta, daughter(0).phi, daughter(1).eta, daughter(1).phi)"), 
      ),
    pairFlags = cms.PSet(
        BestZ = cms.InputTag("bestPairByZMass"),
    ),
    isMC = cms.bool(False),
    addRunLumiInfo = cms.bool(True),
    motherPdgId      = cms.vint32(22, 23),
    makeMCUnbiasTree       = cms.bool(False), 
    checkMotherInUnbiasEff = cms.bool(True),
    allProbes              = cms.InputTag("probeMuons"),
)
if TRIGGER != "SingleMu":
    for K,F in MuonIDFlags.parameters_().iteritems():
        setattr(process.tpTree.tagFlags, K, F)


process.miniIsoSeq = cms.Sequence(
	process.muonMiniIsoNano
)
process.tnpSimpleSequence = cms.Sequence(
    process.tagMuons  + 
    process.oneTag     +
    process.probeMuons +
    process.tpPairs    +
    process.onePair    +
    process.nverticesModule +
    process.miniIsoSeq +
    process.bestPairByZMass + 
    process.tpTree
)

process.tagAndProbe = cms.Path( 
    process.tnpSimpleSequence
)


process.TFileService = cms.Service("TFileService", fileName = cms.string("tnpZ_Data.root"))

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
