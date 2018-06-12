import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rc


def BuildProbas(Size=100, a=1, b=1):
    Probs = [0 for i in xrange(Size)]
    for i in xrange(Size):
        print float(i)/Size*100
        for j in xrange(Size):
            Probs[i]+=float(abs(i-j)**a)/float((i+j+2)**b)
    Probs = np.array(Probs)
    Probs/=Probs.sum()
    return Probs
                  

def PlotProbs(Probs, Plotlabel = ""):
    CumProbs = Probs
    Xvalues= [float(i)/len(CumProbs)*100 for i in xrange(len(CumProbs))]
    CumProbs *= float(len(CumProbs))/100.0
    plt.plot(Xvalues,CumProbs, label = Plotlabel)
    return

def FindMin(Probs):
    return Probs.argmin()+1

somelist = []
for i in xrange(6):
	a=1
	b=a+i/5.
	somelist.append(BuildProbas(Size=100,a=a,b=b))
	PlotProbs(somelist[i], Plotlabel = "a="+str(a) +" and b="+ str(b))
plt.legend()

plt.title(r"$w_{i}=\sum_{j=1}^{100}\frac{\vert i - j\vert^a}{(i + j)^b}$", y=1.025)
plt.xlabel("Rank i")
plt.ylabel(r"$w_{i}\cdot\left(\sum_{i=1}^{100}w_i\right)^{-1}$")
plt.show()
"""
#rc("text", usetex=True)
Probs = BuildProbas(100,1,1.6)
PlotProbs(Probs, Plotlabel="N = 100 Ranks")
Probs = BuildProbas(100,1,1.6)
PlotProbs(Probs, Plotlabel = "N = 10000 Ranks")
overx = np.array([1/(i+1)**0.6 for i in xrange(100)])
overx /= overx.sum()
plt.plot([i+1 for i in xrange(100)],overx, label=r"$x^{-0.6}$")
plt.xlabel(r"$R_i\cdot \frac{100}{N}$")
plt.ylabel(r"$\frac{\sum_{j=1}^{N} w_{ij}}{\sum_{i,j=1}^{N} w_{ij}}\cdot \frac{N}{100}$", fontsize = 15)
plt.legend()
plt.show()
"""
"""
Iss = range(51)
MinRanks = []
Xss = []
for i in Iss:
    Xss.append(i/25.0)
    Probs = BuildProbas(100,1,1+i/25.0)
    MinRanks.append(FindMin(Probs))
plt.plot(Xss,MinRanks,label=r"$\min_i \sum_{j=1}^{100}\frac{\vert i - j \vert^1}{(i + j)^{1+x}}$")
MinRanks = []
Xss = []
for i in Iss:
    Xss.append(i/25.0)
    Probs = BuildProbas(100,6,6+i/25.0)
    MinRanks.append(FindMin(Probs))
plt.plot(Xss,np.array(MinRanks),label=r"$\min_i \sum_{j=1}^{100}\frac{\vert i - j \vert^6}{(i + j)^{6+x}}$")
plt.xlabel("Difference of the exponents x")
plt.ylabel("Rank with lowest probability")
plt.legend(fontsize = 12)
plt.show()
"""
"""
#to plot minima
ass=[i/10.0 for i in xrange(1001)]
ProbList = []
for value in ass:
    ProbList.append(BuildProbas(a=value,b=value+0.6))
yss=[]
pmaxs=[]
for Probs in ProbList:
    yss.append(FindMin(Probs))
    pmaxs.append(Probs[0])
plt.plot(ass,yss, label="Rang mit niedrigster Wahrscheinlichkeit als Funktion von a")
plt.legend()
plt.show()
plt.plot(ass,pmaxs, label="Wahrscheinlichkeit fuer Rang 1 als Funktion von a")
plt.legend()
plt.show()
"""
