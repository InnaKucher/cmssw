import FWCore.ParameterSet.Config as cms

hltobject = cms.EDAnalyzer("TriggerObjectAnalyzer",
   processName = cms.string("HLT"),
   treeName = cms.string("JetTriggers"),
   triggerResults = cms.InputTag("TriggerResults","","HLT"),
   triggerEvent = cms.InputTag("hltTriggerSummaryAOD","","HLT")
)

trigger_list_data = cms.vstring(
   'HLT_HIL3Mu3Eta2p5_PuAK4CaloJet40Eta2p1_v',
   'HLT_HIL3Mu3Eta2p5_PuAK4CaloJet60Eta2p1_v',
   'HLT_HIL3Mu3Eta2p5_PuAK4CaloJet80Eta2p1_v',
   'HLT_HIL3Mu3Eta2p5_PuAK4CaloJet100Eta2p1_v',
   'HLT_HIL3Mu5Eta2p5_PuAK4CaloJet40Eta2p1_v',
   'HLT_HIL3Mu5Eta2p5_PuAK4CaloJet60Eta2p1_v',
   'HLT_HIL3Mu5Eta2p5_PuAK4CaloJet80Eta2p1_v',
   'HLT_HIL3Mu5Eta2p5_PuAK4CaloJet100Eta2p1_v',
   )

trigger_list_mc = trigger_list_data.__add__([
   ])
