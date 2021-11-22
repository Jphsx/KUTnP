

//zdatatrigtest_201.root
//
#include<string>
#include "TFile.h"
#include "TTree.h"

int main(int argc, char *argv[]){
//void addBronze(std::string iFileName="zdatatrigtest_201.root"){

    std::string iFileName = std::string(argv[1]);
    TFile *iFile = TFile::Open(iFileName.c_str());
 //   TTreeReader myReader("tpTree/fitter_tree", iFile);
 //   TTreeReaderValue<Float_t> id(myReader, "AbsPFIso_All");
 //   TTreeReaderValue<Float_t> mini(myReader, "miniIsoAll");
 //   TTreeReaderValue<Int_t> pf(myReader, "Medium");
  
   // std::string iFileName = std::string(argv[1]);

    TTree  &t = * (TTree *) iFile->Get("tpTree/fitter_tree");
    Float_t AbsPFIso_All,miniIsoAll;
    Int_t Medium;
    t.SetBranchAddress("AbsPFIso_All",&AbsPFIso_All);
    t.SetBranchAddress("miniIsoAll",&miniIsoAll);
    t.SetBranchAddress("Medium",&Medium);
    TFile *oFile = new TFile("bronze_temp.root", "RECREATE");
    oFile->mkdir("tpTree")->cd();
    TTree *tOut = t.CloneTree(0);
    int Bronze=0;
    tOut->Branch("Bronze", &Bronze, "Bronze/I");
    
   // while (myReader.Next()) {
     for(int i=0, n= t.GetEntries(); i< n; ++i){
         t.GetEntry(i);
	 if(Medium<1 || miniIsoAll >4 || AbsPFIso_All>4 ){
	     Bronze=1;
	 }
	 else{
 	     Bronze=0;
	 }
	tOut->Fill();
     }         
 
//      if( *id<1 || *mini>4 || *pf>4 ){
//	Bronze=1;
  //    }
   //   else{
//	Bronze=0;
 //     }
 //          tOut->Fill();
//   }
//   tOut->Write();
   tOut->AutoSave();
  // iFile->Close();
   oFile->Close();

}
