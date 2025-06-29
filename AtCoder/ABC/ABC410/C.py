import sys

def main():
    input = sys.stdin.readline
    N, Q = map(int, input().split())
    A = list(range(1, N + 1))
    T = 0

    for _ in range(Q):
        query = list(map(int, input().split()))
        query[0]
        if query[0] == 1:
            idx = (query[1] - 1 + T) % N
            A[idx] = query[2]
        elif query[0] == 2:
            idx = (query[1] - 1 + T) % N
            print(A[idx])
        else:
            T = (T + query[1]) % N

if __name__ == '__main__':
    main()