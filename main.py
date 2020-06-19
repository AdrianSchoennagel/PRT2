import numpy as np
from numpy import cos, sin, tan
import matplotlib.pyplot as plt

from Parameters import *
import FunctionBlocks as FB
from input import *

tt = np.arange(sim_para.t0, sim_para.tf + sim_para.dt, sim_para.dt)

x0 = [0]

fig1, (ax1, ax2, ax3, ax4) = plt.subplots(4)

pt1 = FB.PT1_Block(para_pt1.Kp, para_pt1.T, x0)
d   = FB.D_Block(para_d.Kd)
dt1 = FB.DT1_Block(1, 1, x0)
pt2 = FB.PT2_Block(1, 1, 1, x0)
pi  = FB.PI_Block(1, 2, x0)

x_traj = []
x_traj2 = []
x_traj3 = []
y_out  = []
u_traj = []
for t in tt:
    u_cur = cubic_jump(t)
    u_traj.append(u_cur)

    y_dt1 = dt1.calc(u_cur, t, t + sim_para.dt)
    y_pt2 = pt2.calc(u_cur, t, t + sim_para.dt)
    y_pi  = pi.calc(u_cur, t, t + sim_para.dt)

    x_traj.append(y_dt1[0])
    x_traj2.append(y_pt2[0])
    x_traj3.append(y_pi[0])

ax1.plot(tt, u_traj, label='$u(t)$', lw=1, color='b')
ax2.plot(tt, x_traj, label='$y_dt1(t)$', lw=1, color='r')
ax3.plot(tt, x_traj2, label='$y_pt2(t)$', lw=1, color='r')
ax4.plot(tt, x_traj3, label='$y_pi(t)$', lw=1, color='r')

ax1.set_title('Führungsverlauf')
ax1.set_ylabel(r'u(t)')
ax1.set_xlabel(r't in s')
ax2.set_title('Ausgang DT1')
ax2.set_ylabel(r'y_1(t)')
ax2.set_xlabel(r't in s')
ax3.set_title('Ausgang PT2')
ax3.set_ylabel(r'y_1(t)')
ax3.set_xlabel(r't in s')
ax4.set_title('Ausgang PI')
ax4.set_ylabel(r'y_1(t)')
ax4.set_xlabel(r't in s')

ax1.grid(True)
ax2.grid(True)
ax3.grid(True)
ax4.grid(True)

plt.tight_layout()
plt.show()