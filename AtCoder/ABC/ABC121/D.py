# 0からA までの XOR は周期性があり、fxのように定義できる
# また、fx(A, B) = fx(0, B) ^ fx(0, A - 1)
def main():
    A, B = map(int, input().split())
    
    def fx(n):
        if n % 4 == 0:
            return n
        elif n % 4 == 1:
            return 1
        elif n % 4 == 2:
            return n + 1
        # 3:
        else:
            return 0
    
    print(fx(B) ^ fx(A - 1))
    

if __name__ == '__main__':
    main()