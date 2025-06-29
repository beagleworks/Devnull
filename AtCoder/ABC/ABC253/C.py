def main():
    import sys
    input = sys.stdin.readline
    from sortedcontainers import SortedList

    Q = int(input())
    SL = SortedList()
    for _ in range(Q):
        query = list(map(int, input().split()))
        if query[0] == 1:
            SL.add(query[1])
        elif query[0] == 2:
            for _ in range(min(query[2], SL.count(query[1]))):
                SL.discard(query[1])
        else:
            print(SL[-1] - SL[0])

if __name__ == '__main__':
    main()