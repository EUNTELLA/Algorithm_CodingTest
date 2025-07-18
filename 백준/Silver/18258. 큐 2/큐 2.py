import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
q = deque()

for _ in range(n):
    command = input().strip().split()
    
    if command[0] == "push":
        q.append(command[1])
    elif command[0] == "pop":
        if q :
            print(q.popleft())
        else:
            print(-1)
    elif command[0] == "size":
            print(len(q))
    elif command[0] == "empty":
        print(0 if q else 1)
    elif command[0] == "front":
        if not q: 
            print(-1)
        else:
            print(q[0])
    elif command[0] == "back":
        if not q:
            print(-1)
        else:
            print(q[-1]) 
    