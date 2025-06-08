import sys
input = sys.stdin.readline

Q = int(input())

xcc = [{}]
xpse = [False]

ycc = [{}]
yg = [0]
ybb = [False]

cnt = 0
res = []

for _ in range(Q):
    line = input().split()
    t, s = line[0], line[1]

    if t == '1':
        cur = 0

        for c in s:
            nxt = xcc[cur].get(c)
            if nxt is None:
                nxt = len(xcc)
                xcc[cur][c] = nxt
                xcc.append({})
                xpse.append(False)

            cur = nxt

        xpse[cur] = True

        cur_y = 0
        f = False
        path = []

        for c in s:
            if ybb[cur_y]:
                f = True
                break

            nxt = ycc[cur_y].get(c)
            if nxt is None:
                cur_y = None
                break

            cur_y = nxt
            path.append(cur_y)

        if cur_y is not None and not f and not ybb[cur_y]:
            g = yg[cur_y]
            if g:
                cnt -= g
                for node in path:
                    yg[node] -= g
            ybb[cur_y] = True

    else:
        cur = 0
        f = True
        for c in s:
            if xpse[cur]:
                f = False
                break

            nxt = xcc[cur].get(c)
            if nxt is None:
                cur = None
                break
            cur = nxt

        if f and cur is not None and xpse[cur]:
            f = False

        cur_y = 0
        path = []
        for c in s:
            nxt = ycc[cur_y].get(c)
            if nxt is None:
                nxt = len(ycc)
                ycc[cur_y][c] = nxt
                ycc.append({})
                yg.append(0)
                ybb.append(False)
            cur_y = nxt
            path.append(cur_y)

        if f:
            cnt += 1
            for node in path:
                yg[node] += 1

    res.append(str(cnt))

print('\n'.join(res))
