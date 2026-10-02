import sys

def main():
    data = sys.stdin.read().split()
    t = int(data[0]); pos = 1
    for _ in range(t):
        n = int(data[pos]); pos += 1
        a = list(map(int, data[pos:pos + n])); pos += n
        ans = 0
        for l in range(n):
            mx = 0; x = 0
            for r in range(l, n):
                mx = max(mx, a[r]); x ^= a[r]
                if mx == x:
                    ans += 1
        print(ans)

main()
