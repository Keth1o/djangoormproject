from random import randint

def m1_func(p0, t0, b, t, p20):
    m = (p20 * (1 + b * 20)/(1 + b * t)) * randint(50, 200)
    m1 = m * ((1 - p0 * t0 * (1 + b * (t - 20))) / ((t + 273) * p20))
    return m1

def m2_func(m, pv20, b, t, p20, vv):
    m2 = m * ((1 - pv20 * (1 + b * (t - 20))) / (p20 * (1 + vv * (t - 20))))
    return m2