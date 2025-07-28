from collections import defaultdict
import sys
sys.setrecursionlimit(10**6)

input = sys.stdin.readline

T = int(input())

for _ in range(T):
    n,m = map(int,input().split())
    
    adj_dic = defaultdict(list)
    for _ in range(m):
        x,y = map(int,input().split())
        adj_dic[x].append(y)
        adj_dic[y].append(x)
        

    visited = [False] * (n+1)
    color = [-1] *(n+1)
    
    
    def dfs(node,c):
        color[node] = c
        visited[node] = True
        
        
        for neighbor in adj_dic[node]:
            if color[neighbor] == -1:
                if not dfs(neighbor, 1-c):
                    return False
            elif color[neighbor] ==c:
                 return False
        return True

    is_bipartite = True
    
    for i in range(1,n+1):
        if not visited[i]:
            if not dfs(i,0):
                is_bipartite = False
                break
    
    if is_bipartite:
        print("possible")
    else: 
        print("impossible")