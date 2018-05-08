from sympy import *
import math

p = Symbol('p')
t = Symbol('t')
d = Symbol('d')



# QfとQb
qf = (10*log((p*(7-d))/6))/13 +(3*log(((1-p)*(5-t))/4))/ 13
qb = (2*log((p*(d-1))/6))/11 + (9*log(((1-p)*(t-1))/4) )/ 11

#Q
q = qf + qb

#偏微分
dp = diff(q,p)
dt = diff(q,t)
dd = diff(q,d)

print(dp)
print(dt)
print(dd)
