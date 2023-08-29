# https://www.acmicpc.net/problem/2615

arr = [list(map(int, input().split())) for _ in range(19)]

dx = [0, 1, 1, -1]
dy = [1, 0, 1, 1]

for i in range(19):
    for j in range(19):
        if arr[i][j] == 0:
            continue
        for k in range(4):
            cnt = 1   # 탐색 방향과 반대 방향에 같은 돌이 있다면 무시한다 (중복탐색을 막아서 6목을 방지하기 위해)
            if 0 <= i - dx[k] < 19 and 0 <= j - dy[k] < 19 and arr[i][j] == arr[i - dx[k]][j - dy[k]]:
                continue
            nx = i + dx[k]
            ny = j + dy[k]
            while 0 <= nx < 19 and 0 <= ny < 19 and arr[i][j] == arr[nx][ny]:
                cnt += 1
                nx += dx[k]
                ny += dy[k]
            if cnt == 5:
                print(arr[i][j])
                print(i + 1, j + 1)
                exit()

print(0)

#### 아래는 더 복잡하고 번거롭고 귀찮은 방법
#### 결국 끝까지 전부 탐색해야 하므로 비효율적
arr = [list(map(int, input().split())) for _ in range(19)]
visited = [[[0]*4 for i in range(19)] for _ in range(19)]
dx = [0, 1, 1, -1]
dy = [1, 0, 1, 1]
ans = []
for i in range(19):
    for j in range(19):
        if arr[i][j] == 0:
            continue
        for k in range(4):
            cnt = 1
            nx = i + dx[k]
            ny = j + dy[k]
            while 0 <= nx < 19 and 0 <= ny < 19 and arr[i][j] == arr[nx][ny] and visited[nx][ny][k] == 0:
                cnt += 1
                nx += dx[k]
                ny += dy[k]
            if cnt == 5:
                # print(arr[i][j])
                # print(i + 1, j + 1)
                # exit()
                ans.append((i,j,k))
            elif cnt > 5:
                for _ in range(cnt):
                    nx -= dx[k]
                    ny -= dy[k]
                    # print(nx,ny,k)
                    visited[nx][ny][k] = 1
# print(ans)
if ans:
    for a in ans:
        x,y,z = a
        if visited[x][y][z] == 0:
            print(arr[x][y])
            print(x + 1, y + 1)
            exit()

print(0)
