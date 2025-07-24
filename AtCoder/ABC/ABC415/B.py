def main():
    S = input()

    tmp = 0
    for (i, s) in enumerate(S):        
        if s == '#':
            if not tmp:
                tmp = i + 1
            else:
                print(f"{tmp},{i + 1}")
                tmp = 0

if __name__ == '__main__':
    main()