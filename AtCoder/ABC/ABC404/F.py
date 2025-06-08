N, T, M, K = map(int, input().split())

dpn = [0.0] * (K + 1)
for s in range(K + 1):
    dpn[s] = 1.0 if s >= K else 0.0

if N >= M:
    for _ in range(T):
        dpc = [0.0] * (K + 1)
        dpc[K] = 1.0

        for s in range(K - 1, -1, -1):
            base = dpn[s]
            b = [0.0] * (M + 1)

            for u in range(1, M + 1):
                idx = s + u
                if idx > K:
                    idx = K
                b[u] = dpn[idx] - base

            f = [0.0] + [float('-inf')] * M

            for x in range(1, M + 1):
                tmp = float('-inf')

                for u in range(1, x + 1):
                    v = f[x - u] + b[u]
                    if v > tmp:
                        tmp = v

                f[x] = tmp

            grt = f[M]
            dpc[s] = base + grt / N
        dpn = dpc

else:
    max_cnt = min(N, M)
    for _ in range(T):
        dpc = [0.0] * (K + 1)
        dpc[K] = 1.0

        for s in range(K - 1, -1, -1):
            base = dpn[s]
            b = [0.0] * (M + 1)

            for u in range(1, M + 1):
                idx = s + u
                if idx > K:
                    idx = K
                b[u] = dpn[idx] - base

            f2 = [[float('-inf')] * (max_cnt + 1) for _ in range(M + 1)]
            f2[0][0] = 0.0

            for x in range(M + 1):
                for cnt in range(max_cnt + 1):
                    v = f2[x][cnt]
                    if v < 0.0:
                        continue
                    if x == M or cnt == max_cnt:
                        continue

                    for u in range(1, M - x + 1):
                        w = v + b[u]
                        if w > f2[x + u][cnt + 1]:
                            f2[x + u][cnt + 1] = w

            grt = 0.0
            for cnt in range(max_cnt + 1):
                if f2[M][cnt] > grt:
                    grt = f2[M][cnt]
            dpc[s] = base + grt / N
        dpn = dpc

print("{:.10f}".format(dpn[0]))
