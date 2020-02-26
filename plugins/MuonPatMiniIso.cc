// system include files
#include <memory>
#include <cmath>

// user include files
#include "FWCore/Framework/interface/Frameworkfwd.h"
#include "FWCore/Framework/interface/EDProducer.h"

#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/MakerMacros.h"
#include "FWCore/Framework/interface/ESHandle.h"

#include "FWCore/ParameterSet/interface/ParameterSet.h"
#include "FWCore/ServiceRegistry/interface/Service.h"

#include "DataFormats/Math/interface/deltaR.h"
#include "DataFormats/Common/interface/ValueMap.h"
#include "DataFormats/MuonReco/interface/Muon.h"
#include "DataFormats/EgammaCandidates/interface/GsfElectron.h"
#include "DataFormats/VertexReco/interface/VertexFwd.h"
#include "DataFormats/VertexReco/interface/Vertex.h"
#include "DataFormats/ParticleFlowCandidate/interface/PFCandidate.h"
//#include "PhysicsTools/PatUtils/interface/MiniIsolation.h"
#include "PhysicsTools/PatUtils/interface/MiniIsolation.h"

//
// class declaration
//

class MuonPatMiniIso : public edm::EDProducer {
public:

//  typedef std::vector< edm::FwdPtr<reco::PFCandidate> > PFCollection;

  explicit MuonPatMiniIso(const edm::ParameterSet&);
  ~MuonPatMiniIso();

private:
  virtual void produce(edm::Event&, const edm::EventSetup&);

  // ----------member data ---------------------------
  const edm::EDGetTokenT<edm::View<reco::Muon>> probes_;    
// const edm::EDGetTokenT<PFCollection> pfCandidates_;
 const edm::EDGetTokenT<pat::PackedCandidateCollection> pfCandidates_;
 double dRCandProbeVeto_;
  double dRCandSoftActivityCone_;
  double CandPtThreshold_;
  double ChargedPVdZ_;
  bool usePUcands_;

  /// Store extra information in a ValueMap
  template<typename Hand, typename T>
  void storeMap(edm::Event &iEvent, 
  const Hand & handle,
  const std::vector<T> & values,
  const std::string    & label) const ;
};

//
// constants, enums and typedefs
//


//
// static data member definitions
//

//
// constructors and destructor
//
MuonPatMiniIso::MuonPatMiniIso(const edm::ParameterSet& iConfig):
probes_(consumes<edm::View<reco::Muon>>(iConfig.getParameter<edm::InputTag>("probes"))),
pfCandidates_(consumes<pat::PackedCandidateCollection>(iConfig.getParameter<edm::InputTag>("pfCandidates"))),
dRCandProbeVeto_(iConfig.getParameter<double>("dRCandProbeVeto")),
dRCandSoftActivityCone_(iConfig.getParameter<double>("dRCandSoftActivityCone")),
CandPtThreshold_(iConfig.getParameter<double>("CandPtThreshold"))
{
 // produces<edm::ValueMap<float> >("PATrelminiIso");
 // produces<edm::ValueMap<float> >("PATabsminiIso");
  produces<edm::ValueMap<float> >("PATminichiso");
  produces<edm::ValueMap<float> >("PATmininhiso");
  produces<edm::ValueMap<float> >("PATminiphiso");
  produces<edm::ValueMap<float> >("PATminipuiso");
}


MuonPatMiniIso::~MuonPatMiniIso()
{
}

 float miniIsoDr(const math::XYZTLorentzVector &p4, float mindr, float maxdr, float kt_scale) {
    return std::max(mindr, std::min(maxdr, float(kt_scale / p4.pt())));
  }
//
// member functions
//

