from numpy import *
def loadData(fileName):
    fr = open(fileName)
    numFeat = len(open(fileName).readline().split(',')) - 1
    x = [];
    y = [];
    for line in fr.readlines():
        lineArr = []
        curLine = line.strip().split(',')
        for i in range(numFeat):
            lineArr.append(float(curLine[i]))
        x.append(lineArr)
        y.append(float(curLine[-1]))
    return x, y

def linearRegCostFunction(xmat,ymat,thetamat,lam): 
    m = ymat.shape[0]
    tempmat  = xmat*thetamat-ymat
    #temprory theta to support j==0 
    tempthetamat = themat.copy()
    tempthetamat[0][0] = 0
    thetasum = tempthetamat.T*tempthetamat*lam
    J = tempmat.T*tempmat/2./m+thetasum/2./m
    grad = xmat.T*tempmat+tempthetamat*lam/m
    return J[0][0],grad




if __name__=="__main__":
    X,y = loadData("ex5data1.mat");
    import scipy.io
    mat = scipy.io.loadmat('file.mat')

    theta = zeros((2, 1))
    iterations = 1500;
    alpha = 0.01;
    m = len(y)
    new_col = ones((m,1))
    xmat = mat(X)
    xmat = concatenate((new_col,xmat),1)
    ymat = mat(y).T
    lam = 0
    restheta,res2 = linearRegCostFunction(xmat, ymat, theta,lam);
    print restheta
    import matplotlib.pyplot as plt
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.scatter(X,y)
    myx  = range(30)
    myy  = restheta[0,0]+restheta[1,0]*myx
    ax.plot(myx,myy,s=2,c='red')
    plt.show()
    pause()
