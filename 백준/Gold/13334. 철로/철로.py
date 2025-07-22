import heapq

position= []
n = int(input())
for _ in range(n):
    x,y = map(int,input().split())
    if x> y:
        position.append((y,x))
    else:
        position.append((x,y)) 
d= int(input())

position.sort(key=lambda x: (x[1],x[0]))

l=[]
count = 0
max_count =0

for x , y in position:
    heapq.heappush(l,(x,y))

    count +=1
    
    while y - l[0][0]> d:
        heapq.heappop(l)
        
        count -= 1
        
        if count == 0:
            break
        
    max_count = max(count,max_count)
print(max_count)
        