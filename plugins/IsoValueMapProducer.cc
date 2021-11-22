// -*- C++ -*-
//
// Package:    PhysicsTools/NanoAOD
// Class:      IsoValueMapProducer
// 
/**\class IsoValueMapProducer IsoValueMapProducer.cc PhysicsTools/NanoAOD/plugins/IsoValueMapProducer.cc

 Description: [one line class summary]

 Implementation:
     [Notes on implementation]
*/
//
// Original Author:  Marco Peruzzi
//         Created:  Mon, 04 Sep 2017 22:43:53 GMT
//
//


// system include files
#include <memory>

// user include files
#include "FWCore/Framework/interface/Frameworkfwd.h"
#include "FWCore/Framework/interface/global/EDProducer.h"

#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/MakerMacros.h"

#include "FWCore/ParameterSet/interface/ParameterSet.h"
#include "FWCore/Utilities/interface/StreamID.h"

#include "RecoEgamma/EgammaTools/interface/EffectiveAreas.h"

#include "DataFormats/PatCandidates/interface/Muon.h"
#include "DataFormats/PatCandidates/interface/Electron.h"
#include "DataFormats/PatCandidates/interface/Photon.h"
#include "DataFormats/PatCandidates/interface/IsolatedTrack.h"

//
// class declaration
//

template <typename T>
class IsoValueMapProducer : public edm::global::EDProducer<> {
   public:
  explicit IsoValueMapProducer(const edm::ParameterSet &iConfig):
    src_(consumes<edm::View<T>>(iConfig.getParameter<edm::InputTag>("src"))),
    relative_(iConfig.getParameter<bool>("relative"))
  {
    if ((typeid(T) == typeid(pat::Muon)) || (typeid(T) == typeid(pat::Electron)) || typeid(T) == typeid(pat::IsolatedTrack)) {
      produces<edm::ValueMap<float>>("miniIsoChg");
      produces<edm::ValueMap<float>>("miniIsoAll");
     // produces<edm::ValueMap<float>>("looseIsoFlag");//1 if pass iso ,0 if fail
      ea_miniiso_.reset(new EffectiveAreas((iConfig.getParameter<edm::FileInPath>("EAFile_MiniIso")).fullPath()));
      rho_miniiso_ = consumes<double>(iConfig.getParameter<edm::InputTag>("rho_MiniIso"));
    }
    if (typeid(T) == typeid(pat::Muon)){
  //    produces<edm::ValueMap<int>>("looseIsoFlag");
    }
    if ((typeid(T) == typeid(pat::Electron))) {
      produces<edm::ValueMap<float>>("PFIsoChg");
      produces<edm::ValueMap<float>>("PFIsoAll");
      produces<edm::ValueMap<float>>("PFIsoAll04");
      ea_pfiso_.reset(new EffectiveAreas((iConfig.getParameter<edm::FileInPath>("EAFile_PFIso")).fullPath()));
      rho_pfiso_ = consumes<double>(iConfig.getParameter<edm::InputTag>("rho_PFIso"));
    }
    else if ((typeid(T) == typeid(pat::Photon))) {
      produces<edm::ValueMap<float>>("PFIsoChg");
      produces<edm::ValueMap<float>>("PFIsoAll");
      mapIsoChg_ = consumes<edm::ValueMap<float> >(iConfig.getParameter<edm::InputTag>("mapIsoChg"));
      mapIsoNeu_ = consumes<edm::ValueMap<float> >(iConfig.getParameter<edm::InputTag>("mapIsoNeu"));
      mapIsoPho_ = consumes<edm::ValueMap<float> >(iConfig.getParameter<edm::InputTag>("mapIsoPho"));
      ea_pfiso_chg_.reset(new EffectiveAreas((iConfig.getParameter<edm::FileInPath>("EAFile_PFIso_Chg")).fullPath()));
      ea_pfiso_neu_.reset(new EffectiveAreas((iConfig.getParameter<edm::FileInPath>("EAFile_PFIso_Neu")).fullPath()));
      ea_pfiso_pho_.reset(new EffectiveAreas((iConfig.getParameter<edm::FileInPath>("EAFile_PFIso_Pho")).fullPath()));
      rho_pfiso_ = consumes<double>(iConfig.getParameter<edm::InputTag>("rho_PFIso"));
    }
  }
  ~IsoValueMapProducer() override {}
  
