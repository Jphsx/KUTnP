



scenarios = ["data2017_mu17", "mc2017_mu17"]

IDs = ["Gmedsip", "GminiIso6", "GminiIso5", "Gsiprelmediso5", "Medium", "SIP3D", "MiniIso6", "SIPrelMed", "Smedsip", "SminiIso6", "SminiIso5", "Ssiprelmediso5", "Bloosesip", "Bsiprelloose", "Bmini5relloose", "Loose", "GPmedsip","GPminiIso5" ]

fitmodels = ["E"]

import os
for scenario in scenarios:
	for ID in IDs:
		for fitmodel in fitmodels:

			cmd = "cmsRun muonID.py "+scenario+" "+ID+" "+fitmodel
			os.system(cmd)
			exit		
