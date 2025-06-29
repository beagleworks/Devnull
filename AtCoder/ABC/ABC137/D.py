# 最終日から見ていき、その時点で期限までに報酬が受け取れる仕事のうち最大の報酬を得る仕事を選んでいく
def main():
    import sys
    input = sys.stdin.readline
    import heapq

    N, M  = map(int, input().split())
    A = [tuple(map(int, input().split())) for _ in range(N)]
    heapq.heapify(A)

    B = []
    ans = 0
    for i in range(1, M + 1):
        while A and A[0][0] <= i:
            heapq.heappush(B, -heapq.heappop(A)[1])
        ans += -heapq.heappop(B) if B else 0

    print(ans)

if __name__ == '__main__':
    main()