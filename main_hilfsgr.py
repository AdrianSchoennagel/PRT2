import numpy as np
from numpy import cos, sin, tan
import matplotlib.pyplot as plt

from Parameters import *
import FunctionBlocks as FB
from input import *

x0 = [0]

fig1, (ax1, ax2, ax3, ax4) = plt.subplots(4, figsize=(10,10))

tt = np.arange(sim_para.t0, sim_para.tf + sim_para.dt, sim_para.dt)
solver = FB.Solver_Hilfsg(tt)
hilfsregelgrößenaufschaltung = True
ys = solver.calc(hilfsregelgrößenaufschaltung)
y_r  = ys[0]
y_p1 = ys[1]
y_p2 = ys[2]
y_sh = ys[3]
e_r  = ys[4]
e    = ys[5]
u_p2 = ys[6]

ax1.plot(tt, np.vectorize(cubic_jump)(tt, para.ts, para.dts, para.w0, para.w1), label='$u(t)$', lw=1, color='b')
ax1.plot(tt, np.vectorize(cubic_jump)(tt, para.tz, para.dtz, para.z0, para.z1), label='$z(t)$', lw=1, color='g')
ax2.plot(tt, y_r, label='$y_r(t)$', lw=1, color='r')
ax3.plot(tt, y_p1, label='$y_{p1}(t)$', lw=1, color='r')
ax3.plot(tt, y_p2, label='$y_{p2}(t)$', lw=1, color='g')
ax3.plot(tt, y_sh, label='$y_{sh}(t)$', lw=1, color='b')
ax4.plot(tt, e_r, label='$E_R(t)$', lw=1, color='r')
ax4.plot(tt, e, label='$E(t)$', lw=1, color='b')

ax1.set_title('Führungsverlauf')
ax1.set_ylabel(r'u(t)')
ax1.set_xlabel(r't in s')
ax2.set_title('Ausgang Regler')
ax2.set_xlabel(r't in s')
ax3.set_title('Ausgänge Strecke')
ax3.set_xlabel(r't in s')
ax4.set_title('Abweichungen')
ax4.set_xlabel(r't in s')

ax1.grid(True)
ax2.grid(True)
ax3.grid(True)
ax4.grid(True)
ax1.legend(loc='upper right')
ax2.legend(loc='upper right')
ax3.legend(loc='upper right')
ax4.legend(loc='upper right')

fig2, (ax21, ax22) = plt.subplots(2,figsize=(10,5))
ax21.plot(tt, np.vectorize(cubic_jump)(tt, para.ts, para.dts, para.w0, para.w1), label='$u(t)$', lw=1, color='b')
ax21.plot(tt, np.vectorize(cubic_jump)(tt, para.tz, para.dtz, para.z0, para.z1), label='$z(t)$', lw=1, color='g')
ax22.plot(tt, u_p2, label='$u_{p2}(t)$', lw=1, color='b')
ax22.plot(tt, y_sh+y_p2, label='$x_K(t)$', lw=1, color='r')
ax21.grid(True)
ax22.grid(True)
ax21.legend()
ax22.legend()

plt.tight_layout()
plt.show()