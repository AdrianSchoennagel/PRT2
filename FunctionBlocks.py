from abc import ABC,abstractmethod
import numpy as np
from numpy import cos, sin, tan
import scipy.integrate as sci

from Parameters import *
from input import *

class Solver:
    def __init__(self, tt):
        self.tt = tt
        self.state_start = [0, 0, 0, 0, 0, 0]
        self.p1 = PT2_Block(1, para_p.Ta, para_p.Tb)
        self.p2 = PT2_Block(para_p.K2, para_p.Tc, para_p.Td)
        self.sh = DT1_Block(para_sh.K, para_sh.T)
        self.r  = PI_Block(para_r.Ti, para_r.Kp)

    def ode(self, t, x, returnDxDt = True):
        w = cubic_jump(t, para.ts, para.dts, para.w0, para.w1)
        z = cubic_jump(t, para.tz, para.dtz, para.z0, para.z1)

        y_p1 = self.p1.out(x[1:3], 0)
        u_sh = y_p1 #+ z
        dxdt_sh = self.sh.ode(x[5], u_sh)
        y_sh = self.sh.out(x[5], u_sh)
        u_p2 = y_p1 #+ z
        dxdt_p2 = self.p2.ode(x[3:5], u_p2)
        y_p2 = self.p2.out(x[3:5], u_p2)
        u_r = w - (y_sh + y_p2)
        dxdt_r = self.r.ode(x[0], u_r)
        y_r = self.r.out(x[0], u_r)
        dxdt_p1 = self.p1.ode(x[1:3], y_r)

        if returnDxDt:
            dxdt = np.concatenate((dxdt_r, dxdt_p1, dxdt_p2, dxdt_sh))
            return dxdt
        else:
            y    = np.array([y_r, y_p1, y_p2, y_sh, u_r, w-y_p2])
            return y

    def calc(self):
        solv = sci.solve_ivp(self.ode, (sim_para.t0, sim_para.tf + sim_para.dt), self.state_start, max_step=sim_para.max_step, t_eval=self.tt)
        ys = None
        for i in range(0, len(self.tt)):
            y = self.ode(self.tt[i], solv.y.T[i], False)
            if ys is None:
                ys = [y]
            else:
                ys = np.append(ys, [y], axis=0)
        return ys.T



class PT1_Block():
    def __init__(self, Kp, T, state_sv = 0):
        self.state_sv = state_sv
        self.Kp = Kp
        self.T = T

    def ode(self, x, u):
        dxdt = np.array([(self.Kp * u - x) / self.T])
        return dxdt

    def out(self, x, u):
        return x

class DT1_Block():
    def __init__(self, Kp, T1):
        self.Kp = Kp
        self.T1 = T1
        self.pt1 = PT1_Block(Kp, T1)

    def ode(self, x, u):
        return self.pt1.ode(x, u)

    def out(self, x, u):
        return self.pt1.ode(x, u)[0]

class PT2_Block():
    def __init__(self, Kp, T1, T2):
        self.Kp = Kp
        self.T1 = T1
        self.T2 = T2

    def ode(self, x, u):
        dxdt0 = x[1]
        dxdt1 = -x[0]/(self.T1 * self.T2) - x[1]*(self.T1 + self.T2)/(self.T1 * self.T2) + u*self.Kp/(self.T1*self.T2)
        return np.array([dxdt0, dxdt1])

    def out(self, x, u):
        return x[0]

class I_Block():
    def __init__(self, Ki):
        self.Ki = Ki

    def ode(self, x, u):
        dxdt = np.array([self.Ki*u])
        return dxdt

    def out(self, x, u):
        return x

class PI_Block():
    def __init__(self, Ki, Kp):
        self.Ki = Ki
        self.Kp = Kp

    def ode(self, x, u):
        dxdt = np.array([self.Ki*u])
        return dxdt

    def out(self, x, u):
        return x + self.Kp*u