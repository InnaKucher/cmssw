import FWCore.ParameterSet.Config as cms

hltobject = cms.EDAnalyzer("TriggerObjectAnalyzer",
   processName = cms.string("HLT"),
   treeName = cms.string("MuonTriggers"),
   triggerResults = cms.InputTag("TriggerResults","","HLT"),
   triggerEvent = cms.InputTag("hltTriggerSummaryAOD","","HLT")
)

trigger_list_data = cms.vstring(
   'HLT_HIL3Mu3_NHitQ10_v1',
   'HLT_HIL3Mu5_NHitQ10_v1'
   )

trigger_list_mc = trigger_list_data.__add__([
   ])
