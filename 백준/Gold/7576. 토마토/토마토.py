from collections import deque

M, N = map(int, input().split())
tomato = [list(map(int, input().split())) for _ in range(N)]

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

q = deque()

for i in range(N):
    for j in range(M):
        if tomato[i][j] == 1:
            q.append((i, j))

while q:
    y, x = q.popleft()
    for k in range(4):
        ny, nx = y + dy[k], x + dx[k]
        
        if 0 <= ny < N and 0 <= nx < M and tomato[ny][nx] == 0:
            tomato[ny][nx] = tomato[y][x] + 1
            q.append((ny, nx))

        
max_day = 0
for row in tomato:
    for v in row:
        if v ==0:
            print(-1)
            exit()
        max_day = max(max_day,v)
        
print(max_day-1)