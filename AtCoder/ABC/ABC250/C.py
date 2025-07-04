def main():
    N, Q = map(int, input().split())

    ball = [i for i in range(N)]
    pos = [i for i in range(N)]

    for _ in range(Q):
        x = int(input()) - 1
    
        posx = ball[x]
        posy = posx + 1 if posx + 1 < N else posx - 1
        y = pos[posy]

        ball[x], ball[y] = ball[y], ball[x]
        pos[posx], pos[posy] = pos[posy], pos[posx]
    
    pos = [i + 1 for i in pos]
    print(*pos)

if __name__ == '__main__':
    main()
