import NodeProbs as NoP
import numpy as np
import matplotlib.pyplot as plt
"""
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
plt.imshow(Mins, cmap="jet", origin = "lower", extent = (0,10,0,10), Interpolation = "none")
plt.plot([1,10],[0,9], color="xkcd:black")
plt.xlabel("b")
plt.ylabel("a")
#plt.axis([0,10,0,10])
plt.colorbar(label = "Rank with lowest probability", shrink=0.75)
plt.subplot(122)
plt.imshow(startend, cmap="jet", origin = "lower", extent = (0,10,0,10), Interpolation = "none")
plt.plot([1,10],[0,9], color = "xkcd:black")
plt.xlabel("b")
plt.ylabel("a")
#plt.axis([0,10,0,10])
plt.colorbar(label = r"$\frac{P(r=1)}{P(r=100)}$", shrink=0.75, extend="max")
plt.legend()
plt.show()

Minssmall = [[0 for i in xrange(101)] for j in xrange(101)]
startendsmall = [[0 for i in xrange(101)] for j in xrange(101)]

for i in xrange(len(Mins)):
    print float(i)/len(Mins)*100
    for j in xrange(len(Mins[i])):
        Ps = NoP.BuildProbas(a = i/30.0, b=j/30.0)
        startendsmall[i][j] = Ps[0]/Ps[-1]
        if startendsmall[i][j] > 100:
            startendsmall[i][j] = 100
        Minssmall[i][j] = NoP.FindMin(Ps)
        
plt.subplot(121, label = "Location of the minima")
plt.imshow(Minssmall, cmap="jet", origin = "lower", extent = (0,3,0,3), Interpolation = "none")
plt.plot([1,3],[0,2], color="xkcd:black")
plt.xlabel("b")
plt.ylabel("a")
#plt.axis([0,10,0,10])
plt.colorbar(label = "Rank with lowest probability", shrink=0.75)
plt.subplot(122)
plt.imshow(startendsmall, cmap="jet", origin = "lower", extent = (0,3,0,3), Interpolation = "none")
plt.plot([1,3],[0,2], color = "xkcd:black")
plt.xlabel("b")
plt.ylabel("a")
#plt.axis([0,10,0,10])
plt.colorbar(label = r"$\frac{P(r=1)}{P(r=100)}$", shrink=0.75, extend="max")
plt.legend()
plt.show()
"""
Minsbig = [[0 for i in xrange(101)] for j in xrange(101)]
startendbig = [[0 for i in xrange(101)] for j in xrange(101)]

for i in xrange(len(Minsbig)):
    print float(i)/len(Minsbig)*100
    for j in xrange(len(Minsbig[i])):
        Ps = NoP.BuildProbas(a = 5.9001079220 + i/100000000000.0, b = 6.9999999995 + j/100000000000.0)
        startendbig[i][j] = Ps[0]/Ps[-1]
        if startendbig[i][j] > 100:
            startendbig[i][j] = 100
        Minsbig[i][j] = NoP.FindMin(Ps)
        
plt.subplot(121, label = "Location of the minima")
plt.imshow(Minsbig, cmap="jet", origin = "lower", extent = (6.9999999995,7.0000000005,5.9001079220,5.9001079230), Interpolation = "none")
#plt.plot([6,8],[5,7], color="xkcd:black")
plt.xlabel("b")
plt.ylabel("a")
#plt.axis([0,10,0,10])
plt.colorbar(label = "Rank with lowest probability", shrink=0.75)
plt.subplot(122)
plt.imshow(startendbig, cmap="jet", origin = "lower", extent = (6.9999999995,7.0000000005,5.9001079220,5.9001079230), Interpolation = "none")
#plt.plot([6,8],[5,7], color = "xkcd:black")
plt.xlabel("b")
plt.ylabel("a")
#plt.axis([0,10,0,10])
plt.colorbar(label = r"$\frac{P(r=1)}{P(r=100)}$", shrink=0.75, extend="max")
plt.show()

