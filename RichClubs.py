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
filenames = sorted(glob.glob("./RealNetworks/tags*_2015.gml"))
Graphs = [gt.load_graph(File) for File in filenames]
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
print nx.rich_club_coefficient(xGraphs[0], normalized = False)