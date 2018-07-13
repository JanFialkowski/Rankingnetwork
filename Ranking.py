#!/usr/bin/python2.7
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 14 15:07:17 2018

@author: kingofpi
"""
import numpy as np
from scipy.stats import rankdata
import matplotlib.pyplot as plt
import graph_tool.all as gt
import time
import pickle

class Node:
	counter = 0
	def __init__(self,t=0):
		self.Score = 0.
		self.Rank = Node.counter +1.
		self.ID = Node.counter
		Node.counter += 1
		self.Age = 0.
		self.Trajectory = [self.Rank for i in xrange(t)]
		self.ScoreTrajectory = [0 for i in xrange(t)]
	def __str__(self):
		if len(self.ScoreTrajectory) == 1:
			Points = self.ScoreTrajectory[0]
		elif len(self.ScoreTrajectory) > 1:
			Points = self.ScoreTrajectory[-1]
		return "Score: %g, Rank: %g, Age: %g Links Last Step: %g" %(self.Score, self.Rank, self.Age, Points)
	def CalcScore(self, e = 1.):
		#this function calculates the score of a node 
		self.Score = 0.0
		for i in xrange(int(self.Age)):
			self.Score += (self.ScoreTrajectory[-(i+1)] - (self.Age))/(i+1)**e
		#self.Score -= self.Age
		
def MakeAdjacency(LinkList, Nodes, t0, t1, InitialNodes, sortit=False, maximum = False):
	NumberofNodes = InitialNodes+t1 -1
	if maximum and InitialNodes+t0>=maximum:
		NumberofNodes = maximum + t1-t0-1 #every step adds a node, -1 because t1 is exclusive
	AMatrix = [[0 for i in xrange(NumberofNodes)]for j in xrange(NumberofNodes)]
	if sortit == True:
		Nodes = Nodes[InitialNodes+t1-1-NumberofNodes : InitialNodes+t1] #no -1, because the splice is already exclusive
		# Dictionary: tell every node it's rank.
		Scores = []
		for Node in Nodes:
			Score=0
			for t in xrange(t0,t1):
				Score+=Node.ScoreTrajectory[t]
			Scores.append(Score)
		Ranks = len(Scores) - rankdata(Scores, method="ordinal")
		RankDic = {Name: Rank for (Name,Rank) in zip([i for i in xrange(InitialNodes+t1-1-NumberofNodes, InitialNodes+t1)],Ranks.astype("int",copy=False))}
		for Link in LinkList:
			if t0<=Link[0]<t1:
				Firstlink = Link[1]#-(InitialNodes+t1-NumberofNodes)
				Secondlink = Link[2]#-(InitialNodes+t1-NumberofNodes)
				#print Firstlink, Secondlink
				AMatrix[RankDic[Firstlink]][RankDic[Secondlink]]+=1
				AMatrix[RankDic[Secondlink]][RankDic[Firstlink]]+=1
	else:
		for Link in LinkList:
			if t0<=Link[0]<t1:
				Firstlink = Link[1]-(InitialNodes+t1-NumberofNodes)
				Secondlink = Link[2]-(InitialNodes+t1-NumberofNodes)
				#print Firstlink, Secondlink
				AMatrix[Firstlink][Secondlink]+=1
				AMatrix[Secondlink][Firstlink]+=1
	return AMatrix

def UpdateMatrix(Nodes, Matrix, a = 1.1, b = 2.6):
	#temporary conversion to an array to make later normalizing easier
	ProbM = np.array(Matrix)
	#iterating over the array and calculating the corresponding weights
	Iter = np.nditer(ProbM, flags=["multi_index"], op_flags=["writeonly"])
	while not Iter.finished:
		i = Iter.multi_index[0]
		j = Iter.multi_index[1]
		#print type(Nodes[i].Rank)
		Iter[0] = abs(Nodes[i].Rank-Nodes[j].Rank)**a/(Nodes[i].Rank+Nodes[j].Rank)**b# - (Nodes[i].Age+Nodes[j].Age)**0.8
		if Iter[0] < 0:
			Iter[0] = 0
		Iter.iternext()
	#ProbM **= 0.4
	#normalizing with numpys build-in functions
	if ProbM.sum()!=0:
		ProbM = np.cumsum(ProbM)
		ProbM /= ProbM[-1]
		ProbM = ProbM.reshape((len(Nodes),len(Nodes)))
	#plt.imshow(ProbM, cmap = "binary")
	plt.show
	return ProbM.tolist()

def RollingLinks(ProbM, t, L=20):
	#roll the L links by projecting a uniform distribution onto the given Matrix
	ContactList=[]
	Sum = ProbM[-1][-1]
	while L!=0:
		L-=1
		i=0
		j=0
		if Sum==0:
			while i==j:
				i=np.random.randint(len(ProbM))
				j=np.random.randint(len(ProbM))
		else:
			#roll the random number and check which link is realised by walking through the diagonal of the matrix first.
			Chance=np.random.random_sample()
			while ProbM[i][j]<Chance:
				if i < len(ProbM)-1 and j < len(ProbM[i]):
					if ProbM[i+1][j] < Chance:
						i+=1
				if j == len(ProbM[i])-1:
					j=0
					i+=1
				else:
					j+=1
		ContactList.append([t,i,j])
	return ContactList
	
def Update(Nodes):
	#Update the ranks of the nodes and append to their trajectories
	for Thing in Nodes:
		"""
		Thing.Score = 0.0
		for index, score in enumerate(Thing.ScoreTrajectory):
			length = len(Thing.ScoreTrajectory)
			Thing.Score+=float(score)*((length-index)**-1)
		Thing.Score -= Thing.Age
		"""
		Thing.CalcScore()
	Scores = [i.Score for i in Nodes]
	Ranks = len(Scores) - rankdata(Scores, method="ordinal")+1.0
	for Node in Nodes:
		Node.Rank = Ranks[Nodes.index(Node)].item()
		Node.ScoreTrajectory.append(0)
		Node.Trajectory.append(Node.Rank)
		Node.Age+=1
	return Nodes
	
def FindNode(Nodes):
	#Find the node to be deleted, currently: lowest Rank
	Rankmin = 1
	for i, Point in enumerate(Nodes):
		if Point.Rank > Rankmin:
			Rankmin = Point.Rank
			index = i
	return index
	
def Simulation(initial=5, timesteps=350, maximum=275):
	Nodes = [Node(0) for i in xrange(initial-1)]
	ProbM = [[0. for i in Nodes]for i in Nodes] #Vielleicht ndarray von Anfang an?
	LinkList = []
	DelNodes = []
	NodeDic = {}
	#LinkingTimes = []
	#UpdateTimes = []
	#MatrixTimes = []
	for t in xrange(timesteps):
		print "Fortschritt: %g" %(float(t+1)/timesteps*100)
		
		#add a new node and increase size of ProbM by 1x1
		#also adds the last starting node for t=0
		if len(ProbM) < maximum:
			for E in ProbM:
				E.append(0.)
			ProbM.append([0. for i in xrange(len(Nodes)+1)])
		Nodes.append(Node(t))

		#update the Nodes, i.e. Ranks
		Nodes = Update(Nodes)
		
		#Node deletion if necessary
		while len(Nodes) > maximum:
			Index = FindNode(Nodes)
			DelNodes.append(Nodes[Index])
			del Nodes[Index]
		
		#calculate linking-probability matrix
		t1=time.clock()
		ProbM = UpdateMatrix(Nodes, ProbM)
		
		#roll the links according to the probability matrix
		t1=time.clock()
		AddList = RollingLinks(ProbM,t,15*len(Nodes))
		for L in AddList:
			Nodes[L[1]].ScoreTrajectory[-1]+=1
			Nodes[L[2]].ScoreTrajectory[-1]+=1
			L[1]=Nodes[L[1]].ID
			L[2]=Nodes[L[2]].ID
			LinkList.append(L)
		
		#reformat deleted Nodes for later use
	for Point in DelNodes:
		Zeroes = [0 for i in xrange(timesteps + 1 - len(Point.ScoreTrajectory))]
		Point.ScoreTrajectory.extend(Zeroes)
	Nodes = DelNodes + Nodes
	#populate the Dictionary and rename the links in the list so dead nodes are properly targeted
	for i, Point in enumerate(Nodes):
		NodeDic[Point.ID]=i
	for Link in LinkList:
		Link[1] = NodeDic[Link[1]]
		Link[2] = NodeDic[Link[2]]
	return LinkList, Nodes
	
if __name__=="__main__":
	LinkList, Nodes = Simulation()
	"""
	Dupes = [0 for i in Nodes[-1].Trajectory]
	for t in xrange(len(Nodes[-1].Trajectory)):
		DifferentRanks = []
		for Node in Nodes:
			if Node.Trajectory[t] in DifferentRanks:
				Dupes[t]+=1
			else:
				DifferentRanks.append(Node.Trajectory[t])
	plt.plot(Dupes, label="number of duplicate ranks every timestep")
	plt.xlabel("timestep")
	plt.ylabel("number of duplicate scores")
	plt.legend()
	plt.show()
	"""
	RankoneTimes = []
	TimetoOnes = []
	plt.show()
	#plt.imshow(np.array(MakeAdjacency(LinkList, Nodes, 95, 100, 5,sortit=False, maximum=50)), cmap = "binary", interpolation = "none")
	plt.show()
	plt.show()
	for Thing in Nodes:
		if 1 in Thing.Trajectory:
			plt.plot(Thing.Trajectory, label = Thing.ID)
			RankoneTimes.append(Thing.Trajectory.count(1))
			TimetoOnes.append(Thing.Trajectory.index(1)-(len(Thing.Trajectory)-Thing.Age-1))
	plt.xlabel("Time")
	#plt.ylim(0,20)
	plt.ylabel("Rank")
	plt.legend()
	plt.show()
	for Thing in Nodes:
		plt.plot(Thing.ScoreTrajectory)
	plt.show()
	plt.hist(RankoneTimes, label = "Time spent at Rank one")
	plt.ylabel("Time spent at Rank one")
	plt.show()
	plt.hist(TimetoOnes, label = "Time it takes to reach Rank one")
	plt.ylabel("Time it takes to reach Rank one")
	plt.show()
	
	#plt.imshow(np.array(MakeAdjacency(LinkList, Nodes, 98, 100, 5,sortit=False, maximum=False)), cmap = "binary", interpolation = "none")
	plt.show()
	
	with open("./Simulatednetworks/LinkList","wb") as fp:
		pickle.dump(LinkList,fp)
	with open("./Simulatednetworks/Nodes","wb") as fp:
		pickle.dump(Nodes,fp)
	for i in xrange(52):
		Graph=gt.Graph(directed=False)
		EdgeList = [Edge[1:] for Edge in LinkList if 295+i <= Edge[0] < 295+i+1]
		Graph.add_edge_list(EdgeList)
		#deg = Graph.degree_property_map("out")
		#deg.a = 4*(np.sqrt(deg.a)*0.5+0.4)+10
		#pos = gt.arf_layout(Graph)
		#gt.graph_draw(Graph, vertex_text=Graph.vertex_index, output = "99to100_15Links_11and26.png", vertex_size = deg, output_size = (1000,1000), vertex_text_position = -0.5, pos=pos)
		Graph.save("./Simulatednetworks/SimulatedGraphWeek%d.graphml"%(i))

	#with open("./TestingthepicklingList.txt", "wb") as fp:   #Pickling
	#	pickle.dump(LinkList, fp)
	#with open("./TestingthepicklingNodes.txt", "wb") as fp:
		#pickle.dump(Nodes, fp)
