def main():
    from collections import deque
    
    Q = int(input())
    dq = deque()
    cnt = 0
    keep = 0
    for _ in range(Q):
        q = list(map(int, input().split()))
        if q[0] == 1:
            c = q[1]
            x = q[2]
            dq.append((c, x))
        
        else:
            k = q[1]
            ans = 0
            while k > 0:
                xx, yy = 0, 0
                if cnt:
                    xx = cnt
                    yy = keep
                    cnt = 0
                    keep = 0
                else:
                    xx, yy = dq.popleft()
                if xx <= k:
                    ans += xx * yy
                    k -= xx
                else:
                    ans += k * yy
                    cnt = xx - k
                    keep = yy
                    break
            print(ans) 

if __name__ == '__main__':
    main()