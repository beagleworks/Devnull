def main():
    K, X = map(int, input().split())
    print(*[i for i in range(X - K + 1, X + K) if -1000000 <= i <= 1000000])

if __name__ == '__main__':
    main()