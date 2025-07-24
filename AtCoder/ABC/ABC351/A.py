def main():
    A = sum(list(map(int, input().split())))
    B = sum(list(map(int, input().split())))
    print(A - B + 1)

if __name__ == '__main__':
    main()