n,m = map(int,input().split())
num = [0] * n

for _ in range(m):
    i,j,k = map(int,input().split())   
    
    for c in range(i-1,j):
        num[c] = k
        
print(*num)

            
                
        
