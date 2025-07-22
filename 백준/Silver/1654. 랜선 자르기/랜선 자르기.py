import sys
input = sys.stdin.readline

k,n= map(int,input().split())

powerline = [int(input()) for _ in range(k)]

start = 1
end = max(powerline)
result= 0
 
while start <= end:
    mid = (start + end)//2
    
    count  = sum(power // mid for power in powerline)
    
    if count >= n:
        result = mid
        start = mid + 1
    else:
        end = mid -1
        
print(result)