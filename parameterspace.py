import NodeProbs as NoP
import numpy as np
import matplotlib.pyplot as plt
#"""
Mins = [[0 for i in xrange(101)] for j in xrange(101)]
startend = [[0 for i in xrange(101)] for j in xrange(101)]

for i in xrange(len(Mins)):
    print float(i)/len(Mins)/3.*100
    for j in xrange(len(Mins[i])):
        Ps = NoP.BuildProbas(a = i/10.0, b=j/10.0)
        startend[i][j] = np.log10(Ps[0]/Ps[-1])
        #if startend[i][j] > 100:
            #startend[i][j] = 100
        Mins[i][j] = NoP.FindMin(Ps)
        
plt.subplot(321, label = r"$\min_iP(r=i)$")
plt.title("(a)", loc="left")
plt.imshow(Mins, cmap="jet", origin = "lower", extent = (0,10,0,10), Interpolation = "none")
plt.plot([1,10],[0,9], color="xkcd:black")
plt.xlabel("b")
plt.ylabel("a")
#plt.axis([0,10,0,10])
plt.colorbar(label = r"$\min_i\left(P(r=i)\right)$", shrink=0.75)
plt.subplot(322)
plt.title("(b)", loc = "left")
plt.imshow(startend, cmap="jet", origin = "lower", extent = (0,10,0,10), Interpolation = "none")
plt.plot([1,10],[0,9], color = "xkcd:black")
plt.xlabel("b")
plt.ylabel("a")
plt.colorbar(label = r"$\log_{10}\left(\frac{P(r=1)}{P(r=100)}\right)$", shrink=0.75)
plt.legend()
#plt.show()

#"""
Minssmall = [[0 for i in xrange(101)] for j in xrange(101)]
startendsmall = [[0 for i in xrange(101)] for j in xrange(101)]

for i in xrange(len(Mins)):
    print (float(i)+100)/len(Mins)/3.*100
    for j in xrange(len(Mins[i])):
        Ps = NoP.BuildProbas(a = i/30.0, b=j/30.0)
        startendsmall[i][j] = np.log10(Ps[0]/Ps[-1])
        #if startendsmall[i][j] > 100:
            #startendsmall[i][j] = 100
        Minssmall[i][j] = NoP.FindMin(Ps)
        
plt.subplot(325, label = "Location of the minima")
plt.title("(e)", loc = "left")
plt.imshow(Minssmall, cmap="jet", origin = "lower", extent = (0,3,0,3), Interpolation = "none")
plt.plot([1,3],[0,2], color="xkcd:black")
plt.xlabel("b")
plt.ylabel("a")
#plt.axis([0,10,0,10])
plt.colorbar(label = r"$\min_i\left(P(r=i)\right)$", shrink=0.75)
plt.subplot(326)
plt.title("(f)", loc = "left")
plt.imshow(startendsmall, cmap="jet", origin = "lower", extent = (0,3,0,3), Interpolation = "none")
plt.plot([1,3],[0,2], color = "xkcd:black")
plt.xlabel("b")
plt.ylabel("a")
#plt.axis([0,10,0,10])
plt.colorbar(label = r"$\log_{10}\left(\frac{P(r=1)}{P(r=100)}\right)$", shrink=0.75)
plt.legend()
#plt.show()
"""
"""
Minsbig = [[0 for i in xrange(101)] for j in xrange(101)]
startendbig = [[0 for i in xrange(101)] for j in xrange(101)]

for i in xrange(len(Minsbig)):
    print (float(i)+200)/len(Minsbig)/3.*100
    for j in xrange(len(Minsbig[i])):
        Ps = NoP.BuildProbas(a = 5.0 + i/50.0, b = 6.0 + j/50.0)
        startendbig[i][j] = np.log10(Ps[0]/Ps[-1])
        #if startendbig[i][j] > 100:
            #startendbig[i][j] = 100
        Minsbig[i][j] = NoP.FindMin(Ps)
        
plt.subplot(323, label = r"$\min_iP(r=i)$")
plt.title("(c)", loc = "left")
plt.imshow(Minsbig, cmap="jet", origin = "lower", extent = (6.0,8.0,5.0,7.0), Interpolation = "none")
plt.plot([6,8],[5,7], color="xkcd:black")
plt.xlabel("b")
plt.ylabel("a")
#plt.axis([0,10,0,10])
plt.colorbar(label = r"$\min_i\left(P(r=i)\right)$", shrink=0.75)
plt.subplot(324)
plt.title("(d)", loc = "left")
plt.imshow(startendbig, cmap="jet", origin = "lower", extent = (6.0,8.0,5.0,7.0), Interpolation = "none")
plt.plot([6,8],[5,7], color = "xkcd:black")
plt.xlabel("b")
plt.ylabel("a")
#plt.axis([0,10,0,10])
plt.colorbar(label = r"$\log_{10}\left(\frac{P(r=1)}{P(r=100)}\right)$", shrink=0.75)
plt.suptitle(r"$P(r=i)=\frac{w_i}{\sum_i^{100}w_i}$")
plt.show()
"""
"""