      static void fillDescriptions(edm::ConfigurationDescriptions& descriptions);

   private:

  void produce(edm::StreamID, edm::Event&, const edm::EventSetup&) const override;

      // ----------member data ---------------------------

  edm::EDGetTokenT<edm::View<T>> src_;
  bool relative_;
  edm::EDGetTokenT<double> rho_miniiso_;
  edm::EDGetTokenT<double> rho_pfiso_;
  edm::EDGetTokenT<edm::ValueMap<float>> mapIsoChg_;
  edm::EDGetTokenT<edm::ValueMap<float>> mapIsoNeu_;
  edm::EDGetTokenT<edm::ValueMap<float>> mapIsoPho_;
  std::unique_ptr<EffectiveAreas> ea_miniiso_;
  std::unique_ptr<EffectiveAreas> ea_pfiso_;
  std::unique_ptr<EffectiveAreas> ea_pfiso_chg_;
  std::unique_ptr<EffectiveAreas> ea_pfiso_neu_;
  std::unique_ptr<EffectiveAreas> ea_pfiso_pho_;
  float getEtaForEA(const T*) const;
  void doMiniIso(edm::Event&) const;
  void doPFIsoEle(edm::Event&) const;
  void doPFIsoPho(edm::Event&) const;
//  void doLooseFlag(edm::Event&) const;
};

//
// constants, enums and typedefs
//


//
// static data member definitions
//

template<typename T> float IsoValueMapProducer<T>::getEtaForEA(const T *obj) const{
  return obj->eta();
}
template<> float IsoValueMapProducer<pat::Electron>::getEtaForEA(const pat::Electron *el) const{
  return el->superCluster()->eta();
}
template<> float IsoValueMapProducer<pat::Photon>::getEtaForEA(const pat::Photon *ph) const{
  return ph->superCluster()->eta();
}



template <typename T>
void
IsoValueMapProducer<T>::produce(edm::StreamID streamID, edm::Event& iEvent, const edm::EventSetup& iSetup) const
{

 // if ((typeid(T) == typeid(pat::Muon)) || (typeid(T) == typeid(pat::Electron)) || typeid(T) == typeid(pat::IsolatedTrack)) { doMiniIso(iEvent); };
  if ((typeid(T) == typeid(pat::Muon)) || (typeid(T) == typeid(pat::Electron)) ){ doMiniIso(iEvent); };
  if ((typeid(T) == typeid(pat::Electron))) { doPFIsoEle(iEvent); }
  if ((typeid(T) == typeid(pat::Photon))) { doPFIsoPho(iEvent); }
 // if ((typeid(T) == typeid(pat::Muon)) || (typeid(T) == typeid(pat::Electron)) ){ doLooseFlag(iEvent);};
 // if ((typeid(T) == typeid(pat::Muon))){ doLooseFlag(iEvent);};
}
/*
template<typename T>
void
IsoValueMapProducer<T>::doLooseFlag(edm::Event& iEvent) const {}

//template<typename T>
template<>
void
IsoValueMapProducer<pat::Muon>::doLooseFlag(edm::Event& iEvent) const{
  edm::Handle<edm::View<pat::Muon>> src;
  iEvent.getByToken(src_, src);
  unsigned int nInput = src->size(); 
  std::vector<int> looseIsoFlag;
  looseIsoFlag.reserve(nInput);
  double zero = 0; 
  for (const auto & obj : *src){
	auto absPFiso = (obj.pfIsolationR03().sumChargedHadronPt + std::max(obj.pfIsolationR03().sumNeutralHadronEt + obj.pfIsolationR03().sumPhotonEt - obj.pfIsolationR03().sumPUPt/2.,zero));
//	std::cout<<absPFiso<<" ";
//    int flag;
    if( absPFiso >= (20.+ 300./obj.pt()) ){
 //       flag = 0;
    }
    else{
  //      flag = 1;
    }
    looseIsoFlag.push_back(0);

  }
  //std::cout<<std::endl;
  //std::cout<<std::endl;
  std::unique_ptr<edm::ValueMap<int>> looseIsoV(new edm::ValueMap<int>());
  edm::ValueMap<int>::Filler fillerLoose(*looseIsoV);
  fillerLoose.insert(src,looseIsoFlag.begin(), looseIsoFlag.begin());
  fillerLoose.fill();
  iEvent.put(std::move(looseIsoV),"looseIsoFlag");
}

*/

