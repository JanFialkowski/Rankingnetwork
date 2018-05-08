import numpy as np
import matplotlib.pyplot as plt


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
    Xvalues= [float(i+1)/len(CumProbs)*100 for i in xrange(len(CumProbs))]
    CumProbs *= float(len(CumProbs))/100.0
    plt.plot(Xvalues,CumProbs, label = Plotlabel)
    return

def FindMin(Probs):
    MinProbs = 0
    for i in xrange(len(Probs)):
        if Probs[i]<Probs[MinProbs]:
            MinProbs=i
    return MinProbs

Probs = BuildProbas(100,1,1.6)
PlotProbs(Probs, Plotlabel="100 Knoten")
Probs = BuildProbas(100,100,100.6)
PlotProbs(Probs, Plotlabel = "10000 Knoten")
overx = np.array([1/(i+1)**0.6 for i in xrange(100)])
overx /= overx.sum()
plt.plot([i+1 for i in xrange(100)],overx, label="x**-0.6")
plt.legend()
plt.show()

#for i in xrange(6):
#    Probs = BuildProbas(100,1,1+i/5.0)
#    PlotProbs(Probs, Plotlabel="1 und %g"%(1+i/5.0))
#plt.legend()
#plt.show()

#to plot minima
#ass=[i/10.0 for i in xrange(1001)]
#ProbList = []
#for value in ass:
#    ProbList.append(BuildProbas(a=value,b=value+0.6))
#yss=[]
#pmaxs=[]
#for Probs in ProbList:
#    yss.append(FindMin(Probs))
#    pmaxs.append(Probs[0])
#plt.plot(ass,yss, label="Rang mit niedrigster Wahrscheinlichkeit als Funktion von a")
#plt.legend()
#plt.show()
#plt.plot(ass,pmaxs, label="Wahrscheinlichkeit fuer Rang 1 als Funktion von a")
#plt.legend()
#plt.show()
