# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV5PobmqAPoDFAUq&categoryId=AV5PobmqAPoDFAUq&categoryType=CODE&problemTitle=&orderBy=FIRST_REG_DATETIME&selectCodeLang=ALL&select-1=&pageSize=10&pageIndex=1
# 나중에 더 간단한 풀이 찾아볼 것

T = int(input())

for test_case in range(1, T + 1):
    N = int(input())
    arr = [[0] * N for _ in range(N)]

    a, b, c, d = 1, 0, 0, 0
    n, i, j = 1, 0, 0
    while n <= N * N:
        if a:
            arr[i][j] = n
            n += 1
            if j == N - i - 1:
                a, b = 0, 1
                i += 1
                continue

            j += 1

        elif b:
            arr[i][j] = n
            n += 1
            if i == j:
                b, c = 0, 1
                j -= 1
                continue

            i += 1

        elif c:
            arr[i][j] = n
            n += 1
            if j == N - i - 1:
                c, d = 0, 1
                i -= 1
                continue

            j -= 1

        elif d:
            arr[i][j] = n
            n += 1
            if i == j + 1:
                d, a = 0, 1
                j += 1
                continue

            i -= 1

    print(f'#{test_case}')
    for i in range(N):
        print(*arr[i])
