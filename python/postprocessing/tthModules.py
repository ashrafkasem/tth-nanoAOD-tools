from tthAnalysis.NanoAODTools.postprocessing.modules.genParticleProducer import genLepton, genAll
from tthAnalysis.NanoAODTools.postprocessing.modules.lepJetVarProducer import lepJetVar
from tthAnalysis.NanoAODTools.postprocessing.modules.genHiggsDecayModeProducer import genHiggsDecayMode
from tthAnalysis.NanoAODTools.postprocessing.modules.missingProducer import missing # NB! PLACEHOLDER FOR THE MISSING BRANCHES!
from PhysicsTools.NanoAODTools.postprocessing.modules.btv.btagSFProducer import btagSF
from PhysicsTools.NanoAODTools.postprocessing.examples.puWeightProducer import puWeight
from PhysicsTools.NanoAODTools.postprocessing.modules.jme.jecUncertainties import jecUncert_cpp
try:
  from PhysicsTools.NanoAODTools.postprocessing.modules.jme.jetmetUncertainties import jetmetUncertainties
except ImportError:
  print("Module PhysicsTools.NanoAODTools.postprocessing.modules.jme.jetmetUncertainties not available")
