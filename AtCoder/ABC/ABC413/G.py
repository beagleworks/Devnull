# 障害物が左上から右下に向かって連続している場合、到達不可能である
# 左、もしくは上の壁に接触している障害物から、右、もしくは下の壁に接触している障害物に到達可能であれば、答えはNoとなる

def main():
    from collections import deque
    from collections import defaultdict

    H, W, K = map(int, input().split())
    RC = [tuple(int(x) - 1 for x in input().split()) for _ in range(K)]
    P = defaultdict(lambda: -1)
    for i, t in enumerate(RC):
        P[t] = i
    
    dr = [-1, -1, 0, 1, 1, 1, 0, -1]
    dc = [0, 1, 1, 1, 0, -1, -1, -1]

    visited = [False] * K
    q = deque()

    for t in RC:
        if t[0] == 0 or t[1] == W - 1:
            q.append(t)
            visited[P[t]] = True
    
    while q:
        r, c = q.popleft()
        for i in range(8):
            rr, cc = r + dr[i], c + dc[i]
            if 0 <= rr < H and 0 <= cc < W:
                if P[(rr, cc)] >= 0:
                    if not visited[P[(rr, cc)]]:
                        visited[P[(rr, cc)]] = True
                        q.append((rr, cc))
    
    for t in RC:
        if visited[P[t]]:
            if t[0] == H - 1 or t[1] == 0:
                print("No")
                return
    
    print("Yes")


if __name__ == '__main__':
    main()
