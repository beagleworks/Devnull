def main():
    S = input()
    T = input()
    
    cnt = 0
    for i in range(len(T)):
        if T[i] == S[cnt]:
            print(i + 1)
            cnt += 1


if __name__ == '__main__':
    main()
