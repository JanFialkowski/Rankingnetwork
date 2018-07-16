import graph_tool.all as gt
import matplotlib.pyplot as plt
import numpy as np
import glob
import scipy.stats as sp
import scipy.optimize as optimize
import NodeProbs as NoP
import networkx as nx

filenames = sorted(glob.glob("./Simulatednetworks/SimulatedGraphWeek*.graphml"))
FakeGraphs = [gt.load_graph(File) for File in filenames]
filenames = sorted(glob.glob("./Realnetworks/tags*_2015.gml"))
Graphs = [gt.load_graph(File) for File in filenames]
print len(Graphs)
#"""
xGraphs = [nx.Graph() for i in xrange(len(Graphs))]
xFakeGraphs = [nx.Graph() for i in xrange(len(FakeGraphs))]
for i in xrange(len(Graphs)):
	gt.remove_self_loops(Graphs[i])
	for e in Graphs[i].edges():
		xGraphs[i].add_edge(*e)
for i in xrange(len(FakeGraphs)):
	gt.remove_parallel_edges(FakeGraphs[i])
	for e in FakeGraphs[i].edges():
		xFakeGraphs[i].add_edge(*e)
#print nx.rich_club_coefficient(xGraphs[0], normalized = False)
RealClubs = []
print len(xGraphs)
for Graph in xGraphs:
	Coefficients = nx.rich_club_coefficient(Graph, normalized = False)
	print len(Coefficients)
	Dummy = np.zeros((len(Coefficients),))
	for i in xrange(len(Dummy)):
		Dummy[i] = Coefficients[i]
	RealClubs.append(Dummy)
FakeClubs = []
for Graph in xFakeGraphs:
	Coefficients = nx.rich_club_coefficient(Graph, normalized = False)
	print len(Coefficients)
	Dummy = np.zeros((len(Coefficients),))
	for i in xrange(len(Dummy)):
		Dummy[i] = Coefficients[i]
	FakeClubs.append(Dummy)
Lines = []
f,ax = plt.subplots()
for Values in RealClubs:
	Lines.append(ax.plot(np.arange(Values.size, dtype = "float")/Values.size,Values, c = "xkcd:black"))
for Values in FakeClubs:
	Lines.append(ax.plot(np.arange(Values.size, dtype = "float")/Values.size,Values, c = "blue"))
ax.legend((Lines[0][0],Lines[-1][0]),["Empirical networks","Simulated networks"])
plt.xlabel(r"$k/k_{max-1}$")
plt.ylabel("rich club coefficient")
#plt.legend()
plt.show()
#"""
