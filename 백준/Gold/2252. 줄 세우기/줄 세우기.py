from collections import deque

n,m = map(int, input().split())

indegree = [0] * (n+1)

graph = [[] for _ in range(n+1)]

for _ in range(m):
    a,b = map(int,input().split())
    graph[a].append(b)
    indegree[b] += 1
    
def sort_bfs(v,graph, indegree):
    result = []
    q = deque([i for i in range(1,n+1) if indegree[i] == 0])
    
    while q:
        cur = q.popleft()
        result.append(cur)
        
        for nxt in graph[cur]:
            indegree[nxt] -= 1
            
            if indegree[nxt] == 0:
                q.append(nxt)
    
    return result

result = sort_bfs(n,graph,indegree)
print(*result)
    