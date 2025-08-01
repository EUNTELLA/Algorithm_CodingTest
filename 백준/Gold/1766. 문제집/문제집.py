from collections import deque
import heapq
n,m = map(int, input().split())

indegree = [0] * (n+1)

graph = [[] for _ in range(n+1)]

for _ in range(m):
    a,b = map(int,input().split())
    graph[a].append(b)
    indegree[b] += 1
    
heap=[]
    
for i in range(1,n+1):
    if indegree[i] == 0:
        heapq.heappush(heap,i)
        
while heap:
    target = heapq.heappop(heap)
    print(target, end=' ')
    for i in graph[target]:
        indegree[i] -= 1
        
        if indegree[i] == 0:
            heapq.heappush(heap,i)