template<typename T>
void
IsoValueMapProducer<T>::doMiniIso(edm::Event& iEvent) const{

  edm::Handle<edm::View<T>> src;
  iEvent.getByToken(src_, src);
  edm::Handle<double> rho;
  iEvent.getByToken(rho_miniiso_,rho);
 
  //std::vector<int> looseIsoFlag;
  
  //double pfiso= 20;
  //double zero = 0.0;
  unsigned int nInput = src->size();
  //looseIsoFlag.reserve(nInput);  
  std::vector<float> miniIsoChg, miniIsoAll;
  miniIsoChg.reserve(nInput);
  miniIsoAll.reserve(nInput);
    for (const auto & obj : *src) { 
    auto iso = obj.miniPFIsolation();
    auto chg = iso.chargedHadronIso();
    auto neu = iso.neutralHadronIso();
    auto pho = iso.photonIso();
    auto ea = ea_miniiso_->getEffectiveArea(fabs(getEtaForEA(&obj)));
    float R = 10.0/std::min(std::max(obj.pt(), 50.0),200.0);
    ea *= std::pow(R/0.3,2);
    float scale = relative_ ? 1.0/obj.pt() : 1;
    miniIsoChg.push_back(scale*chg);
    miniIsoAll.push_back(scale*(chg+std::max(0.0,neu+pho-(*rho)*ea)));

   // pfiso = (obj.pfIsolationR03().sumChargedHadronPt + std::max(obj.pfIsolationR03().sumNeutralHadronEt + obj.pfIsolationR03().sumPhotonEt - obj.pfIsolationR03().sumPUPt/2.,zero));
   /*if( pfiso >= (20.+ 300./obj.pt()) ){
       looseIsoFlag.push_back(0);
    }
    else{
        looseIsoFlag.push_back(0);
    }*/
    
       
  }
  
  std::unique_ptr<edm::ValueMap<float>> miniIsoChgV(new edm::ValueMap<float>());
  edm::ValueMap<float>::Filler fillerChg(*miniIsoChgV);
  fillerChg.insert(src,miniIsoChg.begin(),miniIsoChg.end());
  fillerChg.fill();
  std::unique_ptr<edm::ValueMap<float>> miniIsoAllV(new edm::ValueMap<float>());
  edm::ValueMap<float>::Filler fillerAll(*miniIsoAllV);
  fillerAll.insert(src,miniIsoAll.begin(),miniIsoAll.end());
  fillerAll.fill();

    iEvent.put(std::move(miniIsoChgV),"miniIsoChg");
  iEvent.put(std::move(miniIsoAllV),"miniIsoAll");
/* 
  std::unique_ptr<edm::ValueMap<int>> looseIsoV(new edm::ValueMap<int>());
  edm::ValueMap<int>::Filler fillerLoose(*looseIsoV);
  fillerLoose.insert(src,looseIsoFlag.begin(), looseIsoFlag.begin());
  fillerLoose.fill();
  iEvent.put(std::move(looseIsoV),"looseIsoFlag");
*/

  }

template<>
void
IsoValueMapProducer<pat::Photon>::doMiniIso(edm::Event& iEvent) const {}


template<typename T>
void
IsoValueMapProducer<T>::doPFIsoEle(edm::Event& iEvent) const {}

