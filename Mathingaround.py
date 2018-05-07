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
    Xvalues= [float(i)/len(CumProbs)*100 for i in xrange(len(CumProbs))]
    CumProbs *= float(len(CumProbs))/100.0
    plt.plot(Xvalues,CumProbs, label = Plotlabel)
    return

def FindMin(Probs):
    MinProbs = 0
    for i in xrange(len(Probs)):
        if Probs[i]<Probs[MinProbs]:
            MinProbs=i
    return MinProbs

Probs = BuildProbas(100,0,0.6)
PlotProbs(Probs, Plotlabel="1 und 1.6")
Probs = BuildProbas(100,100,100.6)
PlotProbs(Probs, Plotlabel = "10 und 10.6")
overx = np.array([1/(i+1)**0.6 for i in xrange(100)])
overx /= overx.sum()
plt.plot(overx, label="x**-0.6")
plt.legend()
plt.show()


#to plot minima
ass=[i/10.0 for i in xrange(11)]
ProbList = []
for value in ass:
    ProbList.append(BuildProbas(a=value,b=value+0.6))
yss=[]
for Probs in ProbList:
    yss.append(FindMin(Probs))
plt.plot(ass,yss)
plt.show()
