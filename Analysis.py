import graph_tool.all as gt
import matplotlib.pyplot as plt
import numpy as np
import glob
import scipy.stats as sp

filenames = sorted(glob.glob("./Realnetworks/tags*_2015.gml"))
Graphs = [gt.load_graph(File) for File in filenames]
RunningI = 0
LabeltoI = {}
for Graph in Graphs:
	for label in set(Graph.vp.label[vertex] for vertex in Graph.vertices())-set(LabeltoI.keys()):
		LabeltoI[label] = RunningI
		RunningI += 1
Scores = [[] for i in LabeltoI.keys()]

for Graph in Graphs:
	Matrix = gt.adjacency(Graph, weight = Graph.ep.weight)
	for i in xrange(len(Graph.get_vertices())):
		Scores[LabeltoI[Graph.vp.label[i]]].append(Matrix[i].sum()/2.)
print Scores
"""
EperV = [gt.scalar_assortativity(Graph, "total") for Graph in Graphs]
Values = [Thing[0] for Thing in EperV]
plt.plot(Values)
plt.plot([1,52],[-0.12,-0.12])
plt.xlabel("Week")
plt.ylabel("Assortativity r")
plt.show()
print sp.describe(Values)
plt.hist(Values)
plt.show()
"""
"""
Summe = 0
for value in Values:
	Summe += value
Summe /= len(EperV)
print Summe
"""
