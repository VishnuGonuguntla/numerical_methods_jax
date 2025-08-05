import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animatio
from include import Burgers

n = 200
t = 2
L = 10
delt = 0.01

# Initialization:
burg = Burgers.Burgers(n, t, L, delt)
burg.initialization()
burg.burgPlot()

u_final = burg.solver()

# burg.animation(u_final,False)

burg.chart(u_final)