def main():
    H, W = map(int, input().split())
    Field = []
    P = []
    for i in range(H):
        S = input().rstrip()
        Field.append(S)
        for j in range(W):
            if S[j] == 'o': 
                P.append((i, j))
    
    print(abs(P[0][0] - P[1][0]) + abs(P[0][1] - P[1][1]))

if __name__ == '__main__':
    main()
