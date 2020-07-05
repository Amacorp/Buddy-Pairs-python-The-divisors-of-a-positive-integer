
import math

def buddy(start, limit):
    def sum_divisor(n):
        return int(sum((val+num for val,num in ((mas, n/mas) for mas in range(1, int(math.sqrt(n)) + 1) if n % mas == 0 and mas != n / mas))) - n)

    for y in range(start, limit+1):
        sum1 = sum_divisor(y)
        if sum_divisor(sum1 - 1) == y + 1 and sum1 - 1 > y:
            return [y, sum_divisor(y) - 1]
    return 'Nothing'
    
    
or



def buddy(start, limit):
    for n in range(start, limit + 1):
        m = s(n)
        if m > n and n == s(m):
            return [n, m]
            
    return "Nothing"
    
def s(n):
    s = 0
    for i in range(2, round(n ** 0.5)):
        if n % i == 0:
            s += i
            s += n // i
    return s
    
    
    
or


from functools import reduce
def buddy(start, limit):
    for i in range(start, limit+1):
        dev = sorted(factors(i))[:-1]
        bud = sum(dev) - 1
        if bud > i:
            bud_dev = sorted(factors(bud))[:-1]
            if sum(bud_dev) - 1 == i:
                return [i, bud]
    return "Nothing"

def factors(n):
    return set(reduce(list.__add__,
                ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0)))
