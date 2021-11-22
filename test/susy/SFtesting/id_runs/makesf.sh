


#root -b -q -l 'extractPlotsAndComputeTheSFs.C("Medium_PtEtaBins","TnPZ_susyID_GOLD_Data.root","TnPZ_susyID_GOLD_MC_weight.root")'
#python createJsonFile.py EfficienciesAndSF_Medium_pt_eta.root TnPZ_SF_GOLD.json
#mv EfficienciesandSF_Medium_pt_eta.root EfficienciesAndSF_GOLD_Z.root


#root -b -q -l 'extractPlotsAndComputeTheSFs.C("Medium_PtEtaBins","TnPZ_susyID_MEDSIP_Data.root","TnPZ_susyID_MEDSIP_MC_weight.root")'
#python createJsonFile.py EfficienciesAndSF_Medium_pt_eta.root TnPZ_SF_MEDSIP.json
#mv EfficienciesAndSF_Medium_pt_eta.root EfficienciesAndSF_MEDSIP_Z.root

#root -b -q -l 'extractPlotsAndComputeTheSFs.C("Medium_PtEtaBins","TnPZ_susyID_MINI_Data.root","TnPZ_susyID_MINI_MC_weight.root")'
#python createJsonFile.py EfficienciesAndSF_Medium_pt_eta.root TnPZ_SF_MINI.json
#mv EfficienciesAndSF_Medium_pt_eta.root EfficienciesAndSF_MINI_Z.root

#root -b -q -l 'extractPlotsAndComputeTheSFs.C("Medium_PtEtaBins","TnPZ_susyID_SIP_Data.root","TnPZ_susyID_SIP_MC_weight.root")'
#python createJsonFile.py EfficienciesAndSF_Medium_pt_eta.root TnPZ_SF_SIP.json
#mv EfficienciesAndSF_Medium_pt_eta.root EfficienciesAndSF_SIP_Z.root

#root -b -q -l 'extractPlotsAndComputeTheSFs.C("Medium_PtEtaBins","TnPZ_susyID_MED_Data.root","TnPZ_susyID_MED_MC_weight.root")'
#python createJsonFile.py EfficienciesAndSF_Medium_pt_eta.root TnPZ_SF_MED.json
#mv EfficienciesAndSF_Medium_pt_eta.root EfficienciesAndSF_MED_Z.root


root -b -q -l 'extractPlotsAndComputeTheSFs.C("Medium_PtEtaBins","TnPZ_susyID_GOLDMINI_Data.root","TnPZ_susyID_GOLDMINI_MC_weight.root")'
python createJsonFile.py EfficienciesAndSF_Medium_pt_eta.root TnPZ_SF_GOLDMINI.json
mv EfficienciesAndSF_Medium_pt_eta.root EfficienciesAndSF_GOLDMINI_Z.root

root -b -q -l 'extractPlotsAndComputeTheSFs.C("Medium_PtEtaBins","TnPZ_susyID_GOLDMINI_Data_fine.root","TnPZ_susyID_GOLDMINI_MC_weight_fine.root")'
python createJsonFile.py EfficienciesAndSF_Medium_pt_eta.root TnPZ_SF_GOLDMINI_fine.json
mv EfficienciesAndSF_Medium_pt_eta.root EfficienciesAndSF_GOLDMINI_fine_Z.root




