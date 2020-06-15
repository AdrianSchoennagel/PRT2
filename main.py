import numpy as np
from numpy import cos, sin, tan
import matplotlib.pyplot as plt

from Parameters import *
import FunctionBlocks as FB
from input import *

tt = np.arange(sim_para.t0, sim_para.tf + sim_para.dt, sim_para.dt)

x0 = [0]

fig1, (ax1, ax2, ax3) = plt.subplots(3)

pt1 = FB.PT1_Block(para_pt1.Kp, para_pt1.T, x0)
d   = FB.D_Block(para_d.Kd)

x_traj = []
x_traj2 = []
y_out  = []
u_traj = []
for t in tt:
    u_cur = cubic_jump(t)
    u_traj.append(u_cur)

    y_pt1 = pt1.calc(u_cur, t, t + sim_para.dt)
    y_out = d.calc(u_cur)

    x_traj.append(y_pt1[0])
    x_traj2.append(y_out[0])

ax1.plot(tt, u_traj, label='$u(t)$', lw=1, color='b')
ax2.plot(tt, x_traj, label='$y_1(t)$', lw=1, color='r')
ax3.plot(tt, x_traj2, label='$y_1(t)$', lw=1, color='r')

ax1.set_title('Führungsverlauf')
ax1.set_ylabel(r'u(t)')
ax1.set_xlabel(r't in s')
ax2.set_title('Ausgang PT1')
ax2.set_ylabel(r'y_1(t)')
ax2.set_xlabel(r't in s')
ax3.set_title('Ausgang PT1+D')
ax3.set_ylabel(r'y_1(t)')
ax3.set_xlabel(r't in s')

ax1.grid(True)
ax2.grid(True)
ax3.grid(True)

plt.tight_layout()
plt.show()