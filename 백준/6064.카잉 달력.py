# https://www.acmicpc.net/problem/6064
# 실행시간 : 392ms
T = int(input())

for tc in range(1, T + 1):
    M, N, x, y = map(int, input().split()) # M과 N중 더 큰 것을 찾게 했으나 실행시간에 큰 차이 없음
                                           # 그냥 M으로 때려넣었을 때는 실행시간 : 408ms 
    if N>M:
        M,N,x,y=N,M,y,x

    if N==y:
        y = 0

    i = x
    check = 0
    while i <= M * N:

        if i%N-y:
            i += M
            continue

        check = 1
        break

    if check:
        print(i)
    else:
        print(-1)
