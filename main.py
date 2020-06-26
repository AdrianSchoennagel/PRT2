import numpy as np
from numpy import cos, sin, tan
import matplotlib.pyplot as plt

from Parameters import *
import FunctionBlocks as FB
from input import *

x0 = [0]

fig1, (ax1, ax2, ax3, ax4, ax5) = plt.subplots(5)

tt = np.arange(sim_para.t0, sim_para.tf + sim_para.dt, sim_para.dt)
solver = FB.Solver(tt)
ys = solver.calc()
y_pt1 = ys[0]
y_dt1 = ys[1]
y_pt2 = ys[2]
y_pi  = ys[3]

ax1.plot(tt, np.vectorize(cubic_jump)(tt), label='$u(t)$', lw=1, color='b')
ax2.plot(tt, y_pt1, label='$y_pt1(t)$', lw=1, color='r')
ax3.plot(tt, y_dt1, label='$y_dt1(t)$', lw=1, color='r')
ax4.plot(tt, y_pt2, label='$y_pt2(t)$', lw=1, color='r')
ax5.plot(tt, y_pi, label='$y_pi(t)$', lw=1, color='r')

ax1.set_title('Führungsverlauf')
ax1.set_ylabel(r'u(t)')
ax1.set_xlabel(r't in s')
ax2.set_title('Ausgang PT1')
ax2.set_xlabel(r't in s')
ax3.set_title('Ausgang DT1')
ax3.set_xlabel(r't in s')
ax4.set_title('Ausgang PT2')
ax4.set_xlabel(r't in s')
ax5.set_title('Ausgang PI')
ax5.set_xlabel(r't in s')

ax1.grid(True)
ax2.grid(True)
ax3.grid(True)
ax4.grid(True)
ax5.grid(True)


plt.tight_layout()
plt.show()