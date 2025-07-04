'''
処理X : 2 つの整数を選んで，それらから 1 を引く
処理Y : すべての整数から 1 を引く

A < B < C とすると
処理Y を C 回行う 数は A-C(<0) B-C(<0) 0 
その後、C - A 回 + C - B 回 、処理 Y を行ったのではなく 処理 X を行ったことにすると、数は 0 0 0
C >= C - A + C - B であればこの操作は可能である
つまり A + B - C >= 0 であればよく A + B + C - 2 * max(A, B, C) >= 0 と書くことができる

'''

def main():
    A, B, C = map(int, input().split())
    mx = max(A, B, C)
    print(mx if (A + B + C) - 2 * mx >= 0 else -1)

if __name__ == '__main__':
    main()
