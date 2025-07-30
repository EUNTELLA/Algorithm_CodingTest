from collections import deque

M, N, H = map(int, input().split())
tomato = [[list(map(int, input().split())) for _ in range(N)] for _ in range(H)]

dx = [1, -1, 0, 0, 0, 0]
dy = [0, 0, 0, 0, 1, -1]
dh = [0, 0, 1, -1, 0, 0]

q = deque()

for i in range(H):
    for j in range(N):
        for c in range(M): 
            if tomato[i][j][c] == 1:
                q.append((i, j, c ))



while q :
    h,y,x = q.popleft()
    for k in range(6):
        nh = h + dh[k]
        ny = y + dy[k]
        nx = x + dx[k]
        
        if 0 <= nh < H and 0<= ny < N and 0<= nx < M :
            if tomato[nh][ny][nx] == 0:
                tomato[nh][ny][nx] = tomato[h][y][x] + 1
                q.append(( nh, ny, nx))


   
max_day = 0
for h in range(H):
    for row in tomato[h]:
        if 0 in row:
            print(-1)
            exit()
            
        max_day = max(max_day,max(row))
        
print(max_day -1)