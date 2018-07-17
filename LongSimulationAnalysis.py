import pickle
import numpy as np
import scipy as sp
from Ranking import *

"""
with open("./Simulatednetworks/LongLinkList7k", "rb") as fp:
	LinkList = pickle.load(fp)
EdgeList=[Edge[1:] for Edge in LinkList if Edge[0] == 145]
Graph=gt.Graph(directed=False)
Graph.add_edge_list(EdgeList)
Graph.save("SampleSimulation.graphml")
"""
Graph=gt.load_graph("SampleSimulation.graphml")
gt.remove_parallel_edges(Graph)
Degrees = Graph.get_out_degrees(Graph.get_vertices())
Ranks = len(Degrees) - sp.stats.rankdata(Degrees, method = "ordinal")
Index = Graph.new_vertex_property("int")
for v in Graph.vertices():
	Index[v]=Ranks[Graph.vertex_index[v]]
plt.imshow(gt.adjacency(Graph,index=Index).todense(), cmap = "binary")
"""
RankoneTimes = []
TimetoOnes = []
plt.show()
plt.show()
plt.show()
for Thing in Nodes:
	if 1 in Thing.Trajectory:
		#plt.plot(Thing.Trajectory, label = Thing.ID)
		RankoneTimes.append(Thing.Trajectory.count(1))
		TimetoOnes.append(Thing.Trajectory.index(1)-(len(Thing.Trajectory)-Thing.Age-1))
#plt.xlabel("Time")
#plt.ylim(0,150)
#plt.ylabel("Rank")
#plt.legend()
#plt.show()
#for Thing in Nodes:
	#plt.plot(Thing.ScoreTrajectory)
#plt.xlabel("Time")
#plt.ylabel("Number of links participated in")
#plt.xlim(5400,5500)
"""
"""
plt.show()
plt.hist(RankoneTimes, np.arange(max(RankoneTimes)+1), label = "Time spent at Rank one")
plt.xlabel("Time spent at Rank one")
plt.ylabel("Occurences")
plt.show()
plt.hist(TimetoOnes, np.arange(max(TimetoOnes)+1), label = "Time it takes to reach Rank one")
plt.xlabel("Time it takes to reach Rank one")
plt.ylabel("Occurences")
plt.show()
"""
#print sp.stats.describe(RankoneTimes)
#print sp.stats.describe(TimetoOnes)
#print len(TimetoOnes)/float(len(Nodes))
#print len(RankoneTimes)/float(len(Nodes))
#plt.imshow(np.array(MakeAdjacency(LinkList, Nodes, 98, 100, 5,sortit=False, maximum=False)), cmap = "binary", interpolation = "none")
plt.show()
