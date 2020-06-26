from abc import ABC,abstractmethod
import numpy as np
from numpy import cos, sin, tan
import scipy.integrate as sci

from Parameters import *
from input import *

class Solver:
    def __init__(self, tt):
        self.tt = tt
        self.state_start = [0, 0, 0, 0, 0]
        self.pt1 = PT1_Block(para_pt1.Kp, para_pt1.T)
        self.dt1 = DT1_Block(1, 1)
        self.pt2 = PT2_Block(1, 1, 1)
        self.pi  = PI_Block(1, 2)

    def ode(self, t, x, returnDxDt = True):
        u = cubic_jump(t)
        dxdt = np.concatenate((self.pt1.ode(x[0], u), self.dt1.ode(x[1], u), self.pt2.ode(x[2:4], u), self.pi.ode(x[4], u)))
        y    = np.concatenate((self.pt1.out(x[0], u), self.dt1.out(x[1], u), self.pt2.out(x[2:4], u), self.pi.out(x[4], u)))
        if returnDxDt:
            return dxdt
        else:
            return y

    def calc(self):
        solv = sci.solve_ivp(self.ode, (sim_para.t0, sim_para.tf), self.state_start, max_step=sim_para.max_step, t_eval=self.tt)
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
        return np.array([x])

class DT1_Block():
    def __init__(self, Kp, T1):
        self.Kp = Kp
        self.T1 = T1
        self.pt1 = PT1_Block(Kp, T1)

    def ode(self, x, u):
        return self.pt1.ode(x, u)

    def out(self, x, u):
        return self.pt1.ode(x, u)

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
        return np.array([x[0]])

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
        return np.array([x + self.Kp*u])