import sys
from bisect import bisect_left, bisect_right

def main():
    data = sys.stdin.buffer.read().split()
    t = int(data[0]); pos = 1
    out = []
    for _ in range(t):
        n = int(data[pos]); pos += 1
        a = [0] + [int(x) for x in data[pos:pos + n]]
        pos += n
        P = [0] * (n + 1)
        for i in range(1, n + 1):
            P[i] = P[i - 1] ^ a[i]
        where = {}
        for k in range(n + 1):
            where.setdefault(P[k], []).append(k)
        # L[i]: previous index with a >= a[i] (0 if none)
        # R[i]: next index with a >  a[i] (n+1 if none)
        L = [0] * (n + 2)
        R = [n + 1] * (n + 2)
        st = []
        for i in range(1, n + 1):
            while st and a[st[-1]] < a[i]:
                R[st.pop()] = i
            L[i] = st[-1] if st else 0
            st.append(i)
        ans = 0
        for i in range(1, n + 1):
            v = a[i]
            # left prefix indices x in [L[i], i-1], right prefix indices y in [i, R[i]-1]
            lo1, hi1 = L[i], i - 1
            lo2, hi2 = i, R[i] - 1
            if hi1 - lo1 <= hi2 - lo2:
                for x in range(lo1, hi1 + 1):
                    lst = where.get(P[x] ^ v)
                    if lst:
                        ans += bisect_right(lst, hi2) - bisect_left(lst, lo2)
            else:
                for y in range(lo2, hi2 + 1):
                    lst = where.get(P[y] ^ v)
                    if lst:
                        ans += bisect_right(lst, hi1) - bisect_left(lst, lo1)
        out.append(ans)
    print("\n".join(map(str, out)))

main()
