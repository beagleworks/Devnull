def main():
    p, q = input().split()
    if p > q:
        p, q = q, p
    
    p = ord(p) - ord('A')
    q = ord(q) - ord('A')
    L = [3, 1, 4, 1, 5, 9]

    ans = sum(L[p : q])
    print(ans)

if __name__ == '__main__':
    main()