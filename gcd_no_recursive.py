def gcd(p,q):
    while q != 0:
        p,q = q, p % q
    return p

p = 35
q = 42
result = gcd(p,q)
print 'GCD of (%s, %s) is %s: ' % (p, q, result)

