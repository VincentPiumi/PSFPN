m = 672257317069504227   # the "multiplier"
c = 7382843889490547368  # the "increment"
n = 9223372036854775783  # the "modulus"
s0 = 2300417199649672133 # seed

s1 = (s0*m + c) % n
s2 = (s1*m + c) % n
s3 = (s2*m + c) % n
s4 = (s3*m + c) % n

def generate_random(seed, m, c, n, loop) :
    rand = [seed]
    for i in range(1, loop + 1) :
        if i == 1 :
            rand.append((seed*m + c) % n)
        else :
            rand.append((rand[i-1]*m + c) % n)
    return rand

if __name__ == "__main__" :
    print(generate_random(s0, m, c, n, 4))
