def main():
    H, W = map(int, input().split())
    R, C = map(int, input().split())
    R -= 1
    C -= 1
    print(4 - (R == 0) - (R == H - 1) - (C == 0) - (C == W - 1))


if __name__ == '__main__':
    main()
