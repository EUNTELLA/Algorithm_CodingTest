from collections import defaultdict
import sys
sys.setrecursionlimit(10**6)

input = sys.stdin.readline

N = int(input())
M = int(input())

adj_dic = defaultdict(list)

for _ in range(M):
    u,v = map(int,input().split())
    
    adj_dic[u].append(v)
    adj_dic[v].append(u)
    

visited = [False] * (N+1)
def dfs(node):
    stack = [node]
    visited[node] =True
    count = 0
    while stack:
        noded = stack.pop()
        for new in adj_dic[noded]:
            if not visited[new]:
                visited[new] =True
                count += 1
                stack.append(new)
    return count 

# for i in range(1,N+1):
#     if not visited[i]:
#         dfs(i)
        
print(dfs(1))
        
            
