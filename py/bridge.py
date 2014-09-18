import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import proj3d

def new_fig(xlabel=r'$b_0^\ell$',ylabel=r'$b_1^\ell$',zlabel=r'$b_2^\ell$',
                backgroundcolor='w'):

    fig = plt.figure()
    ax = fig.gca(projection='3d')

    ax.set_xlabel(xlabel,color='k',backgroundcolor=backgroundcolor,
        fontsize=16)
    ax.set_ylabel(ylabel,color='k',backgroundcolor=backgroundcolor,
        fontsize=16)
    ax.set_zlabel(zlabel,color='k',backgroundcolor=backgroundcolor,
        fontsize=16)
    ax.w_xaxis.set_rotate_label(False)
    ax.w_yaxis.set_rotate_label(False)
    ax.w_zaxis.set_rotate_label(False)

    ax.tick_params(axis='x', colors='red')
    ax.tick_params(axis='y', colors='blue')
    ax.tick_params(axis='z', colors='green')

    ax.set_xlim(-1.5, 1.5)
    ax.set_ylim(-0.5, 1.5)
    ax.set_zlim(-0.25, 1.25)

    ax.view_init(20,345)
    ax.set_autoscale_on(False)
    
    return fig,ax

def vector(ax,y, label):
    colors = ['r', 'b', 'g']
    v = [0, 0, 0]
    w = v[:]
    for n, yp in enumerate(y):
        color = colors[n]
        x = v[n] + yp
        w[n] = x
        #ax.plot([v[0], w[0]], [v[1], w[1]], [v[2], w[2]], color=color, 
        #        linestyle='--',linewidth=2)
        v[n] = x
    ax.plot([0, y[0]], [0, y[1]], [0, y[2]], color='k', linewidth=2, 
        zorder=10)
    ax.scatter(y[0],y[1],y[2], marker='o', s=40, color='k')
    ax.text(1*y[0], 1*y[1], 1*y[2], label, backgroundcolor='#fcffc9', 
        ha='center', va='center', size=14, zorder=20)

def project_b0(ax, y, v, color='r'):
    ax.plot([y[0],v], [y[1], y[1]], [y[2], y[2]], color=color, linestyle=':')
    ax.plot([v, v], [0, y[1]], [0, y[2]], color=color, linewidth=2)
    ax.scatter(v, y[1], y[2], color=color, marker="*", s=100)
    
def project_b1(ax, y, v, color='b'):
    ax.plot([y[0],y[0]], [y[1], v], [y[2], y[2]], color=color, linestyle=':')
    ax.plot([0, y[0]], [v, v], [0, y[2]], color=color, linewidth=2)
    ax.scatter(y[0], v, y[2], color=color, marker="*", s=100)    
    
def project_b2(ax, y, v, color='g'):
    ax.plot([y[0],y[0]], [y[1], y[1]], [y[2], v], color=color, linestyle=':')
    ax.plot([0, y[0]], [0, y[1]], [v,v], color=color, linewidth=2)
    ax.scatter(y[0], y[1], v, color=color, marker="*", s=100)

instants = np.array([-1,0,1])
constant, line, parabola = np.array([1,1,1]), np.array([-1,0,1]), np.array([1,0,1])
colors = ['r','b','g']

fig2, ax2 = new_fig()
vector(ax2, constant, r'$1$')
vector(ax2, line, r'$t$')
vector(ax2, parabola, r'$t^2$')

fig2.savefig("sparsity_basis_0.svg", transparent=True, bbox_inches='tight', pad_inches=0.15)

project_b1(ax2, constant, 1.5)
project_b1(ax2, line, 1.5)
project_b1(ax2, parabola, 1.5)
ax2.text(1,1.5,1.07, r'$[1,1]^T$', ha='center', va='bottom', size=16)
ax2.text(-1,1.5,1.07, r'$[-1,1]^T$', ha='center', va='bottom', size=16)

fig2.savefig("sparsity_basis_1.svg", transparent=True, bbox_inches='tight', pad_inches=0.15)

project_b0(ax2, constant, -1.5)
project_b0(ax2, line, -1.5)
project_b0(ax2, parabola, -1.5)

fig2.savefig("sparsity_basis_2.svg", transparent=True, bbox_inches='tight', pad_inches=0.15)

project_b2(ax2, constant, -0.2)
project_b2(ax2, line, -0.2)
project_b2(ax2, parabola, -0.2)

fig2.savefig("sparsity_basis_3.svg", transparent=True, bbox_inches='tight', pad_inches=0.15)

#fig4, ax4 = new_fig()
#vector(ax4, constant, r'$1$')
#vector(ax4, line, r'$t$')
#vector(ax4, parabola, r'$t^2$')
ax2.plot([0,1/np.sqrt(2)],[0,1/np.sqrt(2)],[0,0],linewidth=2,color='y')
ax2.plot([0,-1/np.sqrt(2)],[0,1/np.sqrt(2)],[0,0],linewidth=2,color='y')
ax2.plot([0,0],[0,0],[0,1],linewidth=2,color='y')
ax2.text(1/np.sqrt(2),1/np.sqrt(2),0, r"$b_0^n$", backgroundcolor='y', 
        ha='center', va='center', size=14)
ax2.text(-1/np.sqrt(2),1/np.sqrt(2),0, r"$b_1^n$", backgroundcolor='y', 
        ha='center', va='center', size=14)
ax2.text(0,0,1, r"$b_2^n$", backgroundcolor='y', 
        ha='center', va='center', size=14)

fig2.savefig("new_planes_1.svg", transparent=True, bbox_inches='tight', pad_inches=0.15)

theta=-np.pi/4;
c,s=1/np.sqrt(2)*np.cos(theta),1/np.sqrt(2)*np.sin(theta)
R=np.array([[c,-s,0],[s,c,0],[0,0,1]])
constant_2=np.dot(R,constant)
line_2=np.dot(R,line)
parabola_2=np.dot(R,parabola)

fig3, ax3 = new_fig(xlabel=r"$b_0'$",ylabel=r"$b_1'$",zlabel=r"$b_2'$")

ax3.tick_params(axis='x', colors='y')  
ax3.tick_params(axis='y', colors='y')
ax3.tick_params(axis='z', colors='y')

vector(ax3, constant_2, r'$1$')
vector(ax3, line_2, r'$t$')
vector(ax3, parabola_2, r'$t^2$')

project_b1(ax3, constant_2, 1.5, color='y')
project_b1(ax3, line_2, 1.5, color='y')
project_b1(ax3, parabola_2, 1.5, color='y')

project_b0(ax3, constant_2, -1.5, color='y')
project_b0(ax3, line_2, -1.5, color='y')
project_b0(ax3, parabola_2, -1.5, color='y')

project_b2(ax3, constant_2, -0.2, color='y')
project_b2(ax3, line_2, -0.2, color='y')
project_b2(ax3, parabola_2, -0.2, color='y')

print constant_2
print line_2
print parabola_2

fig3.savefig("new_planes_2.svg", transparent=True, bbox_inches='tight', pad_inches=0.15)