template<>
void
IsoValueMapProducer<pat::Electron>::doPFIsoEle(edm::Event& iEvent) const{

  edm::Handle<edm::View<pat::Electron>> src;
  iEvent.getByToken(src_, src);
  edm::Handle<double> rho;
  iEvent.getByToken(rho_pfiso_,rho);
  
  unsigned int nInput = src->size();

  std::vector<float> PFIsoChg, PFIsoAll, PFIsoAll04;
  PFIsoChg.reserve(nInput);
  PFIsoAll.reserve(nInput);
  PFIsoAll04.reserve(nInput);
  
  for (const auto & obj : *src) { 
    auto iso = obj.pfIsolationVariables();
    auto chg = iso.sumChargedHadronPt;
    auto neu = iso.sumNeutralHadronEt;
    auto pho = iso.sumPhotonEt;
    auto ea = ea_pfiso_->getEffectiveArea(fabs(getEtaForEA(&obj)));
    float scale = relative_ ? 1.0/obj.pt() : 1;
    PFIsoChg.push_back(scale*chg);
    PFIsoAll.push_back(scale*(chg+std::max(0.0,neu+pho-(*rho)*ea)));
    PFIsoAll04.push_back(scale*(obj.chargedHadronIso()+std::max(0.0,obj.neutralHadronIso()+obj.photonIso()-(*rho)*ea*16./9.)));
  }
  
  std::unique_ptr<edm::ValueMap<float>> PFIsoChgV(new edm::ValueMap<float>());
  edm::ValueMap<float>::Filler fillerChg(*PFIsoChgV);
  fillerChg.insert(src,PFIsoChg.begin(),PFIsoChg.end());
  fillerChg.fill();
  std::unique_ptr<edm::ValueMap<float>> PFIsoAllV(new edm::ValueMap<float>());
  edm::ValueMap<float>::Filler fillerAll(*PFIsoAllV);
  fillerAll.insert(src,PFIsoAll.begin(),PFIsoAll.end());
  fillerAll.fill();
  std::unique_ptr<edm::ValueMap<float>> PFIsoAll04V(new edm::ValueMap<float>());
  edm::ValueMap<float>::Filler fillerAll04(*PFIsoAll04V);
  fillerAll04.insert(src,PFIsoAll04.begin(),PFIsoAll04.end());
  fillerAll04.fill();

  iEvent.put(std::move(PFIsoChgV),"PFIsoChg");
  iEvent.put(std::move(PFIsoAllV),"PFIsoAll");
  iEvent.put(std::move(PFIsoAll04V),"PFIsoAll04");

}

template<typename T>
void
IsoValueMapProducer<T>::doPFIsoPho(edm::Event& iEvent) const {}

template<>
void
IsoValueMapProducer<pat::Photon>::doPFIsoPho(edm::Event& iEvent) const {

  edm::Handle<edm::View<pat::Photon>> src;
  iEvent.getByToken(src_, src);
  edm::Handle<double> rho;
  iEvent.getByToken(rho_pfiso_,rho);
  edm::Handle<edm::ValueMap<float> > mapIsoChg;
  iEvent.getByToken(mapIsoChg_, mapIsoChg);
  edm::Handle<edm::ValueMap<float> > mapIsoNeu;
  iEvent.getByToken(mapIsoNeu_, mapIsoNeu);
  edm::Handle<edm::ValueMap<float> > mapIsoPho;
  iEvent.getByToken(mapIsoPho_, mapIsoPho);
  
  unsigned int nInput = src->size();

  std::vector<float> PFIsoChg, PFIsoAll;
  PFIsoChg.reserve(nInput);
  PFIsoAll.reserve(nInput);
  
  for (unsigned int i=0; i<nInput; i++){
    auto obj = src->ptrAt(i);
    auto chg = (*mapIsoChg)[obj];
    auto neu = (*mapIsoNeu)[obj];
    auto pho = (*mapIsoPho)[obj];
    auto ea_chg = ea_pfiso_chg_->getEffectiveArea(fabs(getEtaForEA(obj.get())));
    auto ea_neu = ea_pfiso_neu_->getEffectiveArea(fabs(getEtaForEA(obj.get())));
    auto ea_pho = ea_pfiso_pho_->getEffectiveArea(fabs(getEtaForEA(obj.get())));
    float scale = relative_ ? 1.0/obj->pt() : 1;
    PFIsoChg.push_back(scale*std::max(0.0,chg-(*rho)*ea_chg));
    PFIsoAll.push_back(PFIsoChg.back()+scale*(std::max(0.0,neu-(*rho)*ea_neu)+std::max(0.0,pho-(*rho)*ea_pho)));
  }
  
  std::unique_ptr<edm::ValueMap<float>> PFIsoChgV(new edm::ValueMap<float>());
  edm::ValueMap<float>::Filler fillerChg(*PFIsoChgV);
  fillerChg.insert(src,PFIsoChg.begin(),PFIsoChg.end());
  fillerChg.fill();
  std::unique_ptr<edm::ValueMap<float>> PFIsoAllV(new edm::ValueMap<float>());
  edm::ValueMap<float>::Filler fillerAll(*PFIsoAllV);
  fillerAll.insert(src,PFIsoAll.begin(),PFIsoAll.end());
  fillerAll.fill();

  iEvent.put(std::move(PFIsoChgV),"PFIsoChg");
  iEvent.put(std::move(PFIsoAllV),"PFIsoAll");

}



