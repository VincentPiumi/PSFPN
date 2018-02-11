from challenge2 import egcd
from challenge2 import modinv
from challenge0 import generate_random
from challenge3 import crack_unknown_modulus

m = -1   # the "multiplier"
c = -1  # the "increment"
n = -1  # the "modulus"

s0 = 2818206783446335158
s1 = 3026581076925130250
s2 = 136214319011561377
s3 = 359019108775045580
s4 = 2386075359657550866
s5 = 1705259547463444505
s6 = 2102452637059633432

def recover_previous(n, m, c, value) : 
    return ((value - c) * modinv(m, n)) % n  
    
def recover_seed(n, m, c, value, idx) :
    seed = value
    if idx == 0 :
        print("index must be 1 or higher")
    else :
        for i in range(idx) :
            seed = recover_previous(n, m, c, seed)
            idx -= 1
    return seed
    

if __name__ == "__main__" :
    n, m, c = crack_unknown_modulus([s0, s1, s2, s3, s4, s5, s6])
    rando = generate_random(s0, m, c, n, 6)
    print(rando)

    print("current : ", s6)
    print("previous : ", recover_previous(n, m, c, s6))
    print("seed : ", recover_seed(n, m, c, s6, 6))

    # TEST SUR SEED-1 #
    # print("current : ", s0)
    # print("previous : ", recover_previous(n, m, c, s0))
    # seed_1 = recover_seed(n, m, c, s0, 1)
    # print("seed_1 : ", seed_1)

    # rando2 = generate_random(seed_1, m, c, n, 7)
    # print(rando2)
    
