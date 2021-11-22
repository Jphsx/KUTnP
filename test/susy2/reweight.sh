#original reweighting
#root -l -b -q /home/t3-ku/janguian/HADD/tempstorage/TnP_ZmumuM502017_100File.root /home/t3-ku/janguian/HADD/tempstorage/TnP_SingleMuon2017C_zmumu_1.root addNVtxWeight.cxx++



#reweighting for boosted MC with more files, used for finer binning on SF
#root -l -b -q /home/t3-ku/janguian/HADD/tempstorage/TnP_ZmumuM502017_200File.root /home/t3-ku/janguian/jsingera/TnP/SingleMuon/TnP_SingleMuon2017C_zmumu_HADD/TnP_SingleMuon2017C_zmumu_1.root /home/t3-ku/janguian/jsingera/TnP/SingleMuon/TnP_SingleMuon2017C_zmumu_HADD/TnP_SingleMuon2017C_zmumu_2.root /home/t3-ku/janguian/jsingera/TnP/SingleMuon/TnP_SingleMuon2017C_zmumu_HADD/TnP_SingleMuon2017C_zmumu_3.root addNVtxWeight.cxx++

###################################################################
#reweighting done from 11-18-20 crab runs
#root -l -b -q /home/t3-ku/janguian/jsingera/TnP/DYJetsToLL_M-50_TuneCP5_13TeV-madgraphMLM-pythia8/TnP_ZmumuM502017_zmumu_HADD/TnP_ZmumuM502017.root /home/t3-ku/janguian/jsingera/TnP/SingleMuon/TnP_SingleMuon2017C_zmumu_HADD/TnP_SingleMuon2017C_zmumu_1.root /home/t3-ku/janguian/jsingera/TnP/SingleMuon/TnP_SingleMuon2017C_zmumu_HADD/TnP_SingleMuon2017C_zmumu_2.root /home/t3-ku/janguian/jsingera/TnP/SingleMuon/TnP_SingleMuon2017C_zmumu_HADD/TnP_SingleMuon2017C_zmumu_3.root /home/t3-ku/janguian/jsingera/TnP/SingleMuon/TnP_SingleMuon2017C_zmumu_HADD/TnP_SingleMuon2017C_zmumu_4.root addNVtxWeight.cxx++


#root -l -b -q /home/t3-ku/janguian/jsingera/TnP/JpsiToMuMu_JpsiPt8_TuneCP5_13TeV-pythia8/TnP_JpsiPt82017_jpsi_HADD/TnP_JpsiPt82017.root /home/t3-ku/janguian/jsingera/TnP/SingleMuon/TnP_SingleMuon2017C_jpsi_HADD/TnP_SingleMuon2017C_jpsi_1.root /home/t3-ku/janguian/jsingera/TnP/SingleMuon/TnP_SingleMuon2017C_jpsi_HADD/TnP_SingleMuon2017C_jpsi_2.root /home/t3-ku/janguian/jsingera/TnP/SingleMuon/TnP_SingleMuon2017C_jpsi_HADD/TnP_SingleMuon2017C_jpsi_3.root /home/t3-ku/janguian/jsingera/TnP/SingleMuon/TnP_SingleMuon2017C_jpsi_HADD/TnP_SingleMuon2017C_jpsi_2.root /home/t3-ku/janguian/jsingera/TnP/SingleMuon/TnP_SingleMuon2017C_jpsi_HADD/TnP_SingleMuon2017C_jpsi_4.root addNVtxWeight.cxx++i

#reweighting multiyear 1-14-21
#z2016
#root -l -b -q /home/t3-ku/janguian/jsingera/TnP/DYJetsToLL_M-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/TnP_ZmumuM502016_zmumu_HADD/TnP_ZmumuM502016.root /home/t3-ku/janguian/jsingera/TnP/SingleMuon/TnP_SingleMuon2016C_zmumu_HADD/TnP_SingleMuon2016C_zmumu.root addNVtxWeight.cxx++

#jpsi2016
#root -l -b -q /home/t3-ku/janguian/jsingera/TnP/JpsiToMuMu_JpsiPt8_TuneCUEP8M1_13TeV-pythia8/TnP_JpsiPt82016_jpsi_HADD/TnP_JpsiPt82016.root /home/t3-ku/janguian/jsingera/TnP/SingleMuon/TnP_SingleMuon2016C_jpsi_HADD/TnP_SingleMuon2016C_jpsi_1.root /home/t3-ku/janguian/jsingera/TnP/SingleMuon/TnP_SingleMuon2016C_jpsi_HADD/TnP_SingleMuon2016C_jpsi_2.root addNVtxWeight.cxx+


