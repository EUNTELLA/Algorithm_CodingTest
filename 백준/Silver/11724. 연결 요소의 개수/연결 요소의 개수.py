from collections import defaultdict
import sys
sys.setrecursionlimit(10**6)

input = sys.stdin.readline

N, M = map(int, input().split())

adj_dic = defaultdict(list)

for _ in range(M):
    u,v = map(int,input().split())
    
    adj_dic[u].append(v)
    adj_dic[v].append(u)

visited = [False] * (N+1)
def dfs(node):
    stack = [node]
    visited[node] =True
    
    while stack:
        node = stack.pop()
        for new in adj_dic[node]:
            if not visited[new]:
                visited[new] =True
                stack.append(new)
            
count =0

for i in range(1,N+1):
    if not visited[i]:
        dfs(i)
        count +=1
            
print(count)