

from ROOT import TFile, TTree

filein = TFile("tnpZ_withNVtxWeights.root","READ")
tree = filein.Get("tpTree/fitter_tree");

tree
skipEvery= 5
skipcount=0
nEntries = tree.GetEntries

for i in rang(0,nEntries):


