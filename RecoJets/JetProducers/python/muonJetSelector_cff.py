
import FWCore.ParameterSet.Config as cms

ak4PFJetsWithMuon = cms.EDFilter("PFJetXSelector",
                                 src = cms.InputTag("ak4PFJets"),
                                 cut = cms.string("pt > 0.0 && abs(rapidity()) < 3.0")
)
