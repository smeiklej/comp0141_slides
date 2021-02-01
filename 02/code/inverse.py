
import sys

def gcd(x, y):
    q = x / y
    r = x % y
    #print '{y}\t=\t{q}*{x}\t+\t{r}'.format(y=y, q=q, x=x, r=r)
    if r == 0:
        return y
    else:
        return gcd(y, r)

def eea(iters, r_prev, r_cur, s_prev, s_cur, t_prev, t_cur):
    q = r_prev / r_cur
    r = r_prev - q*r_cur
    s = s_prev - q*s_cur
    t = t_prev - q*t_cur
    print 'iteration', iters
    print '\tr = {r},\ts = {s},\tt = {t}'.format(r=r, s=s, t=t).expandtabs(5)
    if r == 0:
        return s_cur, t_cur
    else:
        return eea(iters+1, r_cur, r, s_cur, s, t_cur, t)

s0 = 1
s1 = 0
t0 = 0
t1 = 1

x = int(sys.argv[1])
y = int(sys.argv[2])
g = gcd(x, y)
if g == 1:
    a, b = eea(0, x, y, s0, s1, t0, t1)
    i = a % y
    print '\nThe inverse of {x} modulo {y} is {i}\n'.format(x=x, y=y, i=i)
else:
    print '\n{x} has no inverse modulo {y}'.format(x=x, y=y)
