from include import newtons
from sympy import symbols
import time

start = time.time()
x = symbols('x')
eqn = x**2 - 2*x + 1

initial = 10; n = 10

newton = newtons.NewtonsMethod(x, eqn)
final = newton.solveNewton(n,initial)
end = time.time()

print(f"Elapsed Time: {(end-start):.2f} sec")