from include import newtons_jax
import time

start = time.time()
n = 10; initial = 10
f = lambda x: x**2 - 2*x + 1
jaxx = newtons_jax.Newtons_jax()
fin = jaxx.solve(initial, n ,f)
end = time.time()
print(f"Elapsed Time: {(end-start):.4f} sec")