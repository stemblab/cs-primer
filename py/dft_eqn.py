import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

fig = plt.figure()
ax = fig.gca()

ax.text(1,1,r'$g_n = \frac{1}{N} \sum_{k=0}^{N-1} G_k \cdot e^{(i 2 \pi n / N)k}$',
    ha='center',size=40)
ax.set_frame_on(False)
ax.axes.get_yaxis().set_visible(False)
ax.axes.get_xaxis().set_visible(False)
ax.set_xlim([0,2])
ax.set_ylim([0,2])

fig.savefig("dft_eqn.svg", transparent=True, bbox_inches='tight', pad_inches=0.15)

