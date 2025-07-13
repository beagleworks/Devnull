# 辺(a, b) と 辺(c, d)が並行なら a + b == c + d (mod N)
# すべての辺の組み合わせから平行な組み合わせを引くと答え
def main():
    import sys
    input = sys.stdin.readline
    
    N, M = map(int, input().split())
    F = [0] * N
    for _ in range(M):
        a, b = map(int, input().split())
        F[(a + b) % N] += 1
    
    cur = 0
    for f in F:
        cur += f * (f - 1) // 2
    
    print(M * (M - 1) // 2 - cur)

if __name__ == '__main__':
    main()
