from challenge0 import generate_random

m = 81853448938945944
c = -1 # unknown
n = 9223372036854775783

s0 = 4501678582054734753
s1 = 4371244338968431602

def crack_unknown_increment(states, modulus, multiplier):
    increment = (states[1] - states[0]*multiplier) % modulus
    return modulus, multiplier, increment

if __name__ == "__main__" :
    n, m, c = crack_unknown_increment([s0, s1], n, m)
    print("increment : ",c)
    print("known s1 : ", s1)
    print("calculated s1 : ", generate_random(s0, m, c, n, 1)[1])
