def main():
    N, X, Y, Z = map(int, input().split())
    if X > Y:
        X, Y = Y, X
    print("Yes" if X < Z < Y else "No")

if __name__ == '__main__':
    main()
