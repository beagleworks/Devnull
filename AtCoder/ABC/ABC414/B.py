def main():
    N = int(input())
    ans = ""
    for _ in range(N):
        c, l = input().split()
        if len(ans) + int(l) > 100:
            print("Too Long")
            return
        
        ans += c * int(l)
    
    print(ans)

if __name__ == '__main__':
    main()
