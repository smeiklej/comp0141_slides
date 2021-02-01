
import sys

def gcd(x, y):
    q = x / y
    r = x % y
    print '{x}\t=\t{q}*{y}\t+\t{r}'.format(y=y, q=q, x=x, r=r).expandtabs(6)
    if r == 0:
        return y
    else:
        return gcd(y, r)

x = int(sys.argv[1])
y = int(sys.argv[2])
print '\nThe gcd of {x} and {y} is {gcd}\n'.format(x=x, y=y, gcd=gcd(x, y))

