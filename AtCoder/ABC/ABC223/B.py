def main():
    S = input()
    
    ans1 = ans2 = S
    for _ in range(len(S)):
        S = S[1:] + S[0]
        if S < ans1:
            ans1 = S
        if S > ans2:
            ans2 = S
    
    print(ans1, ans2)

if __name__ == '__main__':
    main()

