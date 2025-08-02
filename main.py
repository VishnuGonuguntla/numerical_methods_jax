import numpy as np
import matplotlib.pyplot as plt

n = 200
x = np.linspace(0,10,n+1)
t = 2
delt = 0.01
delx = 10/n
nt = int(t/delt)
print(nt)
# Initial Condition:
u = np.zeros(n+1)
u[n//4:n//2+1] = np.linspace(0,1,n//4+1)
u[n//2:3*n//4] = np.linspace(1,0,n//4)
plt.plot(x,u,label='Initial Condition',linestyle="--")
tx = delt/delx
up = np.zeros(n+1)
um = np.zeros(n+1)
u_view = np.zeros((nt, n+1))
u_view[0,:] = u.copy()

m = range(1,n)
mp = range(2,n+1)
mm = range(0,n-1)

for t in range(0,nt-1):
    # u[1:n] = u[1:n] + tx*u[1:n]*(u[1:n]-u[2:n+1])
    up[1:n] = 0.5*(u_view[t,m] + abs(u_view[t,m]))*u_view[t,m]*0.5
    um[1:n] = 0.5*(u_view[t,m] - abs(u_view[t,m]))*u_view[t,m]*0.5
    fi1 = up[m] + um[mp]
    fi  = up[mm] + um[m]
    u_view[t+1,m] = u_view[t,m] - tx*(fi1 - fi)
plt.plot(x,u_view[-1,:],label='Final Condition',linestyle="--")
plt.show()

plt.pcolor(x,np.linspace(0,t,nt),u_view,shading='nearest')
plt.show()