def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    print("Yes" if sum(A) <= M else "No")

if __name__ == '__main__':
    main()