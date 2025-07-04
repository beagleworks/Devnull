def main():
    N = int(input())
    L = [2, 1]
    for i in range(2, N + 1):
        L.append(L[-1] + L[-2])
    
    print(L[N])

if __name__ == '__main__':
    main()