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