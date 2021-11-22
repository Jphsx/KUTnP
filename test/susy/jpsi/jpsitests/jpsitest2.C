


void jpsitest2(){

	TFile* f = TFile::Open("648DFFC7-4044-E811-A930-0025905C42A4.root");

//patPackedGenParticles_packedGenParticles__PAT. 	

	 TTreeReader reader("Events", f);

      //  TTreeReaderValue<pat::PackedGenParticle> genparts(reader,"patPackedGenParticles_packedGenParticles__PAT.");
  TTreeReaderValue<edm::Wrapper<vector<pat::PackedGenParticle> > > genparts(reader,"patPackedGenParticles_packedGenParticles__PAT.");


	TH1D* muparent = new TH1D("mu","muparent abs(pdg)",1000,1,1000);
	TH1D* jpsiparent = new TH1D("jpsi","jpsiparent abs(pdg)",1000,1,1000);

	 while(reader.Next()){
		//Int_t pdgs = (*genparts).pdgId();
	//	std::cout<<pdgs<< " ";
	//	for(int i=0; i < 
	//	pdgId_	
		int size = (*genparts)->size();
//		std::cout<< size<< " ";
		for(int i=0; i<size; i++){
			if( (*genparts)->at(i).pdgId()  == 13 ){
				int mompdg = (*genparts)->at(i).mother(0)->pdgId();
				std::cout<<mompdg<<" ";
				
			}
		}	
		
		break;
	}
	


}
