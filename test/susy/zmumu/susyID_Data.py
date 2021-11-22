import FWCore.ParameterSet.Config as cms

process = cms.Process("TagProbe")

process.load('FWCore.MessageService.MessageLogger_cfi')
process.source = cms.Source("EmptySource")
process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(1) )

process.TnP_Muon_ID = cms.EDAnalyzer("TagProbeFitTreeAnalyzer",
    ## Input, output 
    InputFileNames = cms.vstring(#"root://eoscms//eos/cms/store/cmst3/user/botta/TnPtrees/tnpZ_Data.190456-193557.root",
                                 #"file:tnpZ_MC.root"
				#"/home/t3-ku/janguian/CMSSW_10_2_5/src/tnpZ_MC.root",
				#'/home/t3-ku/janguian/CMSSW_10_2_5/src/MuonAnalysis/TagAndProbe/test/susy/zmumu/tnpZ_Data.root'
				#'/home/t3-ku/janguian/jsingera/TnP/SingleMuon/TnP_SingleMuon2017C_zmumu_HADD/TnP_SingleMuon2017C_zmumu_ALL.root'
                                #'/home/t3-ku/janguian/jsingera/TnP/DYJetsToLL_M-50_TuneCP5_13TeV-madgraphMLM-pythia8/TnP_ZmumuM502017_zmumu/200311_001036/0000/zmctrigtest_93.root'
				'/home/t3-ku/janguian/HADD/tempstorage/TnP_SingleMuon2017C_zmumu_1.root'
				 ), ## can put more than one
    ## copy locally to be faster: xrdcp root://eoscms//eos/cms/store/cmst3/user/botta/TnPtrees/tnpZ_Data.190456-193557.root $PWD/tnpZ_Data.190456-193557.root
    ## and then set InputFileNames = cms.vstring("tnpZ_Data.190456-193557.root"), 
    OutputFileName = cms.string("./datafits/TnPZ_susyID_GOLDMINI_Data.root"),
    InputTreeName = cms.string("fitter_tree"), 
    InputDirectoryName = cms.string("tpTree"),  
    ## Variables for binning
    Variables = cms.PSet(
        mass   = cms.vstring("Tag-muon Mass", "76", "125", "GeV/c^{2}"),
        pt     = cms.vstring("muon p_{T}", "0", "1000", "GeV/c"),
        abseta = cms.vstring("muon |#eta|", "0", "2.5", ""),
        pair_dz = cms.vstring("#Deltaz between two muons", "-100", "100", "cm"),
	SIP = cms.vstring("3d impact sig.", "0", "500", ""),
	miniIsoAll = cms.vstring("abs miniIso EA", "0", "500", "GeV/c^{2}"),
	tag_SIP = cms.vstring("(tag) 3d impact sig. ", "0", "6", ""),
    ),
    ## Flags you want to use to define numerator and possibly denominator
    Categories = cms.PSet(
        #PF = cms.vstring("PF Muon", "dummy[pass=1,fail=0]"),
	Medium = cms.vstring("Medium Muon", "dummy[pass=1,fail=0]"),	
       tag_IsoMu24_eta2p1 = cms.vstring("isomu24eta2p1", "dummy[pass=1,fail=0]"),
    ),
    Cuts = cms.PSet(
	SIP4 = cms.vstring("SIP4", "SIP", "4"),

	Mini = cms.vstring("Mini", "miniIsoAll", "6")
    ),

    ## What to fit
    Efficiencies = cms.PSet(
        Medium_pt_eta = cms.PSet(
            UnbinnedVariables = cms.vstring("mass"),
           # EfficiencyCategoryAndState = cms.vstring("PF", "pass"), ## Numerator definition
         #   EfficiencyCategoryAndState = cms.vstring("Medium", "pass", "SIP4", "below", "Mini", "below"),
	    #EfficiencyCategoryAndState = cms.vstring("Medium", "pass"),
	    #EfficiencyCategoryAndState = cms.vstring("SIP4","below"),
	    EfficiencyCategoryAndState = cms.vstring("Mini", "below"),
	 #    EfficiencyCategoryAndState = cms.vstring("Medium", "pass", "SIP4", "below"),
	    BinnedVariables = cms.PSet(
                ## Binning in continuous variables
                pt     = cms.vdouble(2,4,6,8, 10, 20, 30, 40, 60, 100 ),
                abseta = cms.vdouble( 0.0, 1.2, 2.4),
                ## flags and conditions required at the denominator, 
               # tag_IsoMu24_eta2p1 = cms.vstring("pass"), ## i.e. use only events for which this flag is true
                pair_dz = cms.vdouble(-1.,1.),            ## and for which -1.0 < dz < 1.0
		tag_IsoMu24_eta2p1 = cms.vstring("pass"),	
		Medium = cms.vstring("pass"),
		SIP = cms.vdouble(0.,4.),
            ),
            BinToPDFmap = cms.vstring("vpvPlusExpo"), ## PDF to use, as defined below
        )
    ),
    ## PDF for signal and background (double voigtian + exponential background)
    PDFs = cms.PSet(
        vpvPlusExpo = cms.vstring(
            "Voigtian::signal1(mass, mean1[90,80,100], width[2.495], sigma1[2,1,3])",
            "Voigtian::signal2(mass, mean2[90,80,100], width,        sigma2[4,2,10])",
            "SUM::signal(vFrac[0.8,0,1]*signal1, signal2)",
            "Exponential::backgroundPass(mass, lp[-0.1,-1,0.1])",
            "Exponential::backgroundFail(mass, lf[-0.1,-1,0.1])",
            "efficiency[0.9,0,1]",
            "signalFractionInPassing[0.9]"
        ),
#        vpvPlusExpo = cms.vstring(
#            "Voigtian::signal1(mass, mean1[90,80,100], width[2.495], sigma1[2,1,3])",
#            "Voigtian::signal2(mass, mean2[90,80,100], width,        sigma2[4,2,10])",
#            "SUM::signal(vFrac[0.8,0,1]*signal1, signal2)",
#            "Exponential::backgroundPass(mass, lp[-0.1,-1,0.1])",
#            "Exponential::backgroundFail(mass, lf[-0.1,-1,0.1])",
#            "efficiency[0.9,0,1]",
#            "signalFractionInPassing[0.9]"
#        ),
    ),
    ## How to do the fit
    binnedFit = cms.bool(True),
    binsForFit = cms.uint32(40),
    saveDistributionsPlot = cms.bool(True),
    NumCPU = cms.uint32(1), ## leave to 1 for now, RooFit gives funny results otherwise
    SaveWorkspace = cms.bool(False),
)

