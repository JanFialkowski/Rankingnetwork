import graph_tool.all as gt
import matplotlib.pyplot as plt
import numpy as np
import glob
import scipy.stats as sp
import scipy.optimize as optimize
import NodeProbs as NoP

filenames = sorted(glob.glob("./Realnetworks/tags*_2015.gml"))
Graphs = [gt.load_graph(File) for File in filenames]
filenames = sorted(glob.glob("./Simulatednetworks/SimulatedGraphWeek*.graphml"))
FakeGraphs = [gt.load_graph(File) for File in filenames]
#"""
#Degree-Distributions
for Graph in FakeGraphs:
	gt.remove_parallel_edges(Graph)
bins = np.geomspace(0.01,1, num = 30)
print bins
FakeDegrees = []
for i in xrange(len(FakeGraphs)):
	Dummy = FakeGraphs[i].get_out_degrees(FakeGraphs[i].get_vertices()[25+i:]).astype("float")
	#Dummy /= Dummy.max()
	FakeDegrees.extend(Dummy)
	#splicing to deal with the dead nodes
	#FakeDegrees[i]/=FakeDegrees[i].max()
RealDegrees = []
for i in xrange(len(Graphs)):
	dummy = Graphs[i].get_out_degrees(Graphs[i].get_vertices()).astype("float")
	#dummy /= dummy.max()
	RealDegrees.extend(dummy)
	#RealDegrees[i]/=RealDegrees[i].max()
for i in xrange(len(RealDegrees)):
	RealDegrees[i]/=max(RealDegrees)
for i in xrange(len(FakeDegrees)):
	FakeDegrees[i]/=max(FakeDegrees)
#print FakeDegrees

plt.hist([FakeDegrees, RealDegrees], bins = bins, log = True)
plt.xscale("log")
plt.xlabel(r"$k/k_{max}$")
plt.show()
#"""

"""
#Codeblock fuer die Summe ueber die Gewichte eines Knoten
RunningI = 0
LabeltoI = {} #Dictionary, tells every hashtag-label its index I in my Lists
for Graph in Graphs:
	for label in set(Graph.vp.label[vertex] for vertex in Graph.vertices())-set(LabeltoI.keys()):
		LabeltoI[label] = RunningI
		RunningI += 1
Scores = [[] for i in LabeltoI.keys()]
#Scores contains a scoretrajectory for every hashtag, Labels are identified by the LabeltoI dictionary
#Scores[i][j] Score of the i'th Node at time j
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
"""

"""
histogram = [gt.corr_hist(Graph, "total", "total") for Graph in Graphs]
longest = 0
index = 0
#print histogram[0]
for gram in histogram:
	length = len(gram[0])
	if length>longest:
		longest = len(gram[0])
		index = histogram.index(gram)

grammy = histogram[index]
print len(grammy[0])
print longest
plt.imshow(grammy[0], origin = "lower")
#del histogram[index]
superhist = np.zeros_like(grammy[0])
for hist in histogram:
	superhist[:len(hist[0]),:len(hist[0])] += hist[0]
specialhist = superhist.flatten()
specialhist[specialhist.argmax()]=0
print superhist
superhist = specialhist.reshape(superhist.shape)
plt.imshow(superhist)
plt.colorbar()
plt.show()
"""
"""
#code-snippet for the number of nodes per week
Nodes = np.zeros((len(Graphs),))
for i in xrange(len(Graphs)):
	Nodes[i] = len(Graphs[i].get_vertices())
plt.plot(Nodes,label = "real dataset")
average = float(Nodes.sum())/len(Nodes)
plt.plot([0,len(Nodes)-1],[average,average],label = "mean number of nodes = %.1f"%(average))
plt.xlabel("week")
plt.ylabel("number of nodes")
plt.legend()
plt.show()
"""
"""
#calculate highest number of nodes in Graphs  UNUSED
Maxnodes = 0
for Graph in Graphs:
	Nodes = len(Graph.get_vertices())
	if Nodes > Maxnodes:
		Maxnodes = Nodes
"""

"""
PointsforRank = [[] for i in xrange(len(LabeltoI))] 
#should count the scores every rank gets in the following timestep
#PointsforRank[i][j] Punkte die der i-te Rang zum j+1-ten Schritt gemacht hat

#Ranking the nodes by their points, without age
Ranks = [[] for i in LabeltoI.keys()] #contains the ranktrajectory for every hashtag/label
for i in xrange(len(Scores[0])):
	Rankpoints = [ sl[i] for sl in Scores]
	Rankings = len(Rankpoints) - sp.rankdata(Rankpoints, method = "ordinal").astype("float") + 1
	for e in xrange(len(Ranks)):
		Ranks[e].append(Rankings[e])
"""

