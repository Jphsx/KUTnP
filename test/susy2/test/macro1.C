

void macro1(){
	
	TH1F* htsip_jmc = new TH1F("h1", "ntuple", 20, 0, 4);
	TH1F* htiso_jmc = new TH1F("h11", "ntuple", 20,0,4);
	TFile* f1 = TFile::Open("/home/t3-ku/janguian/HADD/tempstorage/TnP_JpsiPt82017_200File.root" );

	 TTreeReader myReader1("tpTree/fitter_tree", f1);

	 TTreeReaderValue<Float_t> tsip_jmc(myReader1, "tag_SIP");
	 TTreeReaderValue<Float_t> tw_jmc(myReader1, "weight");
	TTreeReaderValue<Float_t> tiso_jmc(myReader1, "miniIsoAll");
	while (myReader1.Next()) {
    
   	   htsip_jmc->Fill(*tsip_jmc,*tw_jmc );
	 // if(*tiso_jmc > 0){
	   htiso_jmc->Fill(*tiso_jmc,*tw_jmc);
	//	}
  	 }
   //	htsip_jmc->Draw();	
/////////////////////////	
	 TH1F* htsip_jdt = new TH1F("h2", "Data/MC Shape Comparison for SIP3D and Mini Isolation with J/#psi and Z Tag and Probe pairs;SIP3D || miniIso [GeV];Data/MC", 20, 0, 4);
	TH1F* htiso_jdt = new TH1F("h22", "ntuple", 20, 0, 4);
        TFile* f2 = TFile::Open("/home/t3-ku/janguian/jsingera/TnP/SingleMuon/TnP_SingleMuon2017C_jpsi_HADD/TnP_SingleMuon2017C_jpsi_ALL.root" );

         TTreeReader myReader2("tpTree/fitter_tree", f2);

         TTreeReaderValue<Float_t> tsip_jdt(myReader2, "tag_SIP");
	TTreeReaderValue<Float_t> tiso_jdt(myReader2, "miniIsoAll");
        while (myReader2.Next()) {
      // Just access the data as if myPx and myPy were iterators (note the '*'
      //       // in front of them):
      			
                        htsip_jdt->Fill(*tsip_jdt );
        //		if(*tiso_jdt > 0){
			htiso_jdt->Fill(*tiso_jdt );
	//		}
	}

	htsip_jmc->Scale(1./htsip_jmc->Integral());
	htsip_jdt->Scale(1./htsip_jdt->Integral());
//	htsip_jmc->SetLineColor(kRed);	
	htiso_jmc->Scale(1./htiso_jmc->Integral());
	htiso_jdt->Scale(1./htiso_jdt->Integral());	//htiso_jmc->SetLineColor(kRed);
	htsip_jdt->Divide(htsip_jmc);
	htiso_jdt->Divide(htiso_jmc);	


	htsip_jdt->SetLineColor(kRed);
	htsip_jdt->SetFillColor(kRed);
	htsip_jdt->SetMarkerStyle(25);
	htsip_jdt->SetMarkerColor(kRed);		

	htiso_jdt->SetLineColor(kRed);
	htiso_jdt->SetFillColor(kRed);
	htiso_jdt->SetMarkerStyle(21);
	htiso_jdt->SetMarkerColor(kRed);
//	TCanvas* c1 = new TCanvas();
//	htsip_jdt->Draw();
//	htsip_jmc->Draw("SAME");

//	TCanvas* c2 = new TCanvas();
//	htiso_jdt->Draw();
//	htiso_jmc->Draw("SAME");
	TCanvas* c1 = new TCanvas();
           htsip_jdt->Draw();	
	  htiso_jdt->Draw("SAME");
/////////////////////////


	TH1F* htsip_zmc = new TH1F("h3", "ntuple", 20, 0, 4);
	TH1F* hw = new TH1F("hw","ntuple",100,0,2);
	TH1F* htiso_zmc= new TH1F("h33", "ntuple", 20, 0, 4);
        TFile* f3 = TFile::Open("/home/t3-ku/janguian/CMSSW_10_2_5/src/MuonAnalysis/TagAndProbe/test/susy2/2017_Z/tnpZ_withNVtxWeights.root" );

         TTreeReader myReader3("tpTree/fitter_tree", f3);

         TTreeReaderValue<Float_t> tsip_zmc(myReader3, "tag_SIP");
        TTreeReaderValue<Float_t> tiso_zmc(myReader3, "miniIsoAll"); 
	TTreeReaderValue<Float_t> tw_zmc(myReader3, "weight");
        while (myReader3.Next()) {
      // Just access the data as if myPx and myPy were iterators (note the '*'
      //       // in front of them):
                 //       htsip_zmc->Fill(*tsip_zmc,*tw_zmc );
                 	if(*tw_zmc > 0){
                 	 htsip_zmc->Fill(*tsip_zmc, *tw_zmc);
		//	}
	//		if(*tiso_zmc > 0){
           		htiso_zmc->Fill(*tiso_zmc,*tw_zmc);
          	     	}
			hw->Fill(*tw_zmc);                         
        }
//          htsip_zmc->Draw();
//	  hw->Draw();
      //
//////////////////////////
	
	TH1F* htsip_zdt = new TH1F("h4", "ntuple", 20, 0, 4);
	TH1F* htiso_zdt= new TH1F("h44", "ntuple", 20, 0, 4);
        TFile* f4 = TFile::Open("/home/t3-ku/janguian/HADD/tempstorage/TnP_SingleMuon2017C_zmumu_1.root" );

         TTreeReader myReader4("tpTree/fitter_tree", f4);

         TTreeReaderValue<Float_t> tsip_zdt(myReader4, "tag_SIP");
         TTreeReaderValue<Float_t> tiso_zdt(myReader4, "miniIsoAll");
        while (myReader4.Next()) {

           htsip_zdt->Fill(*tsip_zdt);
	  htiso_zdt->Fill(*tiso_zdt);
         }

       // htsip_zdt->Draw();
	htsip_zmc->Scale(1./htsip_zmc->Integral());
        htsip_zdt->Scale(1./htsip_zdt->Integral());
        htsip_zdt->Divide(htsip_zmc);
//	htsip_zmc->Draw();
	
	htiso_zmc->Scale(1./htiso_zmc->Integral());
	htiso_zdt->Scale(1./htiso_zdt->Integral());
	htiso_zdt->Divide(htiso_zmc);

	htsip_zdt->SetLineColor(kBlue);
	htsip_zdt->SetFillColor(kBlue);
	htsip_zdt->SetMarkerStyle(24);
	htsip_zdt->SetMarkerSize(1);
	htsip_zdt->SetMarkerColor(4);
	htsip_zdt->Draw("SAME");
	
	htiso_zdt->SetLineColor(kBlue);
	htiso_zdt->SetFillColor(kBlue);
	htiso_zdt->SetMarkerStyle(20);
	htiso_zdt->SetMarkerSize(1);
	htsip_zdt->SetMarkerColor(4);
	htiso_zdt->Draw("SAME");


	auto legend = new TLegend(0.2, 0.2, .8, .8);
	  legend->SetNColumns(2);
 
   legend->AddEntry(htsip_jdt, "J/#psi #frac{SIP3D Data}{SIP3D MC}", "lp");
   legend->AddEntry(htsip_zdt, "Z #frac{SIP3D Data}{SIP3D MC}", "lp");
   legend->AddEntry(htiso_jdt, "J/#psi #frac{MiniIso Data}{MiniIso MC}", "lp");
   legend->AddEntry(htiso_zdt, "Z #frac{MiniIso Data}{MiniIso MC}", "lp");	

   legend->Draw();
        //htsip_zdt->Draw("SAMES");
//	htsip_zdt->Draw();	

	TFile* out = new TFile("plot.root","RECREATE");
	out->WriteTObject(c1);
	out->Write();
	out->Close();

}
