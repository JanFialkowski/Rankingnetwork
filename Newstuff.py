import numpy as np
import matplotlib.pyplot as plt

def Weight(r1,r2, a, b):
	return abs(r1-r2)**a/((r1+r2)**b)

Matrix = [[0 for i in xrange(101)] for j in xrange(101)]

for i in xrange(len(Matrix)):
	for j in xrange(len(Matrix[i])):
		Matrix[i][j] = np.log10(Weight(1,100,i/10.,j/10.)/Weight(1,2,i/10.,j/10.))
		#if Matrix[i][j] > 100:
			#Matrix[i][j] = 100
		
plt.imshow(Matrix, extent = (0,10,0,10), cmap = "jet", origin = "lower")
plt.plot([1,10],[0,9], color = "xkcd:black")
plt.xlabel("b")
plt.ylabel("a")
plt.colorbar(label = r"$\log_{10}\left(\frac{W_{1,100}}{W_{1,2}}\right)$")
plt.show()
