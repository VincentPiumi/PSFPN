from challenge0 import generate_random
from challenge1 import crack_unknown_increment

s0 = 6473702802409947663
s1 = 6562621845583276653
s2 = 4483807506768649573

m = -1 # unknown
c = -1 # unknown
n = 9223372036854775783

def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, x, y = egcd(b % a, a)
        return (g, y - (b // a) * x, x)

def modinv(b, n):
    g, x, _ = egcd(b, n)
    if g == 1:
        return x % n
    
def crack_unknown_multiplier(states, modulus):
    multiplier = (states[2] - states[1]) * modinv(states[1] - states[0], modulus) % modulus
    return crack_unknown_increment(states, modulus, multiplier)

if __name__ == "__main__" :
    n, m, c = crack_unknown_multiplier([s0, s1, s2], n)
    print("multiplier : ", m)
    print("increment : ", c)
    print(generate_random(s0, m, c, n, 2))
