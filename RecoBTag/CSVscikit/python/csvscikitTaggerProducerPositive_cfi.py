import FWCore.ParameterSet.Config as cms
import RecoBTag.SecondaryVertex.positiveCombinedSecondaryVertexV2Computer_cfi as sl_cfg
from RecoBTag.CSVscikit.training_settings import csvscikit_vpset
from RecoBTag.CSVscikit.helpers import get_vars

weightfilename = 'RecoBTag/PerformanceMeasurements/test/TMVA_weights.xml'

#charmTagsComputerCvsL = cms.ESProducer(
CSVscikitPosTags = cms.ESProducer(
   'CSVscikitESProducer',
   slComputerCfg = cms.PSet(
      **sl_cfg.positiveCombinedSecondaryVertexV2Computer.parameters_()
      ),
   weightFile = cms.FileInPath(weightfilename),
   variables = csvscikit_vpset,

   computer = cms.ESInputTag('justastupiddummyname'),
   tagInfos = cms.VInputTag(
      cms.InputTag('pfImpactParameterTagInfos'),
      cms.InputTag('pfInclusiveSecondaryVertexFinderTagInfos'),
      ),
   mvaName = cms.string('BDT'),
   useCondDB = cms.bool(False),
   gbrForestLabel = cms.string(''),
   useGBRForest = cms.bool(True),
   useAdaBoost = cms.bool(False)
   )
