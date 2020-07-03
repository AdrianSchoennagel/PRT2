import numpy as np
from numpy import cos, sin, tan
import matplotlib.pyplot as plt

from Parameters import *
import FunctionBlocks as FB
from input import *

x0 = [0]

fig1, (ax1, ax2, ax3, ax4) = plt.subplots(4)

tt = np.arange(sim_para.t0, sim_para.tf + sim_para.dt, sim_para.dt)
solver_kaskade = FB.Solver_Kaskade(tt)
ys = solver_kaskade.calc()
y_r  = ys[0]
y_s1 = ys[1]
y_s2 = ys[2]
y_rh = ys[3]
e    = ys[4]
x_h  = ys[5]


ax1.plot(tt, np.vectorize(cubic_jump)(tt, para.ts, para.dts, para.w0, para.w1), label='$u(t)$', lw=1, color='b')
ax1.plot(tt, np.vectorize(cubic_jump)(tt, para.tz1, para.dtz1, para.z01, para.z11), label='$z1(t)$', lw=1, color='g')
ax1.plot(tt, np.vectorize(cubic_jump)(tt, para.tz2, para.dtz2, para.z02, para.z12), label='$z2(t)$', lw=1, color='k')
ax2.plot(tt, y_r, label='$y_r(t)$', lw=1, color='r')
ax2.plot(tt, y_rh, label='$y_{rh}(t)$', lw=1, color='b')
ax3.plot(tt, y_s1, label='$y_{s1}(t)$', lw=1, color='r')
ax3.plot(tt, y_s2, label='$y_{s2}(t)$', lw=1, color='b')
ax4.plot(tt, e, label='$E(t)$', lw=1, color='r')
ax4.plot(tt, x_h, label='$X_H(t)$', lw=1, color='b')

ax1.set_title('Führungsverlauf')
ax1.set_ylabel(r'u(t)')
ax1.set_xlabel(r't in s')
ax2.set_title('Ausgänge Regler')
ax2.set_xlabel(r't in s')
ax3.set_title('Ausgänge Strecke')
ax3.set_xlabel(r't in s')
ax4.set_title('Abweichungen')
ax4.set_xlabel(r't in s')

ax1.grid(True)
ax2.grid(True)
ax3.grid(True)
ax4.grid(True)
ax1.legend()
ax2.legend()
ax3.legend()
ax4.legend()

plt.tight_layout()
plt.show()
"""

ax1.plot(tt, y_rh, label='u_s1', lw=1, color='b')
ax1.plot(tt, y_s1, label='y_s1', lw=1, color='r')
ax2.plot(tt, x_h, label='u_s2', lw=1, color='b')
ax2.plot(tt, y_s2, label='y_s2', lw=1, color='r')
ax3.plot(tt, e, label='u_r', lw=1, color='b')
ax3.plot(tt, y_r, label='y_r', lw=1, color='r')
ax4.plot(tt, y_r - x_h, label='u_rh', lw=1, color='b')
ax4.plot(tt, y_rh, label='y_rh', lw=1, color='r')

ax1.grid(True)
ax2.grid(True)
ax3.grid(True)
ax4.grid(True)
ax1.legend()
ax2.legend()
ax3.legend()
ax4.legend()

plt.tight_layout()
plt.show()
"""