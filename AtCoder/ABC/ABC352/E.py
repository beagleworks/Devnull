# クラスカル法的な感じ
# 重さが小さい順に辺を追加するだけ
# DSUにより、各部分集合に関して1頂点からの辺だけを追加するだけで十分
def main():
    from atcoder.dsu import DSU

    N, M = map(int, input().split())
    E = []
    for _ in range(M):
        K, C = map(int, input().split())
        A = list(map(int, input().split()))
        E.append((C, K, A))
    
    E.sort()
    dsu = DSU(N + 1)
    weight = 0

    for c, k, a in E:
        for i in range(1, k):
            if not dsu.same(a[0], a[i]):
                dsu.merge(a[0], a[i])
                weight += c

    print(weight if len(dsu.groups()) == 2 else -1)

if __name__ == '__main__':
    main()
