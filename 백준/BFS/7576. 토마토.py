# https://www.acmicpc.net/problem/7576

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

M, N = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
visited = [[-1] * M for _ in range(N)]

# pop(0) 로 하면 시간초과가 뜨기 때문에 선형큐를 사용
def enQ(x, y):
    global rear
    rear += 1
    q[rear] = (x, y)


def deQ():
    global front
    front += 1
    return q[front]


def bfs(q):
    global rear, front

    while rear != front: # rear == front : 큐가 비어있다는 뜻
        x, y = deQ()
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0 <= nx < N and 0 <= ny < M and arr[nx][ny] == 0 and visited[nx][ny] == -1:
                visited[nx][ny] = visited[x][y] + 1
                enQ(nx, ny)


def ready():
    for i in range(N):
        for j in range(M):
            if arr[i][j] == 1:
                enQ(i, j)
                visited[i][j] = 0
            elif arr[i][j] == -1:
                visited[i][j] = -2

rear = front = -1
q = [0] * (N * M)
ready()
# print(q)
bfs(q)
ans = 0
for i in range(N):
    for j in range(M):
        if visited[i][j] == -1:
            print(-1)
            exit()
        ans = max(ans, visited[i][j])
print(ans)
