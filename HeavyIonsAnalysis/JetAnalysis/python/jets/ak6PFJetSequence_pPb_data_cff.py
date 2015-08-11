

import FWCore.ParameterSet.Config as cms
from HeavyIonsAnalysis.JetAnalysis.patHeavyIonSequences_cff import patJetGenJetMatch, patJetPartonMatch, patJetCorrFactors, patJets
from HeavyIonsAnalysis.JetAnalysis.inclusiveJetAnalyzer_cff import *

ak6PFmatch = patJetGenJetMatch.clone(
    src = cms.InputTag("ak6PFJets"),
    matched = cms.InputTag("ak6HiGenJets"),
    maxDeltaR = 0.6
    )

ak6PFparton = patJetPartonMatch.clone(src = cms.InputTag("ak6PFJets"),
                                                        matched = cms.InputTag("hiGenParticles")
                                                        )

ak6PFcorr = patJetCorrFactors.clone(
    useNPV = False,
#    primaryVertices = cms.InputTag("hiSelectedVertex"),
    levels   = cms.vstring('L2Relative','L3Absolute'),
    src = cms.InputTag("ak6PFJets"),
    payload = "AK6PF_generalTracks"
    )

ak6PFpatJets = patJets.clone(jetSource = cms.InputTag("ak6PFJets"),
                                               jetCorrFactorsSource = cms.VInputTag(cms.InputTag("ak6PFcorr")),
                                               genJetMatch = cms.InputTag("ak6PFmatch"),
                                               genPartonMatch = cms.InputTag("ak6PFparton"),
                                               jetIDMap = cms.InputTag("ak6PFJetID"),
                                               addBTagInfo         = False,
                                               addTagInfos         = False,
                                               addDiscriminators   = False,
                                               addAssociatedTracks = False,
                                               addJetCharge        = False,
                                               addJetID            = False,
                                               getJetMCFlavour     = False,
                                               addGenPartonMatch   = False,
                                               addGenJetMatch      = False,
                                               embedGenJetMatch    = False,
                                               embedGenPartonMatch = False,
                                               # embedCaloTowers     = False,
                                               # embedPFCandidates = False
				            )

ak6PFJetAnalyzer = inclusiveJetAnalyzer.clone(jetTag = cms.InputTag("ak6PFpatJets"),
                                                             genjetTag = 'ak6HiGenJets',
                                                             rParam = 0.6,
                                                             matchJets = cms.untracked.bool(False),
                                                             matchTag = 'patJets',
                                                             pfCandidateLabel = cms.untracked.InputTag('particleFlow'),
                                                             trackTag = cms.InputTag("generalTracks"),
                                                             fillGenJets = False,
                                                             isMC = False,
                                                             genParticles = cms.untracked.InputTag("hiGenParticles"),
							     eventInfoTag = cms.InputTag("generator")
                                                             )

ak6PFJetSequence_mc = cms.Sequence(
						  ak6PFmatch
                                                  *
                                                  ak6PFparton
                                                  *
                                                  ak6PFcorr
                                                  *
                                                  ak6PFpatJets
                                                  *
                                                  ak6PFJetAnalyzer
                                                  )

ak6PFJetSequence_data = cms.Sequence(ak6PFcorr
                                                    *
                                                    ak6PFpatJets
                                                    *
                                                    ak6PFJetAnalyzer
                                                    )

ak6PFJetSequence_jec = cms.Sequence(ak6PFJetSequence_mc)
ak6PFJetSequence_mix = cms.Sequence(ak6PFJetSequence_mc)

ak6PFJetSequence = cms.Sequence(ak6PFJetSequence_data)
