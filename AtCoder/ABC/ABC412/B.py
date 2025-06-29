def main():
    S = input()
    T = input()

    for i in range(1, len(S)):
        if S[i].isupper():
            if S[i - 1] not in T:
                print("No")
                return

    print("Yes")

if __name__ == '__main__':
    main()