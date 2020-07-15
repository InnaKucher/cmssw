import FWCore.ParameterSet.Config as cms

pfCSVscikitJetPosTags  = cms.EDProducer(
#pfCombinedCvsLJetTags  = cms.EDProducer(
   "JetTagProducer",
   #jetTagComputer = cms.string('charmTagsComputerCvsL'),
   jetTagComputer = cms.string('CSVscikitPosTags'),
   tagInfos = cms.VInputTag(
      cms.InputTag('pfImpactParameterTagInfos'),
      #cms.InputTag('pfInclusiveSecondaryVertexFinderCvsLTagInfos'),
      cms.InputTag('pfInclusiveSecondaryVertexFinderTagInfos'),
      #cms.InputTag('softPFMuonsTagInfos'),
      #cms.InputTag('softPFElectronsTagInfos'),
      )
)

#pfCSVscikitDummy = pfCSVscikitJetTags.clone(
##pfCombinedCvsBJetTags = pfCombinedCvsLJetTags.clone(
#   #jetTagComputer = cms.string('charmTagsComputerCvsB')
#   jetTagComputer = cms.string('CSVscikitTagsdummy')
#   )
