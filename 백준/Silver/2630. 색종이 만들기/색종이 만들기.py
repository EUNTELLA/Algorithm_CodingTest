n = int(input())
arr = [list(map(int,input().split())) for _ in range(n)]

blue_count = 0
white_count =0


def is_same(n,x,y,init):
    for i in range(y,n+y):
        for j in range(x,n+x):
            if arr[i][j] != init:
                return False
    return True

def solve(n,x,y):
    
    
    
    global white_count, blue_count
    
    if is_same(n,x,y,1):
        blue_count +=1
        return
    
    if is_same(n,x,y,0):
        white_count +=1
        return
    
    if n == 1:
        return
    half = int(n/2)
        
        
    solve (half,x,y)
        
    solve (half,x+half , y)
    
    solve (half,x, y+half)
    
    solve(half, x+half, y+half)

solve(n,0,0)
print(white_count)
print(blue_count)
