import sys
input = sys.stdin.readline
houses = []
n,c = map(int,input().split())

houses = [int(input()) for _ in range(n)]
houses.sort()
 
start = 1 
end = houses [-1] - houses[0]
result = 0 

while start <= end:
    mid = (start + end)//2
    count = 1
    last = houses[0]
    
    for i in range(1,n):
        if houses[i] - last >= mid:
            count += 1
            last= houses[i]
            
    if count >= c:
        result = mid
        start = mid + 1
    else:
        end =mid - 1
        
        
print(result)