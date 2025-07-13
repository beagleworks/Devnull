def main():
    N = int(input())
    if N % 5 == 0:
        print(N)
    else:
        X = N + 5 - N % 5
        Y = N - N % 5
        print(X if abs(X - N) < abs(Y - N) else Y)

if __name__ == '__main__':
    main()
