import math

N = int(input())
k = 1

while True:
    k3 = k * k * k

    if k3 > 4 * N:
        break

    Dy = 3 * k * (4 * N - k3)
    sqDy = math.isqrt(Dy)

    if sqDy * sqDy == Dy:
        numery = -3 * k * k + sqDy
        denomy = 6 * k

        if numery >= 0 and numery % denomy == 0:
            y = numery // denomy
            if y > 0:
                x = y + k
                print(x, y)
                exit()

    if k > 2 * (10 ** 6):
        break

    k += 1

print(-1)
