def main():
    S = input()
    for i in range(1, len(S) - 1):
        if S[i - 1] != S[i]:
            if S[i] != S[i + 1]:
                print(i + 1)
                return
            else:
                print(i - 1 + 1)
                return
    
    print(len(S))

if __name__ == '__main__':
    main()
