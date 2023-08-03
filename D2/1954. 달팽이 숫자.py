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

#### 위에서 나누었던 경우의 수들을 모아 좀 더 짧게 정리

T = int(input())

for test_case in range(1, T + 1):
    N = int(input())
    arr = [[0] * N for _ in range(N)]

    delta = [[0, 1], [1, 0], [0, -1], [-1, 0]] # 좀 더 정리하긴했는데 이게 델타함수의 활용법이 맞는지는 모르겠습니다..
    n, i, j, k = 1, 0, -1, 0                     # 어쨌거나 4가지로 나뉘어있던 갈래들이 하나로 깔끔하게 처리된 것으로 보입니다.
    while n <= N * N:
        ni, nj = i + delta[k][0], j + delta[k][1]
        
        if ni < 0 or ni >= N or nj < 0 or nj >= N or arr[ni][nj] != 0: # 칸을 벗어나거나 중복으로 값을 적지 않도록 설정
            k = (k + 1) % 4
            continue

        i,j = ni, nj
        arr[i][j] = n
        n += 1

    print(f'#{test_case}')
    for i in range(N):
        print(*arr[i])
