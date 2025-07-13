def main():
    A = list(map(int, input().split()))
    for i in range(7):
        for j in range(7):
            if A[i] == A[j]:
                continue
            if A.count(A[i]) >= 3 and A.count(A[j]) >= 2:
                print("Yes")
                return
    
    print("No")

if __name__ == '__main__':
    main()
