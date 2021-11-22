




root -b -q -l 'extractPlotsAndComputeTheSFs.C("Medium_PtEtaBins","./fit_output/TnPJ_MuonID_data2017_mu17_Gmedsip2_E.root","./fit_output/TnPJ_MuonID_mc2017_weight_mu17_Gmedsip2_E.root")'
python createJsonFile.py EfficienciesAndSF_Medium_pt_eta.root ./sf_output/TnPJ_mu17_Gmedsip2_E.json
mv EfficienciesAndSF_Medium_pt_eta.root ./sf_output/EffandSF_J_mu17_Gmedsip2_E.root


root -b -q -l 'extractPlotsAndComputeTheSFs.C("Medium_PtEtaBins","./fit_output/TnPJ_MuonID_data2017_mu17_Smedsip2_E.root","./fit_output/TnPJ_MuonID_mc2017_weight_mu17_Smedsip2_E.root")'
python createJsonFile.py EfficienciesAndSF_Medium_pt_eta.root ./sf_output/TnPJ_mu17_Smedsip2_E.json
mv EfficienciesAndSF_Medium_pt_eta.root ./sf_output/EffandSF_J_mu17_Smedsip2_E.root


#root -b -q -l 'extractPlotsAndComputeTheSFs.C("Medium_PtEtaBins","./fit_output/TnPJ_MuonID_data2017_mu17_GminiIso5_E.root","./fit_output/TnP_MuonID_mc2017_weight_mu17_GminiIso5_A.root")'
#python createJsonFile.py EfficienciesAndSF_Medium_pt_eta.root ./sf_output/TnPZ_mu17_GminiIso5_A.json
#mv EfficienciesAndSF_Medium_pt_eta.root ./sf_output/EffandSF_Z_mu17_GminiIso5_A.root