"""
#Proof-of-concept 
Firstrankings = np.array([sl[0] for sl in Ranks])
Firstscores = np.array([sl[1] for sl in Scores])
actualranks = np.count_nonzero(Firstscores)
print actualranks
#Firstrankings /= actualranks
#Firstscores *= actualranks
Firstscores /= Firstscores.sum()
#print Firstrankings
#print Firstscores
#plt.scatter(Firstrankings, Firstscores)
#plt.show()
"""

"""
#populating PointsforRank
for i in xrange(len(Scores[0])-1):
	for j in xrange(len(Ranks)):
		PointsforRank[Ranks[j][i].astype("int")-1].append(Scores[j][i+1])
PointsforRank = np.array(PointsforRank)
PointsforRank = PointsforRank.transpose()
for Time in PointsforRank:
	Time /= Time.sum()
print PointsforRank.sum()
PointsforRank = PointsforRank.transpose()
MeanProbs = np.array([sl.sum()/len(sl) for sl in PointsforRank]).astype("float")
print MeanProbs.sum()
Sigma = np.array([((sl-mean)**2).sum()/float(len(sl)) for sl,mean in zip(PointsforRank,MeanProbs)])
Sigma = np.sqrt(Sigma)
XValues = np.array([i+1 for i in xrange(len(MeanProbs))]).astype("float")
#XValues /= len(XValues)
#MeanProbs *= len(XValues)
plt.scatter(XValues, MeanProbs, s = 5, label = "real dataset")
plt.xlabel("Rank i")
plt.ylabel("Average probability to gain a link")
#plt.scatter([i+1 for i in xrange(len(PointsforRank))],[sl[0] for sl in PointsforRank], s = 5)
#plt.show()
#plt.plot(XValues,NoP.BuildProbas(Size=len(XValues),a=1.107,b=2.623))
#plt.show()
def fit(x,a,b):
	y = NoP.BuildProbas(Size=len(XValues),a=a,b=b)
	return y

def fit2(x,a,b):
	return b*x**a
Test = optimize.curve_fit(fit,XValues,MeanProbs)
Test2 = optimize.curve_fit(fit2, XValues, MeanProbs)
plt.plot(XValues,NoP.BuildProbas(Size=len(XValues),a=Test[0][0],b=Test[0][1]), "xkcd:orange", label = "best fit with a = %.1f and b = %.1f"%(Test[0][0], Test[0][1]))
#plt.plot(XValues, XValues**Test2[0][0]*Test2[0][1], "green", label = r"$0.06\cdot x^{-0.65}$")
print Test[0]
print np.sqrt(Test[1])
print Test2
plt.legend()
plt.show()
"""
"""
#Code-snippet to calcute graph wide average weight per node
Graphweightsum = []
for i in xrange(len(Scores[0])):
	Graphweightsum.append(0)
	for Score in Scores:
		Graphweightsum[i] += Score[i]/2 #Gradsumme = 2*Linksumme
	Graphweightsum[i] /= len(Graphs[i].get_vertices())
plt.plot(Graphweightsum, label = "real dataset")
average = 0
for entry in Graphweightsum:
	average += entry
average /= len(Graphweightsum)
plt.plot([0,len(Graphweightsum)-1],[average,average], label = "mean number of links per node over time: %.1f"%(average))
plt.xlabel("week")
plt.ylabel("average number of links per Node")
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
for Graph in FakeGraphs:
	gt.remove_parallel_edges(Graph)
EperV = [gt.scalar_assortativity(Graph, "total") for Graph in FakeGraphs]
Values = [Thing[0] for Thing in EperV]
mean = sp.describe(Values)[2]
print np.sqrt(sp.describe(Values)[3])
plt.plot(Values, label = "empirical dataset")
plt.plot([0,51],[mean,mean], label = "mean assortativity: %.3f"%(mean))
plt.xlabel("week")
plt.ylabel("assortativity r")
plt.legend()
plt.show()
#plt.hist(Values)
plt.show()
"""
"""
Summe = 0
for value in Values:
	Summe += value
Summe /= len(EperV)
print Summe
"""
