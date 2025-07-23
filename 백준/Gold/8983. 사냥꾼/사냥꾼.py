import sys
input = sys.stdin.readline

m,n,l = map(int,input().split())

shoot = list(map(int,input().split()))
shoot.sort()

animal= list(map(int,input().split()) for _ in range(n))

count = 0 

for x,y in animal:
    for s in shoot:
        if abs( s-x) + y <= l:
            count += 1
            break
    
    
print(count)