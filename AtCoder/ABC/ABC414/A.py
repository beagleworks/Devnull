def main():
    N, L, R = map(int, input().split())
    ans = 0
    for _ in range(N):
        x, y = map(int, input().split())
        if x <= L and R <= y:
            ans += 1
        
    print(ans)

if __name__ == '__main__':
    main()
