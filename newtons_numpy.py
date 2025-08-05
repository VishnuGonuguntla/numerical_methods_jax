from include import Newtons_numpy as nt
from sympy import symbols
import time

start = time.time()
x = symbols('x')
eqn = x**2 - 2*x + 1

initial = 10; n = 10

func = nt.NewtonsMethod(x, eqn)
func.solveNewton(n,initial)
end = time.time()
func.plot()

print(f"Elapsed Time: {(end-start):.2f} sec")