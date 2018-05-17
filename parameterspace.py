import NodeProbs as NoP
import numpy as np
import matplotlib.pyplot as plt

Mins = [[0 for i in xrange(101)] for j in xrange(101)]
startend = [[0 for i in xrange(101)] for j in xrange(101)]

for i in xrange(len(Mins)):
    print float(i)/len(Mins)*100
    for j in xrange(len(Mins[i])):
        Ps = NoP.BuildProbas(a = i/10.0, b=j/10.0)
        startend[i][j] = Ps[0]/Ps[-1]
        if startend[i][j] > 100:
            startend[i][j] = 100
        Mins[i][j] = NoP.FindMin(Ps)
        
plt.subplot(121, label = "Location of the minima")
plt.imshow(Mins, cmap="jet")
plt.xlabel("b")
plt.ylabel("a")
#plt.axis([0,10,0,10])
plt.colorbar(label = "Rank with lowest probability", shrink=0.65)
plt.subplot(122)
plt.imshow(startend, cmap="jet")
plt.xlabel("b")
plt.ylabel("a")
#plt.axis([0,10,0,10])
plt.colorbar(label = r"$P(r=1)/P(r=100)$", shrink=0.65, extend="max")
plt.legend()
plt.show()
