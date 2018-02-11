from challenge0 import generate_random
from challenge1 import crack_unknown_increment
from challenge2 import crack_unknown_multiplier
from functools import reduce
from fractions import gcd

m = -1 # unknown
c = -1 # unknown
n = -1 # unknown

s0 = 2818206783446335158
s1 = 3026581076925130250
s2 = 136214319011561377
s3 = 359019108775045580
s4 = 2386075359657550866
s5 = 1705259547463444505
s6 = 2102452637059633432

def crack_unknown_modulus(states):
    diffs = [s1 - s0 for s0, s1 in zip(states, states[1:])]
    zeroes = [t2*t0 - t1*t1 for t0, t1, t2 in zip(diffs, diffs[1:], diffs[2:])]
    modulus = abs(reduce(gcd, zeroes))
    return crack_unknown_multiplier(states, modulus)

if __name__ == "__main__" :
    n, m, c = crack_unknown_modulus([s0, s1, s2, s3, s4, s5, s6])
    print("multiplier : ", m)
    print("increment : ", c)
    print("modulus : ", n)
    print(generate_random(s0, m, c, n, 6))
    
