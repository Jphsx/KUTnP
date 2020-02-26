


void jpsitest(){

	TFile* nano = TFile::Open("./648DFFC7-4044-E811-A930-0025905C42A4.root");
	TFile* aod = TFile::Open("../tnpJ_MC.root");
	//are there identical events in nano vs mini????
	TH1D* mll = new TH1D("mll","dilep mass",20,0,5);	
	TH1D* ddz = new TH1D("ddz","dz1-dz2",41,-2.,2);

	 TTreeReader aodReader("tpTree/fitter_tree", aod);

//	 TTreeReaderValue<edm::Wrapper<vector<reco::Muon> > > myMuons(aodReader, "recoMuons_muons__RECO.");
	TTreeReaderValue<Float_t> tagpt(aodReader,"tag_pt");
	TTreeReaderValue<Float_t> tageta(aodReader,"tag_eta");
	TTreeReaderValue<Float_t> tagphi(aodReader,"tag_phi");
	TTreeReaderValue<ULong64_t> tagevent(aodReader,"event");


	TTreeReaderValue<Float_t> propt(aodReader, "pt");
	TTreeReaderValue<Float_t> proeta(aodReader,"eta");
	TTreeReaderValue<Float_t> prophi(aodReader,"phi");

	//TTreeReaderValue<Float_t> miniIso(aodReader,"pfCombAbsMiniIsoEACorr");
	TTreeReaderValue<Float_t> miniIso(aodReader,"miniIsoAll");
	TTreeReaderValue<Float_t> SIP(aodReader,"SIP");

	 TTreeReader nanoReader("Events", nano);

	TTreeReaderValue<vector<pat::Muon> > minimu(nanoReader,"patMuons_slimmedMuons__PAT.obj");
	
	//TTreeReaderValue<vector<double> > nanoPt(nanoReader, "Muon_pt");
	//TTreeReaderValue<vector<double> > nanoPhi(nanoReader, "Muon_phi");
	//  TTreeReaderArray<Float_t> nanoPt = {nanoReader, "Muon_pt"};
	//   TTreeReaderArray<Float_t> nanoPhi = {nanoReader, "Muon_phi"};
//	TTreeReaderArray<Float_t>  nanoEta = {nanoReader, "Muon_eta"};
//	TTreeReaderArray<Float_t>  nanoIso = {nanoReader, "Muon_miniPFRelIso_all"};
//	TTreeReaderArray<Float_t> nanoSIP = {nanoReader, "Muon_sip3d"};
//	TTreeReaderValue<ULong64_t> nanoevent = {nanoReader, "Events"};	


	//double pt,phi,px,py;
	//phi = -1;
	//pt = -1;
	std::vector<double> aodpt{};
	std::vector<double> aodphi{};
	std::vector<double> nanopt{};
	std::vector<double> nanophi{};
	int nnano;
	int nmuon;
	int cnt = 0;
	int nanocnt = 0;

	int cutoff = 0;

	std::vector<int> nmatches{};
	std::vector<std::vector<int>> matchcnts{};

	double dz1,dz2;
	dz1 = -1;
	dz2 = -1;
	while(nanoReader.Next()){
              nnano = (*minimu).size();
	      std::vector<pat::Muon> mus = (*minimu);
			
		if(nnano>=1){
			TLorentzVector r1;
			r1.SetPtEtaPhiM(mus[0].pt(),mus[0].eta(),mus[0].phi(),0.10566);
			r1.Print();
			dz1 = mus[0].dB(pat::Muon::PVDZ);	
			TLorentzVector r2;
                        r2.SetPtEtaPhiM(mus[1].pt(),mus[1].eta(),mus[1].phi(),0.10566);
			r2.Print();
			dz2 = mus[1].dB(pat::Muon::PVDZ);
			TLorentzVector r1r2;
			r1r2 = r1+r2;
			std::cout<<"r1r2 "<< r1r2.Pt()<<"       "<<r1r2.Eta()<<"        "<<r1r2.Phi()<<"        "<<r1r2.M()<<std::endl;
			std::cout<<"dzs "<<dz1<<"	"<<dz2<<"	"<<dz1-dz2<<std::endl;
			mll->Fill(r1r2.M());
			ddz->Fill(dz1-dz2);

		}
		std::cout<<std::endl;
		std::cout<<std::endl;
		if(cutoff > 1000) break;
		cutoff++;
	}
	TCanvas* c1 = new TCanvas();
	mll->Draw();
	TCanvas* c2 = new TCanvas();
	ddz->Draw();
		//try to match muons
/*	 while (aodReader.Next()) {
	
	std::cout<<std::endl;
		std::cout<<"Tag "<< *tagpt <<"		"<< *tageta << "	 "<< *tagphi <<std::endl;
		std::cout<<"Pro "<< *propt <<"		"<< *proeta << "	 "<< *prophi <<"	"<< *miniIso << "	   "<<*SIP<<std::endl;
		TLorentzVector tg;
		tg.SetPtEtaPhiM(*tagpt, *tageta, *tagphi, 0.10566);
		TLorentzVector pr;
		pr.SetPtEtaPhiM(*propt, *proeta, *prophi, 0.10566);
		TLorentzVector mumu;
		mumu= tg+pr;
	
		std::cout<<"mumu "<< mumu.Pt()<<"	"<<mumu.Eta()<<"	"<<mumu.Phi()<<"	"<<mumu.M()<<std::endl;


				nnano = 0;
				//scan all of nanoaod count how many 
				while(nanoReader.Next()){
					nnano = nanoPt.GetSize();
					if( *nanoevent == *tagevent ){
						std::cout<<"event number match found"<<std::endl;
						//print out muons and vals
						for(int j=0; j<nnano;j++){
							std::cout<<"muon "<<j<<" "<<nanoPt[j]<<"	"<<nanoEta[j]<<"	"<<nanoPhi[j]<<"	"<<nanoPt[j]*nanoIso[j]<<"	"<<nanoSIP[j]<<std::endl;	
						//	if((fabs(*propt - nanoPt[j]) <0.001)  && ( fabs(*prophi - nanoPhi[j]) <0.001) && (fabs(*proeta - nanoEta[j]) < 0.001)){
						//		dsip->Fill( *SIP - nanoSIP[j] );
						//		dmin->Fill( *miniIso - nanoPt[j]*nanoIso[j] );
						//		std::cout<<"FILL DSIP"<<std::endl;
						//		cutoff++;
						//	} 
						}
					//if there are two muons, add the leading pt pair
					if(nnano>=2){
						TLorentzVector r1;
						r1.SetPtEtaPhiM(nanoPt[0],nanoEta[0],nanoPhi[0],0.10566);
						TLorentzVector r2;
                                                r2.SetPtEtaPhiM(nanoPt[1],nanoEta[1],nanoPhi[1],0.10566);
						TLorentzVector r1r2;
						r1r2 = r1+r2;
						std::cout<<"r1r2 "<< r1r2.Pt()<<"       "<<r1r2.Eta()<<"        "<<r1r2.Phi()<<"        "<<r1r2.M()<<std::endl;


					}
					std::cout<<std::endl;
					std::cout<<std::endl;
						break;
					}
							nanocnt++;
				
				}
				nanoReader.Restart();
		
			if(cutoff>10)break;
		
	
		cnt++;

	}
*/
/*	TCanvas* c = new TCanvas();
	c->SetLogy();
	//dsip->Draw();
	dmin->Draw();
	c->Print("dmin_Mini.pdf");
	TCanvas* c1 = new TCanvas();
	c1->SetLogy();
	dsip->Draw();
	c1->Print("dsip_Mini.pdf");
*/
}
