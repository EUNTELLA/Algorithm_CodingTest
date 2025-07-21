import sys
input = sys.stdin.readline

n = int(input())
top_h = list(map(int,input().split()))

stack = []
result = []


for i in range(n):
    
    current = top_h[i]
    
    while stack and stack[-1][1] < current:
        stack.pop()

    if stack:
        result.append(stack[-1][0])  
    else:
        result.append(0)

    stack.append((i + 1, current))  

print(' '.join(map(str,result)))