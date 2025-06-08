import sys
sys.setrecursionlimit(100000)

N = int(input())

dp = ["" for _ in range(N + 1)]
for n in range(1, N + 1):
    if set(str(n)) == {"1"}:
        dp[n] = "1" * len(str(n))
    else:
        dp[n] = None

for n in range(1, N + 1):

    for a in range(1, n):
        b = n - a
        ea, eb = dp[a], dp[b]
        if ea is None or eb is None:
            continue
        r = ea + "+" + eb
        if dp[n] is None or len(r) < len(dp[n]):
            dp[n] = r

    def mparts(n):
        res = []
        for a in range(2, n):
            if n % a == 0:
                b = n // a
                res.append([a, b])
                for e in mparts(b):
                    res.append([a] + e)
        return res

    for z in mparts(n):
        res = []
        f = True
        for v in z:
            e = dp[v]
            if e is None:
                f = False
                break

            if "+" in e:
                e = "(" + e + ")"
            res.append(e)

        if not f:
            continue
        r = "*".join(res)
        if dp[n] is None or len(r) < len(dp[n]):
            dp[n] = r

print(dp[N])
