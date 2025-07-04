def main():
    N = input()
    A, B, C, D = int(N[0]), int(N[1]), int(N[2]), int(N[3])
    op = ["+", "-"]
    for i in op:
        for j in op:
            for k in op:
                if eval(f"{A}{i}{B}{j}{C}{k}{D}") == 7:
                    print(f"{A}{i}{B}{j}{C}{k}{D}=7")
                    return
                
if __name__ == '__main__':
    main()