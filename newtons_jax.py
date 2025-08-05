from include import Newtons_jax as nt
import time

start = time.time()
n = 10; initial = 10
f = lambda x: x**2 - 2*x + 1
func = nt.Newtons_jax()
func.solve(initial, n ,f)
end = time.time()
func.plot()
print(f"Elapsed Time: {(end-start):.4f} sec")