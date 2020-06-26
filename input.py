from Parameters import *

def cubic_jump(t, ts, dts, w0, w1):
    if(t<ts):
        return w0
    elif (t>ts+dts):
        return w1
    else:
        at3 = (-2*(w1-w0)*(t-ts)**3)/(dts**3)
        at2 = (3*(w1-w0)*(t-ts)**2)/(dts**2)
        at0 = w0
        return at3+at2+at0