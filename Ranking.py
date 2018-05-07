#!/usr/bin/python2.7
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 14 15:07:17 2018

@author: kingofpi
"""
import numpy as np
from scipy.stats import rankdata
import matplotlib.pyplot as plt
import pprint
#import graph_tool.all as gt
import time

class Node:
	counter = 0.0
	def __init__(self,t=0):
		self.Score = 0.
		self.Rank = Node.counter +1.
		Node.counter += 1.
		self.Age = 0.
		self.Trajectory = [self.Rank for i in xrange(t+1)]
		self.ScoreTrajectory = [0 for i in xrange(t+1)]
	def __str__(self):
		Points = 100
		if len(self.ScoreTrajectory) == 1:
			Points = self.ScoreTrajectory[0]
		elif len(self.ScoreTrajectory) > 1:
			Points = self.ScoreTrajectory[-1]
		return "Score: %g, Rank: %g, Age: %g Links Last Step: %g" %(self.Score, self.Rank, self.Age, Points)
		
def MakeAdjacency(LinkList, t0, t1,InitialNodes):
	NumberofNodes = InitialNodes+t1
	AMatrix = [[0 for i in xrange(NumberofNodes)]for j in xrange(NumberofNodes)]
	for Link in LinkList:
		if t0<=Link[0]<=t1:
			AMatrix[Link[1]][Link[2]]+=1
			AMatrix[Link[2]][Link[1]]+=1
	return AMatrix

def UpdateMatrix(Nodes, Matrix):
	ProbM = np.array(Matrix)
	Iter = np.nditer(ProbM, flags=["multi_index"], op_flags=["writeonly"])
	while not Iter.finished:
		i = Iter.multi_index[0]
		j = Iter.multi_index[1]
		#print type(Nodes[i].Rank)
		Iter[0] = abs(Nodes[i].Rank-Nodes[j].Rank)/(Nodes[i].Rank+Nodes[j].Rank)**1.0# - (Nodes[i].Age+Nodes[j].Age)**0.8
		if Iter[0] < 0:
			Iter[0] = 0
		Iter.iternext()
	#ProbM **= 0.4
	if ProbM.sum()!=0:
		ProbM = np.cumsum(ProbM)
		ProbM /= ProbM[-1]
		ProbM = ProbM.reshape((len(Nodes),len(Nodes)))
	plt.imshow(ProbM, cmap = "binary")
	plt.show
	return ProbM.tolist()

def RollingLinks(ProbM,t, L=20):
	ContactList=[]
	Sum = sum([sum(k) for k in ProbM])
	while L!=0:
		L-=1
		i=0
		j=0
		if Sum==0:
			while i==j:
				i=np.random.randint(len(ProbM))
				j=np.random.randint(len(ProbM))
		else:
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
	for Thing in Nodes:
		for index, score in enumerate(Thing.ScoreTrajectory):
			length = len(Thing.ScoreTrajectory)
			Thing.Score+=float(score)*((length-index)**-3)
		Thing.Score -= Thing.Age
	Scores = [i.Score for i in Nodes]
	Ranks = len(set(Scores)) - rankdata(Scores, method="dense")+1.0
	for Node in Nodes:
		Node.Rank = Ranks[Nodes.index(Node)].item()
		#print Node
		Node.ScoreTrajectory.append(0)
		Node.Trajectory.append(Node.Rank)
		Node.Age+=1
	return Nodes
	
def Simulation(initial=2, timesteps=100):
	Nodes = [Node(0) for i in xrange(initial)]
	ProbM = [[0. for i in Nodes]for i in Nodes] #Vielleicht ndarray von Anfang an?
	LinkList = []
	LinkingTimes = []
	UpdateTimes = []
	MatrixTimes = []
	for t in xrange(timesteps):
		
		#Nodes updaten
		t1=time.clock()
		Nodes = Update(Nodes)
		#UpdateTimes.append(time.clock()-t1)
		
		#Matrix berechnen
		t1=time.clock()
		ProbM = UpdateMatrix(Nodes, ProbM)
		#MatrixTimes.append(time.clock()-t1)
		#pprint.pprint(ProbM)
		
		#Links auswürfeln
		print "Fortschritt: %g" %(float(t+1)/timesteps*100)
		t1=time.clock()
		AddList = RollingLinks(ProbM,t,3*len(Nodes))
		#LinkingTimes.append(time.clock()-t1)
		for L in AddList:
			a = L[1]
			b = L[2]
			Nodes[a].ScoreTrajectory[-1]+=1
			Nodes[b].ScoreTrajectory[-1]+=1
		LinkList.extend(AddList)
		
		#neuen Knoten hinzufügen
		for E in ProbM:
			E.append(0.)
		Nodes.append(Node(t+1))
		ProbM.append([0. for i in Nodes])
		
	#plt.show()
	#plt.plot(LinkingTimes, label="Linking")
	#plt.plot(UpdateTimes, label="Updating")
	#plt.plot(MatrixTimes, label="Matrix")
	#plt.legend()
	#plt.show()
	return LinkList, Nodes
	
if __name__=="__main__":
	LinkList, Nodes = Simulation()
	RankoneTimes = []
	TimetoOnes = []
	plt.imshow(MakeAdjacency(LinkList,0,99,2), cmap="binary")
	plt.show()
	for Thing in Nodes:
		if 1 in Thing.Trajectory:
			plt.plot(Thing.Trajectory, label=Nodes.index(Thing))
			RankoneTimes.append(Thing.Trajectory.count(1))
			TimetoOnes.append(Thing.Trajectory.index(1)-(len(Thing.Trajectory)-Thing.Age-1))
		#plt.plot(Thing.Trajectory)
	#plt.plot(Nodes[0].Trajectory)
	#plt.plot(Nodes[50].Trajectory)
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
	#Graph=gt.Graph(directed=False)
	#EdgeList = [Edge[1:] for Edge in LinkList if Edge[0] in [90,91,92,93,94,95,96]]
	#Graph.add_edge_list(EdgeList)
	#Graph.save("Ranking90week.graphml")
