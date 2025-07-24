def main():
    N = int(input())
    ans = [["#"] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if min(i, j, N - 1 - i, N - 1 - j) % 2 == 1:
                ans[i][j] = "."
    
    print("\n".join("".join(row) for row in ans))

if __name__ == '__main__':
    main()
