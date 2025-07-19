import sys
from collections import deque

input = sys.stdin.readline
#보드 크기 입력
n = int(input())


k = int(input())
apple =[]
snake_info = dict()
for _ in range(k):
    apple.append(list(map(int,input().split())))
    
L = int(input())
for _ in range(L):
    sn_sec, sn_ld = input().strip().split()
    snake_info[int(sn_sec)]=sn_ld

time = 0
dir = 0  # 시작 방향: 오른쪽
snake = deque()
snake.append((0, 0))  # 시작 위치
board = [[0]*n for _ in range(n)]  # 0 = 빈칸

for x,y in apple:
    board[x-1][y-1] =1 # 사과 있는 곳
    
while True:
    time += 1
    head_x, head_y = snake[-1]
    
    dx = [0,1,0,-1 ]
    dy = [1,0,-1,0]
    nx = head_x + dx[dir]
    ny = head_y + dy[dir]

    if not(0 <= nx < n and 0<= ny < n) or (nx, ny) in snake:
        break
        
    snake.append((nx, ny))

    if board[nx][ny] == 1:  # 사과 있음
        board[nx][ny] = 0
    else:  # 사과 없음 → 꼬리 자름
        snake.popleft()

    if time in snake_info:
        if snake_info[time] == 'D':
            dir = (dir + 1) % 4
        else:
            dir = (dir - 1) % 4
            
# print(apple)
# print(snake_info)

print(time)