class WeightedDSU:
    """
    n 要素を管理する重み付き Union-Find（Disjoint Set Union）。
    各要素 x に対して parent[x] はその親を、weight[x] は
    x から parent[x] への重み差（ポテンシャル差）を表します。

    find(x):
        x の根を返しつつ、経路圧縮と重みの更新を行う。
    weight_of(x):
        根から見たときの x の累積重み（ポテンシャル）を返す。
    diff(x, y):
        x->y の重み差（weight_of(y) - weight_of(x)）を返す。
    unite(x, y, w):
        「y のポテンシャル - x のポテンシャル = w」 という制約を
        付けて集合をマージする。既に同じ集合内で矛盾があれば何もしない。

    How to use:
    # 5 要素 (0～4) を用意
        dsu = WeightedDSU(5)

        # 要素 0 と 1 を「1 のポテンシャル - 0 のポテンシャル = 10」という制約で結合
        dsu.unite(0, 1, 10)

        # 要素 1 と 2 を「2 のポテンシャル - 1 のポテンシャル = 5」で結合
        dsu.unite(1, 2, 5)

        # これで 0->2 の重み差は 15 (10+5)
        print(dsu.diff(0, 2))  # => 15

        # 逆向きは -15
        print(dsu.diff(2, 0))  # => -15

        # 同じ集合かどうかの判定
        print(dsu.find(0) == dsu.find(2))  # => True
        print(dsu.find(3) == dsu.find(4))  # => False

    """

    def __init__(self, n: int):
        self.n = n
        self.parent = list(range(n))
        self.rank = [0] * n
        self.weight = [0] * n

    def find(self, x: int) -> int:
        if self.parent[x] != x:
            root = self.find(self.parent[x])
            self.weight[x] += self.weight[self.parent[x]]
            self.parent[x] = root
        return self.parent[x]

    def weight_of(self, x: int) -> int:
        self.find(x)
        return self.weight[x]

    def diff(self, x: int, y: int) -> int:
        return self.weight_of(y) - self.weight_of(x)

    def unite(self, x: int, y: int, w: int) -> bool:
        rx = self.find(x)
        ry = self.find(y)
        if rx == ry:
            return False

        adjusted_w = w + self.weight[x] - self.weight[y]

        if self.rank[rx] < self.rank[ry]:
            self.parent[rx] = ry
            self.weight[rx] = -adjusted_w
        else:
            self.parent[ry] = rx
            self.weight[ry] = adjusted_w
            if self.rank[rx] == self.rank[ry]:
                self.rank[rx] += 1

        return True
