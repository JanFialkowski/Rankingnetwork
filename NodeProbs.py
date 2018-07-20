import numpy as np
import matplotlib.pyplot as plt


def BuildProbas(Size=100, a=1, b=1):
    Probs = [0 for i in xrange(Size)]
    for i in xrange(Size):
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
    return Probs.argmin()+1
