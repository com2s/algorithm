# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV7GKs06AU0DFAXB
# 백트래킹?
def queen(i,N):
    global cnt
    if i == N:
        cnt += 1
        return
    
    for j in range(N): # 퀸의 영역이 겹치는지 확인하고 둘 수 있을 때만 한다.
        if j in chess:
            continue
        flag = 1
        for k in range(i+1):
            if chess[i-k] == j-k or chess[i-k] == j+k:
                flag = 0
                break
        if flag:
            chess[i] = j
            queen(i+1,N)
            chess[i] = -1

T = int(input())

for tc in range(1,T+1):
    N = int(input())
    
    cnt = 0
    chess = [-1]*N # 사실 [0]*(N+1) 로 해도 상관없다. (인덱스를 1~N 으로 하는 방법)
    queen(0,N)
    print(f'#{tc} {cnt}')
