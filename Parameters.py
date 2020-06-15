class Parameters(object):
    pass

# Physical parameter
para = Parameters()  # instance of class Parameters
para.ts = 1         # define step time start
para.dts = 0.01         # define step time width
para.w0 = 0         # define level before step
para.w1 = 2         # define level after step
# LISTING_END ParaClass

# LISTING_START SimuPara
# Simulation parameter
sim_para = Parameters()  # instance of class Parameters
sim_para.t0 = 0          # start time
sim_para.tf = 10         # final time
sim_para.dt = 0.01       # step-size
sim_para.max_step = 0.01 # maximum step size for RK45
# LISTING_END SimuPara

# LISTING_START PT1-Glied
para_pt1 = Parameters()
para_pt1.T = 2
para_pt1.Kp = 0.1
# LISTING_END PT1-Glied

# LISTING_START D-Glied
para_d = Parameters()
para_d.Kd = 1
# LISTING_END PT1-Glied