from Parameters import *

def cubic_jump(t):
    if(t<para.ts):
        return para.w0
    elif (t>para.ts+para.dts):
        return para.w1
    else:
        at3 = (-2*(para.w1-para.w0)*(t-para.ts)**3)/(para.dts**3)
        at2 = (3*(para.w1-para.w0)*(t-para.ts)**2)/(para.dts**2)
        at0 = para.w0
        return at3+at2+at0