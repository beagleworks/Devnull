def main():
    N, A, B = map(int, input().split())

    for i in range(A * N):
        line = ""
        for j in range(B * N):
            line += "." if ((i // A) % 2 + (j // B)) % 2 == 0 else "#"
        print(line)


if __name__ == '__main__':
    main()
