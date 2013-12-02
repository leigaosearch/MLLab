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
def computeCost(xmat,ymat,thetamat): 
    m = ymat.shape[0]
    tempmat  = xmat*thetamat-ymat
    J = tempmat.T*tempmat/2./m
    return J[0][0]
def gradientDescent(xmat, ymat, thetamat, alpha, num_iters):
   m = ymat.shape[0]
   J_history = zeros((num_iters, 1))
   for iter in range(num_iters):
       #g = dot(X.T,(dot(X,theta)-array(y).T))/m
  
       thetamat = thetamat -alpha*(xmat.T*(xmat*thetamat-ymat))/m
       J_history[iter] = computeCost(xmat, ymat, thetamat);

   return thetamat, J_history



if __name__=="__main__":
    X,y = loadData("ex1data1.txt");

    theta = zeros((2, 1))
    iterations = 1500;
    alpha = 0.01;
    m = len(y)
    new_col = ones((m,1))
    xmat = mat(X)
    xmat = concatenate((new_col,xmat),1)
    ymat = mat(y).T
    computeCost(xmat, ymat, theta)
    restheta,res2 = gradientDescent(xmat, ymat, theta, alpha, iterations);
    print restheta
    import matplotlib.pyplot as plt
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.scatter(X,y)
    myx  = range(30)
    myy  = restheta[0,0]+restheta[1,0]*myx
    ax.plot(myx,myy,s=2,c='red')
    plt.show()
    

    
    plt.show()
    pause()