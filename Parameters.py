class Parameters(object):
    pass

# Physical parameter
para = Parameters()  # instance of class Parameters
para.ts = 1         # define step time start
para.dts = 0.01         # define step time width
para.w0 = 0         # define level before step
para.w1 = 0         # define level after step

para.tz = 1         # define step time start
para.dtz = 0.01         # define step time width
para.z0 = 0         # define level before step
para.z1 = 0         # define level after step
# LISTING_END ParaClass

# LISTING_START SimuPara
# Simulation parameter
sim_para = Parameters()  # instance of class Parameters
sim_para.t0 = 0          # start time
sim_para.tf = 20         # final time
sim_para.dt = 0.01       # step-size
sim_para.max_step = 0.01 # maximum step size for RK45
# LISTING_END SimuPara

"""
Hilfsgrößenregler
"""

# LISTING_START Strecke
para_p = Parameters()
para_p.Ta = 0.3
para_p.Tb = 0.4
para_p.K2 = 2
para_p.Tc = 1.0
para_p.Td = 2.0
# LISTING_END Strecke

# LISTING_START Regler
para_r = Parameters()
para_r.Kp = 0.803
para_r.Ti = 0.4
# LISTING_END Regler

# LISTING_START Kompensation
# para_sh = Parameters()
# para_sh.K = 1/para_r.Kp
# para_sh.T = para_r.Ti
# # LISTING_END Kompensation

# LISTING_START Kompensation
para_sh_hilfsg = Parameters()
para_sh_hilfsg.Kp = 6
para_sh_hilfsg.T = 2.33
# LISTING_END Kompensation


"""
Kaskadenregler
"""

# Physical parameter
para.tz1 = 1         # define step time start
para.dtz1 = 0.01         # define step time width
para.z01 = 0         # define level before step
para.z11 = 0         # define level after step

para.tz2 = 1         # define step time start
para.dtz2 = 0.01         # define step time width
para.z02 = 0         # define level before step
para.z12 = 0         # define level after step
# LISTING_END ParaClass


# LISTING_START Strecke
para_s = Parameters()
para_s.Ta = 0.3
para_s.Tb = 0.4
para_s.K2 = 2
para_s.Tc = 1.0
para_s.Td = 2.0
# LISTING_END Strecke

# LISTING_START Regler
para_rk = Parameters()
para_rk.Kp = 0.7
para_rk.Ti = 2.0
# LISTING_END Regler

# LISTING_START Kompensation
para_rh = Parameters()
para_rh.Kp = 1.2
para_rh.Ti = 2.0
# LISTING_END Kompensation