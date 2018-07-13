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
                  

def PlotProbs(Probs, Plotlabel = "", lw=1.5, marker=""):
    CumProbs = Probs
    Xvalues= [float(i+1)/len(CumProbs)*100 for i in xrange(len(CumProbs))]
    CumProbs *= float(len(CumProbs))/100.0
    plt.plot(Xvalues,CumProbs, label = Plotlabel, lw=lw, marker=marker)
    return

def FindMin(Probs):
    return Probs.argmin()+1

def Integrated(x):
	return (2*x/(1+x)+np.log((x+1)/x)-np.log(4))

def Int2(x):
	return(2*x+x*np.log(1+1/x)-np.log(1+x)-x*np.log(4))/(2-np.log(4))

def func(x):
	return -5./8*(x**0.4/0.5*(2./3-2**0.4)-5./3*((1-x)/((1+x)**0.6)-1))

"""
Probs = BuildProbas(100,1,1.6)
PlotProbs(Probs, Plotlabel="a = 1 and b = 1.6")
Probs = BuildProbas(100,2,2.6)
PlotProbs(Probs, Plotlabel = "a= 2 and b = 2.6")
Probs = BuildProbas(100,10,10.6)
PlotProbs(Probs, Plotlabel = "a= 10 and b = 10.6")
overx = np.array([1/(i+1)**0.6 for i in xrange(100)])
overx /= overx.sum()
plt.plot([i+1 for i in xrange(100)],overx, label=r"$x^{-0.6}$")
plt.xlabel("Rank i")
plt.ylabel(r"$w_{i}\cdot\left(\sum_{i=1}^{N}w_i\right)^{-1}$")
plt.title(r"$w_{i}=\sum_{j=1}^{100}\frac{\vert i - j\vert^{a}}{(i + j)^{a + 0.6}}$", y=1.025)
plt.legend()
plt.show()
"""
"""
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
"""
#rc("text", usetex=True)
#Probs = BuildProbas(10,1,2).cumsum()
#PlotProbs(Probs, Plotlabel="N=10 Ranks", marker=".")
Probs1 = BuildProbas(100,1,2)
PlotProbs(Probs1, Plotlabel="N = 100 Ranks", lw=2.5, marker=".")
ProbsI = Integrated(np.array([(i+1)/100.0 for i in xrange(100)]))
ProbsI /= ProbsI.sum()
r1 = (ProbsI - Probs1)
r1 **= 2
PlotProbs(ProbsI, Plotlabel="Sampling approach")
ProbsA = [Int2(1/100.)]
ProbsB = [Int2((i+2)/100.)-Int2((i+1)/100.) for i in xrange(100-1)]
ProbsA.extend(ProbsB)
ProbsI2 = np.array(ProbsA)
r2 = (Probs1- ProbsI2)
r2 **= 2
PlotProbs(ProbsI2, Plotlabel = "Integrational approach")
#Probs2 = BuildProbas(10000,1,2)
#PlotProbs(Probs2, Plotlabel = "N = 10000 Ranks")

#overx = np.array([1/(i+1)**0.6 for i in xrange(100)])
#overx /= overx.sum()
#plt.plot([i+1 for i in xrange(100)],overx, label=r"$x^{-0.6}$")
plt.xlabel(r"$i\cdot\frac{100}{N}$")
plt.ylabel(r"$w_{i}\cdot\left(\sum_{i=1}^{N}w_i\right)^{-1}\cdot\frac{N}{100}$")
plt.title(r"$w_{i}=\sum_{j=1}^{N}\frac{\vert i - j\vert^1}{(i + j)^{2}}$", y=1.025)
plt.legend()
plt.show()

Probs1 = Probs1.cumsum()
PlotProbs(Probs1, Plotlabel = "Cumulative probability distribution", lw=2.5, marker = ".")
ProbsI2 = ProbsI2.cumsum()
PlotProbs(ProbsI2, Plotlabel = "Integrational approach")
plt.show()
#Diffs = np.array([Probs[i]-ProbsI2[i*len(ProbsI2)/len(Probs)] for i in xrange(len(Probs))])
#print Diffs
#print Diffs.sum()
"""

#"""
Probs1 = BuildProbas(10000,1,2.6)
PlotProbs(Probs1, Plotlabel="N = 100 Ranks", lw=2.5, marker=".")
ProbsA = [func(1/10000.)]
ProbsB = [func((i+2)/10000.)-func((i+1)/10000.) for i in xrange(10000-1)]
ProbsA.extend(ProbsB)
ProbsI2 = np.array(ProbsA)
r2 = (Probs1- ProbsI2)
r2 **= 2
PlotProbs(ProbsI2/ProbsI2.sum(), Plotlabel = "Integrational approach")
plt.show()
#"""

#"""
Probs1 = BuildProbas(1000,1,2.6)
plt.plot(Probs1.cumsum(),lw=2.5)
Probs2 = np.array([func((i+1)/1000.) for i in xrange(1000)])
plt.plot(Probs2/Probs2[-1])
plt.show()
#"""

"""
Iss = range(1001)
MinRanks = []
Xss = []
for i in Iss:
    Xss.append(i/500.0)
    Probs = BuildProbas(500,1,1+i/500.0)
    MinRanks.append(FindMin(Probs))
plt.plot(Xss,MinRanks,label=r"$\min_i \sum_{j=1}^{500}\frac{\vert i - j \vert^1}{(i + j)^{1+x}}$")
MinRanks = []
Xss = []
for i in Iss:
    Xss.append(i/500.0)
    Probs = BuildProbas(500,6,6+i/500.0)
    MinRanks.append(FindMin(Probs))
plt.plot(Xss,np.array(MinRanks),label=r"$\min_i \sum_{j=1}^{500}\frac{\vert i - j \vert^6}{(i + j)^{6+x}}$")
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
