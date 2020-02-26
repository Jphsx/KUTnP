

instructions to build

	cmsrel CMSSW_10_2_5

	cd CMSSW_10_2_5/src

	cmsenv
	
	git clone https://github.com/Jphsx/KUTnP.git MuonAnalysis/TagAndProbe -b 94_newSelector

need to also get pat tools

	git cms-addpkg PhysicsTools/PatAlgos


next build
	
	scram b


KU SUSY related files are located in:

	/MuonAnalysis/TagAndProbe/test/susy

Muon POG old code is located in:
	
	/MuonAnalysis/TagAndProbe/test/zmumu
	/MuonAnalysis/TagAndProbe/test/jpsi
	//MuonAnalysis/TagAndProbe/test/upsilon
