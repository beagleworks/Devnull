def main():
    N = int(input())
    S = "=" if N % 2 else "=="
    T = '-' * (N // 2) if N % 2 else '-' * ((N - 2) // 2)
    print(T + S + T) 

if __name__ == '__main__':
    main()
