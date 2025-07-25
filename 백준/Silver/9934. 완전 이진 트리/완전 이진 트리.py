import sys
sys.setrecursionlimit(10**6)


def build(start,end, depth):
    if start> end:
        return
    
    mid = (start+ end)//2
    level[depth].append(node[mid])

    build(start, mid-1 , depth +1)
    build(mid + 1 , end, depth+1)
    
    
k = int(input())
node = list(map(int,input().split()))
level = [[] for _ in range(k)]

build(0,len(node)-1,0)

for i in range(k):
    print(*level[i])