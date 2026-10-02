import random, sys

# usage: python generator.py <seed> <mode> [n] [maxv]
# modes: rand, small, equal, inc, dec, pow2, balanced, ...
def gen_case(mode, n, maxv, rng):
    if mode == "rand":
        return [rng.randint(0, maxv) for _ in range(n)]
    if mode == "equal":
        v = rng.randint(0, maxv)
        return [v] * n
    if mode == "inc":
        return sorted(rng.randint(0, maxv) for _ in range(n))
    if mode == "dec":
        return sorted((rng.randint(0, maxv) for _ in range(n)), reverse=True)
    if mode == "balanced":  # ruler-like sequence -> balanced Cartesian tree (worst case for split sizes)
        return [min((((i + 1) & -(i + 1)).bit_length() - 1), 29) for i in range(n)]
    if mode == "pow2":
        return [1 << rng.randint(0, 29) for _ in range(n)]
    raise ValueError(mode)

if __name__ == "__main__":
    seed = int(sys.argv[1]); mode = sys.argv[2]
    n = int(sys.argv[3]) if len(sys.argv) > 3 else 8
    maxv = int(sys.argv[4]) if len(sys.argv) > 4 else 7
    rng = random.Random(seed)
    print(1); print(n); print(*gen_case(mode, n, maxv, rng))
