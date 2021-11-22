import FWCore.ParameterSet.Config as cms


### USAGE:
###    cmsRun fitMuonID.py <scenario> [ <id> [ <binning1> ... <binningN> ] ]
###
### scenarios:
###   - data_all (default)  
###   - signal_mc

## my modification usage:::
###    cmsRUn fitMuonID.py <scenario> <ID> <fitmodel>

import sys
args = sys.argv[1:]
if (sys.argv[0] == "cmsRun"): args =sys.argv[2:]
scenario = "data_all"
ID = "medsip"
fitmodel = "A"

print("Run params ", args)
if len(args) > 0: scenario = args[0]
print "Will run scenario ", scenario
if len(args) > 1: ID = args[1]
print "Will use id ", ID
if len(args) > 2: fitmodel = args[2]
print "Will use fit model ", fitmodel

process = cms.Process("TagProbe")

process.load('FWCore.MessageService.MessageLogger_cfi')
process.source = cms.Source("EmptySource")
process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(1) )

Template = cms.EDAnalyzer("TagProbeFitTreeAnalyzer",
    ## Input, output 
    InputFileNames = cms.vstring('/home/t3-ku/janguian/HADD/tempstorage/TnP_SingleMuon2017C_zmumu_1.root'), ## can put more than one
    ## copy locally to be faster: xrdcp root://eoscms//eos/cms/store/cmst3/user/botta/TnPtrees/tnpZ_Data.190456-193557.root $PWD/tnpZ_Data.190456-193557.root
    ## and then set InputFileNames = cms.vstring("tnpZ_Data.190456-193557.root"), 
    OutputFileName = cms.string("./datafits/TnPZ_susyID_GOLDMINI_Data.root"),
    InputTreeName = cms.string("fitter_tree"), 
    InputDirectoryName = cms.string("tpTree"),  
    ## Variables for binning
    Variables = cms.PSet(
	tag_dxy = cms.vstring("Tag dxy","0","0.07","cm"),
        dxy = cms.vstring("Probe dxy","0","0.07","cm"),
        mass   = cms.vstring("Tag-Probe Mass", "2.8", "3.4", "GeV/c^{2}"),
        pt     = cms.vstring("Probe p_{T}", "0", "50", "GeV/c"),
        tag_pt = cms.vstring("Tag p_{T}","0","59","GeV/c"),
        abseta = cms.vstring("Probe |#eta|", "0", "2.5", ""),
        tag_abseta = cms.vstring("Tag |#eta|","0","2.5",""),
#       tag_dxy = cms.vstring("Tag dxy","0","0.07","cm"),
        tag_dz = cms.vstring("Tag dz","0","0.15","cm"),
#       dxy = cms.vstring("Probe dxy","0","0.07","cm"),
        dz = cms.vstring("Probe dz","0","0.15","cm"),
        tag_LoosePFIso = cms.vstring("Tag passes(1) Loose PFIso","0","1.5",""),
        LoosePFIso = cms.vstring("Probe passes(1) Loose PFIso","0","1.5",""),
#        pair_dz = cms.vstring("#Deltaz between two muons", "-20", "20", "cm"),
        SIP = cms.vstring("Probe 3d impact sig.", "0", "20", ""),
        miniIsoAll = cms.vstring("Probe abs. miniIso EA", "0", "30", "GeV/c"),
        tag_SIP = cms.vstring("Tag 3d impact sig. ", "0", "6", ""),
        AbsPFIso_All = cms.vstring("Probe abs. PFIso ", "0", "30", "GeV/c"),
       # weight = cms.vstring("weight","0","10",""),
	#tag_IsoMu24_eta2p1 = cms.vstring("tag IsoMu24eta2p1","0","1.5","")
    ),
    ## Flags you want to use to define numerator and possibly denominator
    Categories = cms.PSet(
        #PF = cms.vstring("PF Muon", "dummy[pass=1,fail=0]"),
	#Medium = cms.vstring("Medium Muon", "dummy[pass=1,fail=0]"),	
        #tag_IsoMu24_eta2p1 = cms.vstring("isomu24eta2p1", "dummy[pass=1,fail=0]"),
    ),
    Cuts = cms.PSet(
#	SIP4 = cms.vstring("SIP4", "SIP", "4"),

#	Mini = cms.vstring("Mini", "miniIsoAll", "6")
    ),

    ## What to fit
    Efficiencies = cms.PSet(
        Medium_pt_eta = cms.PSet(
            UnbinnedVariables = cms.vstring("mass"),
           # EfficiencyCategoryAndState = cms.vstring("PF", "pass"), ## Numerator definition
         #   EfficiencyCategoryAndState = cms.vstring("Medium", "pass", "SIP4", "below", "Mini", "below"),
	    #EfficiencyCategoryAndState = cms.vstring("Medium", "pass"),
	    #EfficiencyCategoryAndState = cms.vstring("SIP4","below"),
#	    EfficiencyCategoryAndState = cms.vstring("Mini", "below"),
	 #    EfficiencyCategoryAndState = cms.vstring("Medium", "pass", "SIP4", "below"),
	    BinnedVariables = cms.PSet(
                ## Binning in continuous variables
                pt     = cms.vdouble(2,4,6,8, 10, 20, 30, 40, 60, 100 ),
               # abseta = cms.vdouble( 0.0, 1.2, 2.4),
                ## flags and conditions required at the denominator, 
               # tag_IsoMu24_eta2p1 = cms.vstring("pass"), ## i.e. use only events for which this flag is true
            ##    pair_dz = cms.vdouble(-1.,1.),            ## and for which -1.0 < dz < 1.0
#		tag_IsoMu24_eta2p1 = cms.vstring("pass"),	
#		Medium = cms.vstring("pass"),
#		SIP = cms.vdouble(0.,4.),
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
	voigtPlusExpo = cms.vstring(
            "Voigtian::signal(mass, mean[90,80,100], width[2.495], sigma[3,1,20])",
            "Exponential::backgroundPass(mass, lp[0,-5,5])",
            "Exponential::backgroundFail(mass, lf[0,-5,5])",
            "efficiency[0.9,0,1]",
            "signalFractionInPassing[0.9]"
        ),
	voigtGaussExpo = cms.vstring(
		"Voigtian::signal1(mass, mean[90,80,100], width[2.495], sigma[3,1,20])"
		"Gaussian::signal2(mass, mean[90,80,100], sigma[3,1,20])"
		"SUM::signal(vFrac[0.8,0,1]*signal1, signal2)",
		"Exponential::backgroundPass(mass, lp[-0.1,-1,0.1])",
	        "Exponential::backgroundFail(mass, lf[-0.1,-1,0.1])",
            	"efficiency[0.9,0,1]",
            	"signalFractionInPassing[0.9]"
	),
	 gaussPlusExpo = cms.vstring(
            #"CBShape::signal(mass, mean[3.1,3.0,3.2], sigma[0.05,0.02,0.06], alpha[3., 0.5, 5.], n[1, 0.1, 100.])",
            #"Chebychev::backgroundPass(mass, {cPass[0,-0.5,0.5], cPass2[0,-0.5,0.5]})",
            #"Chebychev::backgroundFail(mass, {cFail[0,-0.5,0.5], cFail2[0,-0.5,0.5]})",
            "Gaussian::signal(mass, mean[3.1,3.0,3.2], sigma[0.05,0.02,0.1])",
            "Exponential::backgroundPass(mass, lp[0,-5,5])",
            "Exponential::backgroundFail(mass, lf[0,-5,5])",
            "efficiency[0.9,0,1]",
            "signalFractionInPassing[0.9]"
        ),
	vpvPlusExpoJ = cms.vstring(
	    "Voigtian::signal1(mass, mean1[3.1,3.0,3.2], width[0.00001], sigma1[0.1,0.025,0.3])",
            "Voigtian::signal2(mass, mean2[3.1,3.0,3.2], width,        sigma2[0.1,0.025,0.3])",
            "SUM::signal(vFrac[0.8,0,1]*signal1, signal2)",
            "Exponential::backgroundPass(mass, lp[-0.1,-1,0.1])",
            "Exponential::backgroundFail(mass, lf[-0.1,-1,0.1])",
            "efficiency[0.9,0,1]",
            "signalFractionInPassing[0.9]"
	)

    ),
    ## How to do the fit
    binnedFit = cms.bool(True),
    binsForFit = cms.uint32(40),
    saveDistributionsPlot = cms.bool(True),
    NumCPU = cms.uint32(1), ## leave to 1 for now, RooFit gives funny results otherwise
    SaveWorkspace = cms.bool(False),
)

#PREFIX="/home/t3-ku/janguian/HADD/tempstorage/"
PREFIX="./"
process.TnP_MuonID = Template.clone(
    InputFileNames = cms.vstring(),
    InputTreeName = cms.string("fitter_tree"),
    InputDirectoryName = cms.string("tpTree"),
    OutputFileName = cms.string("./fit_output/TnPJ_MuonID_%s_%s.root" % (scenario,ID)),
    Efficiencies = cms.PSet(),
)
if "_weight" in scenario:
    process.TnP_MuonID.WeightVariable = cms.string("weight")
    process.TnP_MuonID.Variables.weight = cms.vstring("weight","0","10","")


if "data2018" in scenario:
    #process.TnP_MuonID.InputFileNames = [ "/home/t3-ku/janguian/HADD/tempstorage/TnP_SingleMuon2017C_zmumu_1.root", "/home/t3-ku/janguian/HADD/tempstorage/TnP_SingleMuon2017C_zmumu_2.root" ]
    process.TnP_MuonID.InputFileNames = [ "/home/t3-ku/janguian/jsingera/TnP/SingleMuon/TnP_SingleMuon2018A_jpsi_HADD/TnPSingleMuon2018A_jpsi_1.root" ]
    #process.TnP_MuonID.InputFileNames = [ "/home/t3-ku/janguian/jsingera/TnP/SingleMuon/TnP_SingleMuon2017C_jpsi_HADD/TnP_SingleMuon2017C_jpsi_2.root" ]
if "mc2018" in scenario:
    process.TnP_MuonID.InputFileNames = [ "./tnpJ_withNVtxWeights.root" ]


#current id modes "
#if ID
module = process.TnP_MuonID.clone(OutputFileName = cms.string("./fit_output/TnPJ_MuonID_%s_%s_%s.root" % (scenario, ID, fitmodel)))

#if "isoMu24eta2p1" in scenario:
	#setattr(module.BinnedVariables, 
	#module.Efficiencies.Medium_pt_eta.BinnedVariables.tag_IsoMu24_eta2p1 = cms.vstring("pass")
	#setattr(module.Efficiences, "Medium_pt_eta", cms.PSet( 
shape = "vpvPlusExpo"
if "A" in fitmodel:
	shape = "vpvPlusExpo"
if "B" in fitmodel:
	shape = "voigtPlusExpo"
if "C" in fitmodel:
	shape = "voigtGaussExpo"
if "D" in fitmodel:
	shape = "gaussPlusExpo"
if "E" in fitmodel:
	shape = "vpvPlusExpoJ"

#base veryloose
if "VeryLoose" in ID:
        print("very Loose")
         #pt>3  |eta| < 2.4  dxy<= 0.05 dz <= 0.1 sip3d<=8  looseisoflag==pass
        module.Cuts.DXYp = cms.vstring("DXYp","dxy","0.05")
        module.Cuts.DXYm = cms.vstring("DXYm","dxy","-0.05")
        module.Cuts.DZp = cms.vstring("DZp","dz","0.1")
        module.Cuts.DZm = cms.vstring("DZm","dz","-0.1")
        module.Cuts.SIP8 = cms.vstring("SIP8","SIP","8")
        module.Cuts.LIF = cms.vstring("LIF","LoosePFIso","0")
        #module.Categories.LoosePFIso = cms.vstring("Loose PF Iso","dummy[pass=1,fail=0]")
        setattr(module.Efficiencies, "Medium_pt_eta", cms.PSet(
            EfficiencyCategoryAndState  = cms.vstring("DXYp","below","DXYm","above","DZp","below","DZm","above","SIP8","below","LIF","above"),
            UnbinnedVariables = cms.vstring("mass"),
            BinnedVariables = cms.PSet(),
            BinToPDFmap = cms.vstring(shape)

        ))

if "_Medium" in ID:
        print("Medium")
        module.Categories.Medium = cms.vstring("Medium Muon", "dummy[pass=1,fail=0]")
        setattr(module.Efficiencies, "Medium_pt_eta", cms.PSet(
            EfficiencyCategoryAndState  = cms.vstring("Medium", "pass"),
            UnbinnedVariables = cms.vstring("mass"),
            BinnedVariables = cms.PSet(),
            BinToPDFmap = cms.vstring(shape)

        ))

#set binning
pt = cms.vdouble(3.0, 4.0,  5.0, 6.0, 7.0, 9.0, 11.0, 14.0, 17.0, 20.0)
abseta = cms.vdouble( 0.0, 1.2, 2.4)
getattr(module.Efficiencies, "Medium_pt_eta").BinnedVariables.pt = pt
getattr(module.Efficiencies, "Medium_pt_eta").BinnedVariables.abseta = abseta
if "veryLoose" in scenario:
        #to pass we need to fufill these conditions, apply very loose to both tag and probe for consistency
        #pt>3  |eta| < 2.4  dxy<= 0.05 dz <= 0.1 sip3d<=8  looseisoflag==pass
        getattr(module.Efficiencies, "Medium_pt_eta").BinnedVariables.tag_pt = cms.vdouble(3,9999)
        getattr(module.Efficiencies, "Medium_pt_eta").BinnedVariables.tag_abseta = cms.vdouble(0,2.4)
        getattr(module.Efficiencies, "Medium_pt_eta").BinnedVariables.tag_dxy = cms.vdouble(-0.05,0.05)
        getattr(module.Efficiencies, "Medium_pt_eta").BinnedVariables.dxy = cms.vdouble(-0.05,0.05)
        getattr(module.Efficiencies, "Medium_pt_eta").BinnedVariables.tag_dz = cms.vdouble(-0.1,0.1)
        getattr(module.Efficiencies, "Medium_pt_eta").BinnedVariables.dz = cms.vdouble(-0.1,0.1)
        getattr(module.Efficiencies, "Medium_pt_eta").BinnedVariables.SIP = cms.vdouble(0,8)
        getattr(module.Efficiencies, "Medium_pt_eta").BinnedVariables.tag_SIP = cms.vdouble(0,8)
        getattr(module.Efficiencies, "Medium_pt_eta").BinnedVariables.LoosePFIso = cms.vdouble(0.5,1.5)
        getattr(module.Efficiencies, "Medium_pt_eta").BinnedVariables.tag_LoosePFIso = cms.vdouble(0.5,1.5)

if "isoMu24eta2p1" in scenario:
	print("appending trigger isoMu24eta2p1")
	module.Categories.tag_IsoMu24_eta2p1 = cms.vstring("isomu24eta2p1", "dummy[pass=1,fail=0]")
	tag_IsoMu24_eta2p1 = cms.vstring("pass")
	getattr(module.Efficiencies, "Medium_pt_eta").BinnedVariables.tag_IsoMu24_eta2p1 = tag_IsoMu24_eta2p1
	#getattr(module.Efficiencies,"Medium_pt_eta").BinnedVariables.tag_IsoMu24_eta2p1 = cms.vdouble(0.5,1.5)


if "Mu7p5Tk2" in scenario:
        print("appending trigger Mu7p5Tk2")
        module.Categories.Mu7p5_Track2_Jpsi_TK = cms.vstring("Mu7p5Tk2", "dummy[pass=1,fail=0]")
        Mu7p5_Track2_Jpsi_TK = cms.vstring("pass")
        getattr(module.Efficiencies, "Medium_pt_eta").BinnedVariables.Mu7p5_Track2_Jpsi_TK = Mu7p5_Track2_Jpsi_TK

if "IsoTkMu22" in scenario:
        print("appending trigger tag_IsoTkMu22")
        module.Categories.tag_IsoTkMu22 = cms.vstring("isotkmu22", "dummy[pass=1,fail=0]")
        tag_IsoTkMu22 = cms.vstring("pass")
        getattr(module.Efficiencies, "Medium_pt_eta").BinnedVariables.tag_IsoTkMu22 = tag_IsoTkMu22


if "mu17" in scenario:
	print("appending trigger Mu17")
	module.Categories.tag_Mu17 = cms.vstring("mu17", "dummy[pass=1,fail=0]")
	tag_Mu17 = cms.vstring("pass")
	getattr(module.Efficiencies, "Medium_pt_eta").BinnedVariables.tag_Mu17 = tag_Mu17


if "_weight" in scenario:
	print("applying weights")
	getattr(module.Efficiencies, "Medium_pt_eta").UnbinnedVariables.append("weight")


print("begin fit")
setattr(process, "runtest",module)
process.p1 = cms.Path(module)
#process.p1 = cms.Path(process.TnP_Muon_ID)
#process.p2 = cms.Path(process.TnP_Muon_Iso)
