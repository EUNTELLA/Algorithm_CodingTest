import sys
input = sys.stdin.readline

n = int(input())
stack = []



for i in range(n):
    command = input().split()
    
    
    if command[0] == "push":
        stack.append(command[1])
    elif command[0] == "pop":
        if stack:
            print(stack.pop())
        else:
            print(-1)
    elif command[0] == "size":
        print(len(stack))
    elif command[0] == "empty":
        print(0 if stack else 1)
    elif command [0] == "top":
        if not stack:
            print(-1)
        else:
            print(stack[-1])