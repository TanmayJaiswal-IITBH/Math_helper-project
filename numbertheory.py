def is_prime(n):
    for i in range(2,int(n**0.5)+1):
        if  n%i==0:
            return False
        return True
def GCD(a,b):
    if b>a:
        a,b=b,a
    if a%b==0:
        return b
    else:
        return GCD(a,a%b)
def LCM(a,b):
    return abs(a*b)//GCD(a,b)
def prime_factors(n):
    i = 2
    factors = []
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.append(i)
    if n > 1:
        factors.append(n)
    return factors
    

        