import graph_tool.all as gt
import matplotlib.pyplot as plt
import numpy as np
import glob
import scipy.stats as sp

filenames = sorted(glob.glob("./Realnetworks/tags*_2015.gml"))
Graphs = [gt.load_graph(File) for File in filenames]

#Codeblock fuer die Summe ueber die Gewichte eines Knoten
RunningI = 0
LabeltoI = {}
for Graph in Graphs:
	for label in set(Graph.vp.label[vertex] for vertex in Graph.vertices())-set(LabeltoI.keys()):
		LabeltoI[label] = RunningI
		RunningI += 1
Scores = [[] for i in LabeltoI.keys()]
counting = 0
for Graph in Graphs:
	Matrix = gt.adjacency(Graph, weight = Graph.ep.weight)
	counting += 1
	for i in xrange(len(Graph.get_vertices())):
		Scores[LabeltoI[Graph.vp.label[i]]].append(Matrix[i].sum()/2)
	for Score in Scores: #Nullkorrektur, wenn Knoten im aktuellen Graphen nicht existiert wird Score als 0 hinzugefuegt
		if len(Score)<counting:
			Score.append(0)
print Scores

#Ranking the nodes by their points, without age
Ranks = [[] for i in LabeltoI.keys()]
for i in xrange(len(Scores[0])):
	Rankpoints = [ sl[i] for sl in Scores]
	Rankings = len(Rankpoints) - sp.rankdata(Rankpoints, method = "ordinal").astype("float") + 1
	for e in xrange(len(Ranks)):
		Ranks[e].append(Rankings[e])

Firstrankings = np.array([sl[0] for sl in Ranks])
Firstscores = np.array([sl[0] for sl in Scores])
actualranks = np.count_nonzero(Firstscores)
print actualranks
Firstrankings /= actualranks
Firstscores *= actualranks
Firstscores /= Firstscores.sum()
print Firstrankings
print Firstscores
plt.scatter(Firstrankings, Firstscores)

plt.show()
"""
#Code-snippet to calcute graph wide average weight per node
Graphweightsum = []
for i in xrange(len(Scores[0])):
	Graphweightsum.append(0)
	for Score in Scores:
		Graphweightsum[i] += Score[i]/2 #Gradsumme = 2*Weightsumme
	Graphweightsum[i] /= len(Graphs[i].get_vertices())
plt.plot(Graphweightsum, label = r"$\frac{\sum_{i,j}^N w_{ij}}{N}$")
average = 0
for entry in Graphweightsum:
	average += entry
average /= len(Graphweightsum)
plt.plot([0,len(Graphweightsum)-1],[average,average], label = "Mean over time")
plt.xlabel("time")
plt.ylabel("average weight")
plt.legend()
plt.show()
"""
"""
Code-snippet to plot the scores over time
for Score in Scores:
	plt.plot(Score, label = LabeltoI.keys()[LabeltoI.values().index(Scores.index(Score))])
plt.xlabel("Week")
plt.ylabel("Degree of the Node")
#plt.legend()
plt.show()
"""

"""
#Codeblock fuer die Assortivity
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