#### Slighly different configuration for isolation, where the "passing" is defined by a cut
"""process.TnP_Muon_Iso = process.TnP_Muon_ID.clone(
    OutputFileName = cms.string("TnP_Muon_Iso_Simple.root"),
    ## More variables
    Variables = process.TnP_Muon_ID.Variables.clone(
       # combRelIsoPF04dBeta = cms.vstring("PF Combined Relative Iso", "-100", "99999", ""),
        tag_nVertices       = cms.vstring("N(vertices)", "0", "99", "")
    ),
    ## Cuts: name, variable, cut threshold
    Cuts = cms.PSet()
       # PFIsoLoose = cms.vstring("PFIsoLoose" ,"combRelIsoPF04dBeta", "0.20"),
       # PFIsoTight = cms.vstring("PFIsoTight" ,"combRelIsoPF04dBeta", "0.12"),
   # ),
    ## What to fit
    Efficiencies = cms.PSet(
        Iso_vtx_tight = cms.PSet(
            UnbinnedVariables = cms.vstring("mass"),
            EfficiencyCategoryAndState = cms.vstring("PFIsoTight", "below"), ## variable is below cut value 
            BinnedVariables = cms.PSet(
                tag_nVertices = cms.vdouble(0.5,4.5,8.5,12.5,16.5,20.5,24.5,30.5), 
                PF = cms.vstring("pass"),                 ## 
                tag_IsoMu24_eta2p1 = cms.vstring("pass"), ## tag trigger matched
                pair_dz = cms.vdouble( -1.,1. ),          ## and for which -1.0 < dz < 1.0
                pt     = cms.vdouble( 25,  100 ),
                abseta = cms.vdouble( 0.0, 2.4 ),
            ),
            BinToPDFmap = cms.vstring("vpvPlusExpo"), ## PDF to use, as defined below
        ),
        Iso_vtx_loose = cms.PSet(
            UnbinnedVariables = cms.vstring("mass"),
            EfficiencyCategoryAndState = cms.vstring("PFIsoLoose", "below"), ## variable is below cut value 
            BinnedVariables = cms.PSet(
                tag_nVertices = cms.vdouble(0.5,4.5,8.5,12.5,16.5,20.5,24.5,30.5), 
                PF = cms.vstring("pass"),                 ## 
                tag_IsoMu24_eta2p1 = cms.vstring("pass"), ## tag trigger matched
                pair_dz = cms.vdouble( -1.,1. ),          ## and for which -1.0 < dz < 1.0
                pt     = cms.vdouble( 25,  100 ),
                abseta = cms.vdouble( 0.0, 2.4 ),
            ),
            BinToPDFmap = cms.vstring("vpvPlusExpo"), ## PDF to use, as defined below
        ),
    ),
)
"""
process.p1 = cms.Path(process.TnP_Muon_ID)
#process.p2 = cms.Path(process.TnP_Muon_Iso)
