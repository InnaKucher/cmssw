import FWCore.ParameterSet.Config as cms

from HeavyIonsAnalysis.VectorBosonAnalysis.tupelSequence_PbPb_cff import *

from PhysicsTools.PatAlgos.mcMatchLayer0.photonMatch_cfi import photonMatch
photonMatch.src = cms.InputTag("photons")
patPhotonSequence.remove([patPhotons])
patPhotonSequence.append([photonMatch, patPhotons])

from PhysicsTools.PatAlgos.mcMatchLayer0.electronMatch_cfi import electronMatch
electronMatch.src = cms.InputTag("gedGsfElectronsTmp")
patElectronSequence.remove([patElectrons])
patElectronSequence.append([electronMatch, patElectrons])
