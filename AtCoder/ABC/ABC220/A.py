def main():
    A, B, C = map(int, input().split())
    for i in range(1, 1001):
        if A <= C * i <= B:
            print(C * i)
            return

    print(-1)

if __name__ == '__main__':
    main()
