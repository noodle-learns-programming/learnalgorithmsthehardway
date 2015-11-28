
def gcd(p, q):
    print 'Input: ', p, q
    if q == 0:
        return p
    p,q = q, p % q
    return gcd(p, q)

p = 35 
q = 42
result = gcd(p, q)
print 'Greatest common divisor of (%d, %d) is %s' % (p, q, result)