// ------------ method called to produce the data  ------------
void
MuonPatMiniIso::produce(edm::Event& iEvent, const edm::EventSetup& iSetup)
{
  using namespace edm;

  // read input
  Handle<View<reco::Muon> > probes;
  iEvent.getByToken(probes_, probes);

  //Handle<View<reco::PFCandidate> > pfCandidates;
  Handle<pat::PackedCandidateCollection > pfCandidates;
  iEvent.getByToken(pfCandidates_, pfCandidates);
  const pat::PackedCandidateCollection* pfcands = &(*pfCandidates);

  View<reco::Muon>::const_iterator probe, endprobes=probes->end();
 // PFCollection::const_iterator iP, beginpf = pfCandidates->begin(), endpf=pfCandidates->end();
  unsigned int n = probes->size();
  
//  std::vector<float> reliso(n,0);
//  std::vector<float> absiso(n,0);
//  std::vector<float> relisoEA(n,0);
//  std::vector<float> absisoEA(n,0);
  pat::PFIsolation pfiso;

  std::vector<float> chisov(n,0);
  std::vector<float> nhisov(n,0);
  std::vector<float> phisov(n,0);
  std::vector<float> puisov(n,0);
  
	float mindr=0.05;
	 float maxdr=0.2 ;
	float kt_scale=10.0;
          float ptthresh=0.5;
	 float deadcone_ch=0.0001;
         float deadcone_pu=0.01;
	 float deadcone_ph=0.01;
	 float deadcone_nh=0.01;
          float dZ_cut=0.0;



  // loop on PROBES
  unsigned int imu = 0;
  for (probe = probes->begin(); probe != endprobes; ++probe, ++imu) {
    const reco::Muon &mu = *probe;
	const math::XYZTLorentzVector p4 = mu.p4();
//	reliso[imu]
//	pfiso = pat::getMiniPFIsolation(pfc, mu.p4());
//	pfiso = pat::getMiniPFIsolation(pfc ,mu.p4());
  //      reliso[imu] = 
   float chiso = 0, nhiso = 0, phiso = 0, puiso = 0;
    float drcut = miniIsoDr(p4, mindr, maxdr, kt_scale);
    for (auto const &pc : *pfcands) {
      float dr = deltaR(p4, pc.p4());
      if (dr > drcut)
        continue;
      float pt = pc.p4().pt();
      int id = pc.pdgId();
      if (std::abs(id) == 211) {
        bool fromPV = (pc.fromPV() > 1 || fabs(pc.dz()) < dZ_cut);
        if (fromPV && dr > deadcone_ch) {
          // if charged hadron and from primary vertex, add to charged hadron isolation
          chiso += pt;
        } else if (!fromPV && pt > ptthresh && dr > deadcone_pu) {
          // if charged hadron and NOT from primary vertex, add to pileup isolation
          puiso += pt;
        }
      }
      // if neutral hadron, add to neutral hadron isolation
      if (std::abs(id) == 130 && pt > ptthresh && dr > deadcone_nh)
        nhiso += pt;
      // if photon, add to photon isolation
      if (std::abs(id) == 22 && pt > ptthresh && dr > deadcone_ph)
        phiso += pt;
   }//end pfcand loop 
       chisov[imu] = chiso;
	nhisov[imu] = nhiso;
	phisov[imu] = phiso;
	puisov[imu] = puiso;
    
  }// end loop on probes

  storeMap(iEvent, probes, chisov, "PATminichiso");
  storeMap(iEvent, probes, nhisov, "PATmininhiso");
  storeMap(iEvent, probes, phisov, "PATminiphiso");
  storeMap(iEvent, probes, puisov, "PATminipuiso");
}

template<typename Hand, typename T>
void
MuonPatMiniIso::storeMap(edm::Event &iEvent,
const Hand & handle,
const std::vector<T> & values,
const std::string    & label) const {
  using namespace edm; using namespace std;
  unique_ptr<ValueMap<T> > valMap(new ValueMap<T>());
  typename edm::ValueMap<T>::Filler filler(*valMap);
  filler.insert(handle, values.begin(), values.end());
  filler.fill();
  iEvent.put(std::move(valMap), label);
}

//define this as a plug-in
DEFINE_FWK_MODULE(MuonPatMiniIso);
