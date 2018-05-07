import numpy as np
import matplotlib.pyplot as plt


def BuildMatrix(Size=1000, a=1, b=1):
    #baut die Wahrscheinlichkeitsmatrix für Size Knoten mit den Exponenten a und b.
    Matrix = np.array([[float(i)+j for i in xrange(Size)] for j in xrange(Size)])
    for i in xrange(len(Matrix)):
        for j in xrange(len(Matrix[i])):
            Matrix[i][j] = abs(i-j)**a/(i+j+2.)**b
    #Matrix = Matrix.cumsum()
    Matrix /= Matrix.sum()
    #print Matrix.sum()
    #Matrix = Matrix.reshape(len(Matrix),len(Matrix))
    return Matrix
                  

def PlotProbs(NewMatrix, Plotlabel = ""):
    #Plottet die kumulative Wahrscheinlichkeit für einen Knoten von Rang n Teil eines neuen Links zu sein.
    CumProbs = [0 for i in xrange(len(NewMatrix))]
    for i in xrange(len(NewMatrix)):
        CumProbs[i]=NewMatrix[i].sum()
        for j in xrange(len(NewMatrix)):
            CumProbs[i] += NewMatrix[j][i]
    Xvalues= [float(i)/len(CumProbs)*100 for i in xrange(len(CumProbs))]
    CumProbs = np.array(CumProbs)
    CumProbs *= len(CumProbs)/float(100)
    plt.plot(Xvalues,CumProbs, label = Plotlabel)
    return

NewMatrix = BuildMatrix(1000,1,1.6)
PlotProbs(NewMatrix, Plotlabel="1000 Knoten")
NewMatrix = BuildMatrix(100,1,1.6)
PlotProbs(NewMatrix, Plotlabel = "100 Knoten")
overx = np.array([1/(i+1)**0.6 for i in xrange(100)])
overx /= overx.sum()*0.5
plt.plot(overx, label="x**-0.6")
plt.legend()
plt.show()
