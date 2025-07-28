from collections import defaultdict
import sys
sys.setrecursionlimit(10**6)

input = sys.stdin.readline

k = int(input())

for _ in range(k):
    V,E = map(int, input().split())
    
    adj_dic = defaultdict(list)
    
    for _ in range(E):
        u,v = map (int,input().split())
        adj_dic[u].append(v)
        adj_dic[v].append(u)


    visited = [False] * (V+1)
    color = [-1] *(V+1)

    def dfs(node,c):
        color[node] = c
        visited [node] = True
    
        for neighbor in adj_dic[node]:
            if color[neighbor] == -1:
                if not dfs(neighbor, 1- c):
                    return False
            elif color[neighbor] == c:
                return False
        return True

    is_bipartite = True
            
    for i in range(1, V+1):
        if not visited[i]:
            if not dfs(i,0):
                is_bipartite = False
                break
        
            
    if is_bipartite:
        print("YES")              
    else:
        print("NO")