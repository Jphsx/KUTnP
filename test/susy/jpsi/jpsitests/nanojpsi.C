#define nanojpsi_cxx
#include "nanojpsi.h"
#include <TH2.h>
#include <TStyle.h>
#include <TCanvas.h>

void nanojpsi::Loop()
{
//   In a ROOT session, you can do:
//      root> .L nanojpsi.C
//      root> nanojpsi t
//      root> t.GetEntry(12); // Fill t data members with entry number 12
//      root> t.Show();       // Show values of entry 12
//      root> t.Show(16);     // Read and show values of entry 16
//      root> t.Loop();       // Loop on all entries
//

//     This is the loop skeleton where:
//    jentry is the global entry number in the chain
//    ientry is the entry number in the current Tree
//  Note that the argument to GetEntry must be:
//    jentry for TChain::GetEntry
//    ientry for TTree::GetEntry and TBranch::GetEntry
//
//       To read only selected branches, Insert statements like:
// METHOD1:
//    fChain->SetBranchStatus("*",0);  // disable all branches
//    fChain->SetBranchStatus("branchname",1);  // activate branchname
// METHOD2: replace line
//    fChain->GetEntry(jentry);       //read all branches
//by  b_branchname->GetEntry(ientry); //read only this branch
   if (fChain == 0) return;

   Long64_t nentries = fChain->GetEntriesFast();

   Long64_t nbytes = 0, nb = 0;
   for (Long64_t jentry=0; jentry<nentries;jentry++) {
      Long64_t ientry = LoadTree(jentry);
      if (ientry < 0) break;
      nb = fChain->GetEntry(jentry);   nbytes += nb;
      // if (Cut(ientry) < 0) continue;
      //
      //
      //
      //
      //
     	for(int i=0; i<nGenPart; i++){
		if( GenPart_pdgId[i] == 13 ){
			int momidx = GenPart_genPartIdxMother[i];
			muonparent->Fill(GenPart_pdgId[momidx]);
			

			
			
		}

		if( GenPart_pdgId[i] == 443){
			int momidx = GenPart_genPartIdxMother[i];
			jpsparent->Fill(GenPart_pdgId[momidx]);
			std::cout<<GenPart_pdgId[momidx]<<" ";
		}
		std::cout<<std::endl;

		
//Muon_miniPFRelIso_all
//Muon_pt

	}

	for(int i=0; i<nMuon; i++){
		double absiso = Muon_pt[i]* Muon_miniPFRelIso_all[i];
		miniso->Fill(absiso);
	}	
		
	//	miniso;
       /// muonparent;
       // jpsparent;
	



      
   }
	TCanvas* c1 = new TCanvas();
	muonparent->Draw();
	c1->Print("muonparent.pdf");

	TCanvas* c2 = new TCanvas();
	jpsparent->Draw();
	c2->Print("jparent.pdf");
	

	TCanvas* c3 = new TCanvas();
	miniso->Draw();
	c3->Print("iso.pdf");



	
}
