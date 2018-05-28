import graph_tool.all as gt
import matplotlib.pyplot as plt
import numpy as np
import glob
import scipy.stats as sp

filenames = sorted(glob.glob("./Realnetworks/tags*_2015.gml"))
Graphs = [gt.load_graph(File) for File in filenames]

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
Summe = 0
for value in Values:
	Summe += value
Summe /= len(EperV)
print Summe
"""
