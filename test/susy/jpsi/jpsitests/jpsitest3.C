


void jpsitest2(){
/*Br   86 :GenPart_genPartIdxMother : Int_t index of the mother particle      *
*Entries :  1955951 : Total  Size=  163902967 bytes  File Size  =   14891764 *
*Baskets :      442 : Basket Size=     464384 bytes  Compression=  11.01     *
*............................................................................*
*Br   87 :GenPart_pdgId : Int_t PDG id                                       *
*Entries :  1955951 : Total  Size=  163898050 bytes  File Size  =   17127530 *
*Baskets :      442 : Basket Size=     464384 bytes  Compression=   9.57     *
*/



	TFile* f = TFile::Open("D8BCDB81-4844-E811-A71C-0025904C5DE0.root");

//patPackedGenParticles_packedGenParticles__PAT. 	

	 TTreeReader reader("Events", f);

      //  TTreeReaderValue<pat::PackedGenParticle> genparts(reader,"patPackedGenParticles_packedGenParticles__PAT.");
 // TTreeReaderValue<edm::Wrapper<vector<pat::PackedGenParticle> > > genparts(reader,"patPackedGenParticles_packedGenParticles__PAT.");
	TTreeReaderValue<vector<int>> pdg(reader,"patPackedGenParticles_packedGenParticles__PAT.");


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
