#!puzlet

import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

As = np.array([[1.1,0.9],[1,1]]) # $A^\sharp$
bs = np.array([[2],[2]]) # $b^\sharp$
n = np.array([[0.1],[0]])

xs=np.linalg.solve(As,bs)
xn=np.linalg.solve(As,bs+n)

fig = plt.figure()
ax = fig.gca()

o=np.array([0,0])
#print (*n)

ax.quiver(0,0,As[0,0]*xs[0],As[1,0]*xs[0],
    angles='xy',scale_units='xy',scale=1,color='b')
ax.quiver(As[0,0]*xs[0],As[1,0]*xs[0],As[0,1]*xs[1],As[1,1]*xs[1],
    angles='xy',scale_units='xy',scale=1,color='g')

ax.quiver(0,0,As[0,0]*xn[0],As[1,0]*xn[0],
    angles='xy',scale_units='xy',scale=1,color='b')
ax.quiver(As[0,0]*xn[0],As[1,0]*xn[0],As[0,1]*xn[1],As[1,1]*xn[1],
    angles='xy',scale_units='xy',scale=1,color='g')

ax.set_xlim([0,2.1])
ax.set_ylim([0,2.1])

ax2 = fig.add_axes([.2, .55, .3, .3])
ax2.quiver(0,0,As[0,0],As[1,0],angles='xy',scale_units='xy',scale=1,color='b')
ax2.quiver(0,0,As[0,1],As[1,1],angles='xy',scale_units='xy',scale=1,color='g')
ax2.set_xlim([0,1.2])
ax2.set_ylim([0,1.2])

fig.savefig("two_lines.svg", transparent=True, bbox_inches='tight', pad_inches=0.15)
