from collections import defaultdict
from collections import deque
import sys
sys.setrecursionlimit(10**6)

input = sys.stdin.readline

n,m = map(int,input().split())
maze = [input().strip() for _ in range(n)]
    
visited = [[False] * m for _ in range(n)]


def bfs ():
    visited [0][0] = True
    q = deque()
    q.append((0,0))

    dy = (-1,1,0,0)
    dx = (0,0,-1,1)
    
    while q:
        y,x = q.popleft()
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if not (0 <= nx < m and 0 <= ny < n):
                continue
            
            if maze[ny][nx] == "1" and visited[ny][nx] == False :
                visited[ny][nx] = visited[y][x] +1
                q.append((ny,nx))


bfs()
print(visited[n-1][m-1])