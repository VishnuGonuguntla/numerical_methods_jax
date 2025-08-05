import numpy as np
from sympy import diff
import matplotlib.pyplot as plt

class NewtonsMethod:
    def __init__(self, x,eqn):
        self.x = x
        self.eqn = eqn
        self.diff = diff(eqn)
        self.a = np.zeros(1)
    
    def solveNewton(self, n, initial):
        f = lambda xy: self.eqn.subs(self.x, xy)
        fdash = lambda xy: self.diff.subs(self.x,  xy)
        self.x0 = np.zeros(n)
        self.x0[0] = initial
        for i in range(n-1):
            self.x0[i+1] = self.x0[i] - f(self.x0[i])/fdash(self.x0[i])

    def plot(self):
        print(self.x0)
        plt.plot(self.x0)
        plt.show()