#z 2018
#root -l -b -q /home/t3-ku/janguian/jsingera/TnP/DYJetsToLL_M-50_TuneCP5_13TeV-madgraphMLM-pythia8/TnP_ZmumuM502018_zmumu_HADD/TnP_ZmumuM502018.root /home/t3-ku/janguian/jsingera/TnP/SingleMuon/TnP_SingleMuon2018A_zmumu_HADD/TnPSingleMuon2018A_zmumu_1.root /home/t3-ku/janguian/jsingera/TnP/SingleMuon/TnP_SingleMuon2018A_zmumu_HADD/TnPSingleMuon2018A_zmumu_2.root addNVtxWeight.cxx+

#j 2018
#root -l -b -q /home/t3-ku/janguian/jsingera/TnP/JpsiToMuMu_JpsiPt8_TuneCP5_13TeV-pythia8/TnP_JpsiPt82018_jpsi_HADD/TnP_JpsiPt82018.root /home/t3-ku/janguian/jsingera/TnP/SingleMuon/TnP_SingleMuon2018A_jpsi_HADD/TnPSingleMuon2018A_jpsi_1.root /home/t3-ku/janguian/jsingera/TnP/SingleMuon/TnP_SingleMuon2018A_jpsi_HADD/TnPSingleMuon2018A_jpsi_2.root addNVtxWeight.cxx+



#reweighting for charmonium/ jpsi central samples
#2016
#echo "Running 2016"
#root -l -b -q /home/t3-ku/janguian/jsingera/TnP/CentralSamples/TnPTreeJPsi_80X_JpsiToMuMu_JpsiPt8_Pythia8.root /home/t3-ku/janguian/jsingera/TnP/CentralSamples/TnPTreeJPsi_LegacyRereco07Aug17_Charmonium_Run2016Bver2_GoldenJSON.root addNVtxWeight.cxx+
#mv tnpZ_withNVtxWeights.root /home/t3-ku/janguian/jsingera/TnP/CentralSamples/TnPTreeJPsi_80X_JpsiToMuMu_JpsiPt8_Pythia8_WEIGHT.root
#mv nVtx.png nVtx_jpsi2016.png

#2017
echo "Running 2017"
root -l -b -q /home/t3-ku/janguian/jsingera/TnP/CentralSamples/TnPTreeJPsi_94X_JpsiToMuMu_Pythia8.root /home/t3-ku/janguian/TnPCentralSamples/TnPTreeJPsi_17Nov2017_Charmonium_Run2017Cv1_Full_GoldenJSON.root /home/t3-ku/janguian/TnPCentralSamples/TnPTreeJPsi_17Nov2017_Charmonium_Run2017Dv1_Full_GoldenJSON.root addNVtxWeight.cxx+
mv tnpZ_withNVtxWeights.root /home/t3-ku/janguian/jsingera/TnP/CentralSamples/TnPTreeJPsi_94X_JpsiToMuMu_Pythia8_WEIGHT.root
mv nVtx.png nVtx_jpsi2017.png

#2018 
#echo "Running 2018"
#root -l -b -q /home/t3-ku/janguian/jsingera/TnP/CentralSamples/TnPTreeJPsi_102XAutumn18_JpsiToMuMu_JpsiPt8_Pythia8.root /home/t3-ku/janguian/jsingera/TnP/CentralSamples/TnPTreeJPsi_17Sep2018_Charmonium_Run2018Av1_GoldenJSON.root /home/t3-ku/janguian/jsingera/TnP/CentralSamples/TnPTreeJPsi_17Sep2018_Charmonium_Run2018Bv1_GoldenJSON.root /home/t3-ku/janguian/jsingera/TnP/CentralSamples/TnPTreeJPsi_17Sep2018_Charmonium_Run2018Cv1_GoldenJSON.root addNVtxWeight.cxx+
#mv tnpZ_withNVtxWeights.root /home/t3-ku/janguian/jsingera/TnP/CentralSamples/TnPTreeJPsi_102XAutumn18_JpsiToMuMu_JpsiPt8_Pythia8_WEIGHT.root
#mv nVtx.png nVtx_jpsi2018.png

