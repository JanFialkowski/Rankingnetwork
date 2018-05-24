import graph_tool.all as gt
import matplotlib.pyplot as plt
import numpy as np
import glob

filenames = sorted(glob.glob("./Realnetworks/tags*_2015.gml"))
Graphs = [gt.load_graph(File) for File in filenames]

plt.plot([len(Graph.get_vertices()) for Graph in Graphs])
plt.show()
