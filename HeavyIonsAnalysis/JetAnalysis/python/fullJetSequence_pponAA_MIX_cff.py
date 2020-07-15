import FWCore.ParameterSet.Config as cms

from HeavyIonsAnalysis.JetAnalysis.rerecoGen_cff import *
from HeavyIonsAnalysis.JetAnalysis.rerecoRho_cff import *
from HeavyIonsAnalysis.JetAnalysis.rerecoJets_cff import *
from HeavyIonsAnalysis.JetAnalysis.rerecoTracks_cff import *

from HeavyIonsAnalysis.JetAnalysis.jets.akPu3CaloJetSequence_pponPbPb_mc_cff import *
from HeavyIonsAnalysis.JetAnalysis.jets.ak3PFJetSequence_pponPbPb_mc_cff import *
from HeavyIonsAnalysis.JetAnalysis.jets.akPu3PFJetSequence_pponPbPb_mc_cff import *
from HeavyIonsAnalysis.JetAnalysis.jets.akCs3PFJetSequence_pponPbPb_mc_cff import *
from HeavyIonsAnalysis.JetAnalysis.jets.akFlowPuCs3PFJetSequence_pponPbPb_mc_cff import *

from HeavyIonsAnalysis.JetAnalysis.jets.akPu4CaloJetSequence_pponPbPb_mc_cff import *
from HeavyIonsAnalysis.JetAnalysis.jets.ak4PFJetSequence_pponPbPb_mc_cff import *
from HeavyIonsAnalysis.JetAnalysis.jets.akPu4PFJetSequence_pponPbPb_mc_cff import *
from HeavyIonsAnalysis.JetAnalysis.jets.akCs4PFJetSequence_pponPbPb_mc_cff import *
from HeavyIonsAnalysis.JetAnalysis.jets.akFlowPuCs4PFJetSequence_pponPbPb_mc_cff import *

from RecoJets.JetProducers.muonJetSelector_cff import *

genSignalSequence = cms.Sequence(
    genParticlesForJets +

    hiSignalGenParticles +
    genParticlesForJetsSignal +

    #put this back for the analysis and SFs! not for b-tagging
    #ak3HiGenJets +
    ak4HiGenJets +

    myPartons +
    signalPartons +

    #put this back for the analysis and SFs! not for b-tagging
    #ak3HiSignalGenJets +
    ak4HiSignalGenJets +

    #put this back for the analysis and SFs! not for b-tagging
    #ak3HiGenNjettiness +
    ak4HiGenNjettiness
)

genCleanedSequence = cms.Sequence(
    genParticlesForJets +
    #put this back for the analysis and SFs! not for b-tagging
    #ak3HiGenJets +
    ak4HiGenJets +

    myPartons +
    cleanedPartons +

    #put this back for the analysis and SFs! not for b-tagging
    #ak3HiCleanedGenJets +
    ak4HiCleanedGenJets
)

jetSequence = cms.Sequence(
    rhoSequence +

    highPurityTracks +

    #akPu3CaloJets +

    #put this back for the analysis and SFs
    #ak3PFJets +

    #akPu3PFJets +
    #akCs3PFJets +

    #put this back for the analysis and SFs! not for b-tagging
    #akFlowPuCs3PFJets +

    #akPu4CaloJets +
    ak4PFJets +
    ak4PFJetsWithMuon +
    #akPu4PFJets +
    #akCs4PFJets +
    akFlowPuCs4PFJets +


    #akPu3CaloJetSequence +

    #put this back for the analysis and SFs
    #ak3PFJetSequence +

    #akPu3PFJetSequence +
    #akCs3PFJetSequence +

    #put this back for the analysis and SFs! not for b-tagging
    #akFlowPuCs3PFJetSequence +

    #akPu4CaloJetSequence +
    ak4PFJetSequence +
    #akPu4PFJetSequence +
    #akCs4PFJetSequence +
    akFlowPuCs4PFJetSequence
)
