def main():
    N = int(input())
    S = [input() for _ in range(N)]
    
    T = set()
    for i in range(N):
        for j in range(N):
            if i == j:
                continue
            T.add(S[i] + S[j])
    
    print(len(T))

if __name__ == '__main__':
    main()
