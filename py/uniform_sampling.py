import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
import resources
from riddle import plot123

# Three functions
hack = 0.0001 # avoid browser SVG rendering bug
functions = lambda x: [1+hack*x, x, 0.5*x**2]

# Domain (X) and values (Y) for each function
X = np.linspace(-np.pi, np.pi, 256, endpoint=True)
Y = functions(X)

# Sample points
a = [-1, 0, 1]
b = functions(np.array(a))

# Labels and sample colors (for each graph)
labels = [r'$f(t)=x_0$', r'$f(t)=x_1 t$', r'$f(t)=x_2 t^2$']
col = ['red', 'blue', 'green']

fig=plt.figure(figsize=(8,2))
for p in range(3): plot123(fig,p,X,Y,a,b,labels,col)

fig.savefig("uniform_sampling.svg", transparent=True, bbox_inches='tight', pad_inches=0.15)

