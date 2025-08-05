import jax.numpy as jnp
from jax import grad

class Newtons_jax:
    def solve(self, initial,n, f):
        x = jnp.linspace(0,10,11)
        grad_eq = grad(f)
        self.a = jnp.zeros(n)
        self.a = self.a.at[0].set(initial)
        for i in range(n-1):
            self.a = self.a.at[i+1].set(self.a[i] - f(self.a[i])/grad_eq(self.a[i]))
        return self.a 