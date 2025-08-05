import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

class Burgers:
    def __init__ (self, n, t, L,delt):
        self.n = n
        self.t = t
        self.L = L
        self.delt = delt
        self.nt = int(t/delt)
        self.delx = self.L/n
    
    def initialization(self):
        self.x = np.linspace(0, self.L, self.n + 1)
        self.u = np.zeros(self.n+1)
        self.u[self.n//5:2*self.n//5 + 1] = 1
        self.u[3*self.n//5:4*self.n//5 + 1] = 1
    
    def burgPlot(self):
        plt.plot(self.x,self.u,label='Initial Condition')
        plt.legend()
        plt.xlabel('x')
        plt.ylabel('u(x,0)')
        plt.show()
    
    def solver(self):
        n = self.n
        tx = self.delt/self.delx
        up = np.zeros(n+1)
        um = np.zeros(n+1)
        u_view = np.zeros((self.nt, n+1))
        u_view[0,:] = self.u.copy()
        
        m =  range(1,n)
        mp = range(2,n+1)
        mm = range(0,n-1)
        for t in range(self.nt-1):
            up[1:n] = 0.5*(u_view[t,m] + abs(u_view[t,m]))*u_view[t,m]*0.5
            um[1:n] = 0.5*(u_view[t,m] - abs(u_view[t,m]))*u_view[t,m]*0.5
            fi1 = up[m] + um[mp]
            fi  = up[mm] + um[m]
            u_view[t+1,m] = u_view[t,m] - tx*(fi1 - fi)
        return u_view

    def animation(self, u_view, save_gif=False):
        fig = plt.figure(figsize=(10, 6))
        def anim(j):
            plt.cla()
            plt.plot(self.x,self.u,label='Initial Condition')
            plt.plot(self.x,u_view[j,:],label='Final Condition',linestyle="--")
            plt.legend()
            plt.xlabel('x')
            plt.ylabel('u(x,t)')
            plt.title(f"Time = {j*self.delt:.2f} seconds")
        anims = animation.FuncAnimation(fig, anim, frames=self.nt-1, repeat=False, interval=1)
        plt.show()
        if save_gif:
            anims.save('animation.gif', writer='pillow', fps=3)
        

    def chart(self, u_view):
        plt.pcolor(self.x,np.linspace(0,self.t,self.nt),u_view,shading='auto')
        plt.colorbar(label='u(x,t)')
        plt.show()