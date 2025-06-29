# クエリ3は 当該時刻までのクエリ1の和 - 最後にクエリ2が起こった時刻までのクエリ1の和

def main():
    import sys
    input = sys.stdin.readline
    from atcoder.fenwicktree import FenwickTree

    N, M, Q = map(int, input().split())

    adds = []
    last = [0] * N
    val = [0] * N
    sums = [[]]
    ans = []
    J = []
    for _ in range(Q):
        query = list(map(int, input().split()))
        if query[0] == 1:
            l, r, x = query[1] - 1, query[2], query[3]
            adds.append((l, x))
            sums.append([])
            adds.append((r, -x))
            sums.append([])

        elif query[0] == 2:
            i, x = query[1] - 1, query[2]
            last[i] = len(adds)
            val[i] = x

        else:
            i, j = query[1] - 1, query[2] - 1
            ans.append(val[i])
            J.append(j)
            sums[last[i]].append((len(ans) - 1, -1))
            sums[len(adds)].append((len(ans) - 1, 1))
    
    d = FenwickTree(M + 1)
    for t in range(len(adds) + 1):
        for p in sums[t]:
            ai, c = p
            ans[ai] += d.sum(0, J[ai] + 1) * c
        
        if t == len(adds):
            break
        d.add(adds[t][0], adds[t][1])

    print(*ans)

if __name__ == '__main__':
    main()