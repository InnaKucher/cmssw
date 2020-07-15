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
   'HLT_HIL3Mu3Eta2p5_PuAK4CaloJet40Eta2p1_FilterDr_v',
   'HLT_HIL3Mu3Eta2p5_PuAK4CaloJet60Eta2p1_FilterDr_v',
   'HLT_HIL3Mu3Eta2p5_PuAK4CaloJet80Eta2p1_FilterDr_v',
   'HLT_HIL3Mu3Eta2p5_PuAK4CaloJet100Eta2p1_FilterDr_v',
   'HLT_HIL3Mu5Eta2p5_PuAK4CaloJet40Eta2p1_FilterDr_v',
   'HLT_HIL3Mu5Eta2p5_PuAK4CaloJet60Eta2p1_FilterDr_v',
   'HLT_HIL3Mu5Eta2p5_PuAK4CaloJet80Eta2p1_FilterDr_v',
   'HLT_HIL3Mu5Eta2p5_PuAK4CaloJet100Eta2p1_FilterDr_v',
   'HLT_HIPuAK4CaloJet40Eta5p1_v',
   'HLT_HIPuAK4CaloJet60Eta5p1_v',
   'HLT_HIPuAK4CaloJet80Eta5p1_v',
   'HLT_HIPuAK4CaloJet100Eta5p1_v',
   'HLT_HIPuAK4CaloJet120Eta5p1_v',
   'HLT_HIPuAK4CaloJet40Fwd_v',
   'HLT_HIPuAK4CaloJet60Fwd_v',
   'HLT_HIPuAK4CaloJet80Fwd_v',
   'HLT_HIPuAK4CaloJet100Fwd_v',
   'HLT_HIPuAK4CaloJet120Fwd_v',
   'HLT_HIPuAK4CaloJet80_35_Eta1p1_v',
   'HLT_HIPuAK4CaloJet100_35_Eta1p1_v',
   'HLT_HIPuAK4CaloJet80_35_Eta0p7_v',
   'HLT_HIPuAK4CaloJet100_35_Eta0p7_v',
   'HLT_HIPuAK4CaloJet80_45_45_Eta2p1_v',
   'HLT_HIPuAK4CaloJet60Eta2p4_DeepCSV0p4_v',
   'HLT_HIPuAK4CaloJet80Eta2p4_DeepCSV0p4_v',
   'HLT_HIPuAK4CaloJet100Eta2p4_DeepCSV0p4_v',
   'HLT_HIPuAK4CaloJet60Eta2p4_CSVv2WP0p75_v',
   'HLT_HIPuAK4CaloJet80Eta2p4_CSVv2WP0p75_v',
   'HLT_HIPuAK4CaloJet100Eta2p4_CSVv2WP0p75_v',
   'HLT_HICsAK4PFJet60Eta1p5_v',
   'HLT_HICsAK4PFJet80Eta1p5_v',
   'HLT_HICsAK4PFJet100Eta1p5_v',
   'HLT_HICsAK4PFJet120Eta1p5_v'
   )

trigger_list_mc = trigger_list_data.__add__([
   ])
