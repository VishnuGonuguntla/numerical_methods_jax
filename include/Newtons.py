import numpy as np
from sympy import symbols, solve, diff

class NewtonsMethod:
    def __init__(self, x,eqn):
        self.x = x
        self.eqn = eqn
        self.diff = diff(eqn)        
    
    def solveNewton(self, n, initial):
        eq = lambda xy: self.eqn.subs(self.x, xy)
        ans = lambda xy: self.diff.subs(self.x,  xy)
        x0 = np.zeros(n)
        x0[0] = initial
        for i in range(n-1):
            x0[i+1] = x0[i] - eq(x0[i])/ans(x0[i])
        return x0