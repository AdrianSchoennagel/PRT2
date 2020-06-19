from abc import ABC,abstractmethod
import numpy as np
from numpy import cos, sin, tan
import scipy.integrate as sci

from Parameters import *

class Abstract_Block(ABC):
    def __init__(self, state_sv):
        self.state_sv = state_sv

    @abstractmethod
    def ode(self, t, x, u):
        pass

    def calc(self, u, t0, t1):
        solv = sci.solve_ivp(self.ode, (t0, t1), self.state_sv, args=(u,), max_step=sim_para.max_step)
        self.state_sv = solv.y.T[1]
        return solv.y.T[0]

class D_Block():
    def __init__(self, Kd, u_init = None):
        self.Kd = Kd
        self.u_past = u_init

    def calc(self, u):
        if self.u_past is None:
            self.u_past = u
        du = np.gradient([self.u_past, u], sim_para.dt)
        self.u_past = u
        return du * self.Kd


class PT1_Block(Abstract_Block):
    def __init__(self, Kp, T, state_sv):
        super().__init__(state_sv)
        self.Kp = Kp
        self.T = T

    def ode(self, t, x, u):
        dxdt = np.array([(self.Kp * u - x) / self.T])
        return dxdt

class DT1_Block():
    def __init__(self, Kp, T1, state_sv = 0):
        self.Kp = Kp
        self.T1 = T1
        self.pt1 = PT1_Block(Kp, T1, state_sv)
        self.d = D_Block(1)

    def calc(self, u, t0, t1):
        y_pt1 = self.pt1.calc(u, t0, t1)
        y_out = self.d.calc(y_pt1[0])
        return y_out

class PT2_Block():
    def __init__(self, Kp, T1, T2, state_sv = 0):
        self.Kp = Kp
        self.T1 = T1
        self.T2 = T2
        self.pt1_1 = PT1_Block(Kp, T1, state_sv)
        self.pt1_2 = PT1_Block(1, T2, state_sv)

    def calc(self, u, t0, t1):
        y_pt1 = self.pt1_1.calc(u, t0, t1)
        y_out = self.pt1_2.calc(y_pt1[0], t0, t1)
        return y_out

class I_Block(Abstract_Block):
    def __init__(self, Ki, state_sv):
        super().__init__(state_sv)
        self.Ki = Ki

    def ode(self, t, x, u):
        dxdt = np.array([self.Ki*u])
        return dxdt

class PI_Block:
    def __init__(self, Ki, Kp, state_sv = 0):
        self.Ki = Ki
        self.Kp = Kp
        self.i = I_Block(Ki, state_sv)

    def calc(self, u, t0, t1):
        y_i = self.i.calc(u, t0, t1)
        y_out = y_i + self.Kp*u
        return y_out
