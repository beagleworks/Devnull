// PythonではO(HW^2)が間に合わない
#include <bits/stdc++.h>
using namespace std;
using ll = long long;
using VV = vector<vector<int>>;

void solve() {
    int H, W;
    cin >> H >> W;
    VV A(H, vector<int>(W));

    for (int i = 0; i < H; ++i) {
        string s;
        cin >> s;
        for (int j = 0; j < W; ++j) {
            A[i][j] = (s[j] == '#') ? 1 : -1;
        }
    }

    // 行数が列数を超えるときは転置
    if (H > W) {
        VV B(W, vector<int>(H));
        for (int i = 0; i < H; ++i)
            for (int j = 0; j < W; ++j)
                B[j][i] = A[i][j];
        A.swap(B);
        swap(H, W);
    }

    ll ans = 0;

    vector<int> freq(2 * H * W + 1);
    vector<int> used;
    used.reserve(W + 1);

    // 上端u, 下端dを全探索
    for (int u = 0; u < H; ++u) {
        vector<int> C(W, 0);
        for (int d = u; d < H; ++d) {
            // 各列の累積和を更新
            for (int j = 0; j < W; ++j) {
                C[j] += A[d][j];
            }

            // freq と used をリセット（計算量を抑えるため）
            used.clear();
            freq[H * W] = 1;
            used.push_back(H * W);

            ll prefix = 0;
            for (int j = 0; j < W; ++j) {
                prefix += C[j];
                int idx = int(prefix) + H * W;
                ans += freq[idx];
                if (freq[idx] == 0) {
                    used.push_back(idx);
                }
                freq[idx]++;
            }

            for (int idx : used) {
                freq[idx] = 0;
            }
        }
    }
    cout << ans << "\n";
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int T;
    cin >> T;
    while (T--) {
        solve();
    }
    return 0;
}

/*
def solve():
    import sys
    from collections import defaultdict
    input = sys.stdin.readline

    H, W = map(int, input().split())
    A = [[1 if c == '#' else -1 for c in input().rstrip()] for _ in range(H)]

    if H > W:
        A = list(map(list, zip(*A)))
        H, W = W, H

    ans = 0

    for u in range(H):
        C = [0] * W

        for d in range(u, H):
            for j in range(W):
                C[j] += A[d][j]

            pp = 0
            fq = defaultdict(int)
            fq[0] = 1

            for j in range(W):
                pp += C[j]
                ans += fq[pp]
                fq[pp] += 1
    
    print(ans)

def main():
    T = int(input())        
    for _ in range(T):
        solve()

if __name__ == "__main__":
    main()

*/