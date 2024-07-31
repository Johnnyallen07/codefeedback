solution = {
    'task_a': (
        'x,y,f,g,s,p',
        """
import numpy as np
def func(x):
    y = 1 / (1+25*x**2)
    #y = np.sin(x)

    return y
def Lagrangian(j,xn,xp):
    # establish the number of nodes
    n = len(xn)
    # the order of the polynomial will then be n-1

    # set the initial value of the polynomial to 1
    L = 1
    # range of k is from 0 to n-1 (the order of the polynomial)
    for k in range(0,n):
        # exclude the case k == j
        if k != j:
            L *= (xp-xn[k]) / (xn[j]-xn[k])
    return L
def LagInterp(xn,yn,x):
    N = len(xn)
    # establish the order of the interpolating polynomial, N-1
    n = N - 1
    y = np.ndarray(len(x))
    # interpolate for all the values of x in the interpolating range
    for i in range(len(x)):
        # evaluate pn(xp)
        yp = 0
        # use Langrangian polynomial up to n, included
        for j in range(0,n+1):
            yp += yn[j] * Lagrangian(j,xn,x[i])
        # add the curren value of yp to the list of y
        y[i] = yp
    return y
a = 1 # lower interval
b = 2 # upper interval
N = 4 # number of nodes
xn = np.linspace(a,b,N)

yn = func(xn)

# set the domain of interpolation
dx = 0.05
x = np.arange(0,3+dx,dx)

y = LagInterp(xn,yn,x)
    """
),
    'task_b' : ('I',"""

    def f(x):
        y = 1/np.sqrt(x**17.10+2023)
        #y = 1/np.sqrt(x**1.10+2023)
        #y = np.sin(x)

        return y

    def trapzeqd(x,y):
        # get the interval h: distance between any two consecutives nodes
        h = x[1] - x[0]
        # get the number of intervals
        N = len(x) - 1  # obviously x and y must have same length
        S = 0.0
        for n in range(1,N):
            S += y[n]  # add the current calue of y

        I = h * (y[0]/2 + S + y[-1]/2 )

        # an alternative approach, with slicing and the function np.sum(), the integral can be computed within one line
        I = h * (y[0]/2 + np.sum(y[1:-1]) + y[-1]/2 )

        return I
    a = 0
    b = [10,100,1000,10000]
    N = 5
    I = [] # generate an empty list where to store the results of I, for the various b
    for up in b:
        # recompute the x interval
        x = np.linspace(a,up,N+1)
        # recompute y for these new nodes
        y = f(x)
        # compute the integral and append the resukt to the list I
        I += [trapzeqd(x,y)]

    """
)
}
