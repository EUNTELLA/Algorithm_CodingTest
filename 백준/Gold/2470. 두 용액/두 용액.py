import sys
input = sys.stdin.readline
from bisect import bisect_left
n = int(input())
ph = list(map(int, input().split()))
ph.sort()


min_sum= float('inf')
answer = (0,0)

for i in range(n-1):
    target = -ph[i]
    
    idx = bisect_left(ph,target, i+1,n)
    
    for j in [idx - 1 , idx]:
        if j > i and j<n:
            total = ph[i] + ph[j]
            if abs(total) < min_sum:
                min_sum = abs(total)
                answer = (ph[i],ph[j])
                
print(answer[0],answer[1])