// ------------ method fills 'descriptions' with the allowed parameters for the module  ------------
template <typename T>
void
IsoValueMapProducer<T>::fillDescriptions(edm::ConfigurationDescriptions& descriptions) {
  edm::ParameterSetDescription desc;
  desc.add<edm::InputTag>("src")->setComment("input physics object collection");
  desc.add<bool>("relative")->setComment("compute relative isolation instead of absolute one");
  if ((typeid(T) == typeid(pat::Muon)) || (typeid(T) == typeid(pat::Electron)) || typeid(T) == typeid(pat::IsolatedTrack)) {
    desc.add<edm::FileInPath>("EAFile_MiniIso")->setComment("txt file containing effective areas to be used for mini-isolation pileup subtraction");
    desc.add<edm::InputTag>("rho_MiniIso")->setComment("rho to be used for effective-area based mini-isolation pileup subtraction");
  }
  if ((typeid(T) == typeid(pat::Electron))) {
    desc.add<edm::FileInPath>("EAFile_PFIso")->setComment("txt file containing effective areas to be used for PF-isolation pileup subtraction for electrons");
    desc.add<edm::InputTag>("rho_PFIso")->setComment("rho to be used for effective-area based PF-isolation pileup subtraction for electrons");
  }
  if ((typeid(T) == typeid(pat::Photon))) {
    desc.add<edm::InputTag>("mapIsoChg")->setComment("input charged PF isolation calculated in VID for photons");
    desc.add<edm::InputTag>("mapIsoNeu")->setComment("input neutral PF isolation calculated in VID for photons");
    desc.add<edm::InputTag>("mapIsoPho")->setComment("input photon PF isolation calculated in VID for photons");
    desc.add<edm::FileInPath>("EAFile_PFIso_Chg")->setComment("txt file containing effective areas to be used for charged PF-isolation pileup subtraction for photons");
    desc.add<edm::FileInPath>("EAFile_PFIso_Neu")->setComment("txt file containing effective areas to be used for neutral PF-isolation pileup subtraction for photons");
    desc.add<edm::FileInPath>("EAFile_PFIso_Pho")->setComment("txt file containing effective areas to be used for photon PF-isolation pileup subtraction for photons");
    desc.add<edm::InputTag>("rho_PFIso")->setComment("rho to be used for effective-area based PF-isolation pileup subtraction for photons");
  }
  std::string modname;
  if (typeid(T) == typeid(pat::Muon)) modname+="Muon";
  else if (typeid(T) == typeid(pat::Electron)) modname+="Ele";
  else if (typeid(T) == typeid(pat::Photon)) modname+="Pho";
  else if (typeid(T) == typeid(pat::IsolatedTrack)) modname+="IsoTrack";
  modname+="IsoValueMapProducer";
  descriptions.add(modname,desc);
}


typedef IsoValueMapProducer<pat::Muon> MuonIsoValueMapProducer;
typedef IsoValueMapProducer<pat::Electron> EleIsoValueMapProducer;
typedef IsoValueMapProducer<pat::Photon> PhoIsoValueMapProducer;
typedef IsoValueMapProducer<pat::IsolatedTrack> IsoTrackIsoValueMapProducer;

//define this as a plug-in
DEFINE_FWK_MODULE(MuonIsoValueMapProducer);
//DEFINE_FWK_MODULE(EleIsoValueMapProducer);
//DEFINE_FWK_MODULE(PhoIsoValueMapProducer);
//DEFINE_FWK_MODULE(IsoTrackIsoValueMapProducer);

